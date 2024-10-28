import os
import random
from PIL import Image
def make_collage(images, filename, width, init_height):
    """
    Make a collage image with a width equal to `width` from `images` and save to `filename`.
    """
    if not images:
        print('No images for collage found!')
        return False
    margin_size = 2
    # run until a suitable arrangement of images is found
    while True:
        # copy images to images_list
        images_list = images[:]
        coefs_lines = []
        images_line = []
        x = 0
        while images_list:
            # get first image and resize to `init_height`
            img_path = images_list.pop(0)
            img = Image.open(img_path)
            img.thumbnail((width, init_height))
            # when `x` will go beyond the `width`, start the next line
            if x > width:
                coefs_lines.append((float(x) / width, images_line))
                images_line = []
                x = 0
            x += img.size[0] + margin_size
            images_line.append(img_path)
        # finally add the last line with images
        coefs_lines.append((float(x) / width, images_line))

        # compact the lines, by reducing the `init_height`, if any with one or less images
        if len(coefs_lines) <= 1:
            break
        if any(map(lambda c: len(c[1]) <= 1, coefs_lines)):
            # reduce `init_height`
            init_height -= 10
        else:
            break

    # get output height
    out_height = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            out_height += int(init_height / coef) + margin_size
    if not out_height:
        print('Height of collage could not be 0!')
        return False

    collage_image = Image.new('RGB', (width, int(out_height)), (35, 35, 35))
    # put images to the collage
    y = 0
    for coef, imgs_line in coefs_lines:
        if imgs_line:
            x = 0
            for img_path in imgs_line:
                img = Image.open(img_path)
                # if need to enlarge an image - use `resize`, otherwise use `thumbnail`, it's faster
                k = (init_height / coef) / img.size[1]
                if k > 1:
                    img = img.resize((int(img.size[0] * k), int(img.size[1] * k)), Image.LANCZOS)
                else:
                    img.thumbnail((int(width / coef), int(init_height / coef)), Image.LANCZOS)
                if collage_image:
                    collage_image.paste(img, (int(x), int(y)))
                x += img.size[0] + margin_size
            y += int(init_height / coef) + margin_size
    collage_image.save(filename)
    return True

def main():
    """Main function to create a collage from user-provided folder."""
    image_folder = input("Enter the path to your image folder (e.g., C:/pictures/whatever): ")
    output_file = input("Enter the output file name (e.g., collage.png): ")
    collage_width = int(input("Enter the resulting collage image width (e.g., 800): "))
    init_height = int(input("Enter the initial height for resizing the images (e.g., 200): "))
    shuffle_images = input("Would you like to shuffle the images? (yes/no): ").strip().lower() == 'yes'
    files = [os.path.join(image_folder, fn) for fn in os.listdir(image_folder)] # Get images
    images = [fn for fn in files if os.path.splitext(fn)[1].lower() in ('.jpg', '.jpeg', '.png')]
    if not images:
        print('No images for making collage! Please select another directory with images!')
        return
    
    if shuffle_images: # Shuffle images if needed
        random.shuffle(images)

    print('Making collage...')
    res = make_collage(images, output_file, collage_width, init_height)
    if not res:
        print('Failed to create collage!')
        return
    print('Collage is ready!')
if __name__ == '__main__':
    main()

