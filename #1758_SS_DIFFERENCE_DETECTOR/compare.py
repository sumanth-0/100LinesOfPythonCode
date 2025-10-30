import cv2
import imutils
import numpy as np
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def compare_images(img_path1, img_path2, output_path):
    """
    Compares two images and saves a new image with differences
    highlighted by red rectangles, using a manual threshold.
    """
    # Load the two images
    try:
        imageA = cv2.imread(img_path1)
        imageB = cv2.imread(img_path2)
        
        if imageA is None or imageB is None:
            logging.error("Could not read one or both images. Check file paths.")
            return
    except Exception as e:
        logging.error(f"Error loading images: {e}")
        return

    # Check if images have the same dimensions
    if imageA.shape != imageB.shape:
        logging.warning("Images have different sizes. Resizing second image to match first.")
        # We must make a copy of imageB for the final output stack
        imageB_resized = cv2.resize(imageB, (imageA.shape[1], imageA.shape[0]))
    else:
        imageB_resized = imageB

    # 1. Convert images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB_resized, cv2.COLOR_BGR2GRAY)

    # 2. Compute the absolute difference between the grayscale images
    diff = cv2.absdiff(grayA, grayB)

    # 3. Apply a low threshold.
    # This creates a "dirty mask" that includes *all* potential
    # changes, both signal and noise.
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    # 4. (THE NEW METHOD) Use Morphological Opening
    # This is the key. It removes small, scattered noise (irrelevant details)
    # while preserving large, grouped areas (evident changes).
    
    # Define a 5x5 kernel (the "size" of noise to remove)
    kernel = np.ones((5, 5), np.uint8)
    
    # Apply the operation. Erosion (removes noise) -> Dilation (restores signal)
    clean_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # 5. Find contours (outlines) on the *clean mask*
    cnts = cv2.findContours(clean_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    logging.info(f"Found {len(cnts)} potential differences...")

    # 6. Create a copy of imageA to draw on
    imageA_with_boxes = imageA.copy()

    # Loop over contours and filter by size
    diff_count = 0
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        
        # Final filter for any tiny specks that survived
        if w > 10 and h > 10:
            diff_count += 1
            # Draw on the copy
            cv2.rectangle(imageA_with_boxes, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # 7. Create side-by-side output
    output_image = np.hstack([imageA_with_boxes, imageB_resized])

    try:
        cv2.imwrite(output_path, output_image)
        logging.info(f"Successfully saved diff image to {output_path}")
        logging.info(f"Highlighted {diff_count} significant difference areas.")
    except Exception as e:
        logging.error(f"Error saving output image: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("\nUsage: python diff_detector.py <image1_path> <image2_path> <output_path>")
        print("Example: python diff_detector.py screenshot1.png screenshot2.png diff.png\n")
        sys.exit(1)
    
    img1 = sys.argv[1]
    img2 = sys.argv[2]
    output = sys.argv[3]
    
    compare_images(img1, img2, output)