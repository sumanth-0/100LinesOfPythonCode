# Screenshot Difference Detector

This script compares two images (e.g., screenshots) and generates a new, side-by-side image. The original image (left) has visual differences highlighted with red rectangles, and the new image (right) is shown for comparison.

It uses a robust **Morphological Opening** technique to intelligently separate "evident changes" from "irrelevant noise." This is the standard method for cleaning binary images in computer vision.

1.  It finds all pixel differences above a low threshold.
2.  It uses an **Erosion** pass to remove all small, scattered noise.
3.  It uses a **Dilation** pass to restore the size of the large, "evident" changes that survived.
4.  It highlights these remaining clean areas.

## Requirements

-   Python 3.x
-   `opencv-python`
-   `imutils`
-   `numpy`

## Installation

1.  **Clone or download** this repository (or just save `diff_detector.py`).

2.  **Install the required Python libraries** using pip:
    ```bash
    pip install opencv-python-headless numpy imutils
    ```

## Usage

Run the script from your terminal and provide three arguments:
1.  The path to the first image (the "before" image).
2.  The path to the second image (the "after" image).
3.  The path where the *combined output* image should be saved.

### Example

```bash
python diff_detector.py screenshot_before.png screenshot_after.png diff_combined.png