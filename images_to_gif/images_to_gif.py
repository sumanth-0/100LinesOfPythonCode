from PIL import Image
import os
import re

def sort_images(image_files):
    return sorted(image_files, key=lambda file: int(re.sub(r'[^0-9]', '', file)), reverse=False)

# Folder where your images are stored
image_folder = 'images'

# Get all image files from the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg'))]

# Sort images by name (you might need to adjust this depending on your naming scheme)
image_files = sort_images(image_files)

# Load images into a list
images = [Image.open(os.path.join(image_folder, f)) for f in image_files]

# Save as GIF
images[0].save('output.gif', save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)

# Parameters:
# 'save_all=True' saves all the images as frames in the gif
# 'append_images' is the list of images to append as frames
# 'duration=500' sets the time between frames in milliseconds (500ms in this case)
# 'loop=0' makes the GIF loop infinitely (change this for finite loops)
