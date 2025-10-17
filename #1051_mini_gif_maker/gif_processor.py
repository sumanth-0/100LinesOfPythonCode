import os
from PIL import Image

# Compatibility for Pillow constants
PALETTE_ADAPTIVE = getattr(Image, 'ADAPTIVE', None)

class GifProcessor:
    """Handles the image manipulation logic for creating GIFs."""

    def __init__(self):
        self.frames_paths = []  # List of file paths
        self.frames_images = []  # List of PIL.Image objects

    def add_images(self, paths):
        """Adds new images, skipping duplicates or invalid files."""
        added_count = 0
        errors = []
        for p in paths:
            p = os.path.abspath(p)
            if p in self.frames_paths:
                continue
            try:
                img = Image.open(p).convert("RGBA")
                self.frames_paths.append(p)
                self.frames_images.append(img)
                added_count += 1
            except Exception as e:
                errors.append(f"Could not load {os.path.basename(p)}: {e}")
        return added_count, errors

    def remove_image(self, index):
        """Removes an image at the specified position."""
        if 0 <= index < len(self.frames_paths):
            del self.frames_paths[index]
            del self.frames_images[index]

    def move_image(self, old_index, direction):
        """Moves an image up or down in the list."""
        new_index = old_index + direction
        if 0 <= new_index < len(self.frames_paths):
            # Swap elements between the lists
            p_path, p_img = self.frames_paths.pop(old_index), self.frames_images.pop(old_index)
            self.frames_paths.insert(new_index, p_path)
            self.frames_images.insert(new_index, p_img)
            return True
        return False

    def get_frame_basenames(self):
        """Returns only the basenames of the loaded image files."""
        return [os.path.basename(p) for p in self.frames_paths]

    def _prepare_frames_for_saving(self):
        """Prepares frames for saving by resizing them to a common size."""
        if not self.frames_images:
            raise ValueError("No frames to save.")

        widths, heights = zip(*(im.size for im in self.frames_images))
        target_size = (max(widths), max(heights))

        prepared = []
        for im in self.frames_images:
            if im.size == target_size:
                prepared.append(im.copy())
                continue

            # Paste the image centered onto a transparent background
            bg = Image.new("RGBA", target_size, (255, 255, 255, 0))
            x = (target_size[0] - im.width) // 2
            y = (target_size[1] - im.height) // 2
            bg.paste(im, (x, y), im)
            prepared.append(bg)

        return prepared

    def save_gif(self, save_path, duration, loop):
        """Saves the images as an animated GIF file."""
        prepared_frames = self._prepare_frames_for_saving()

        # Convert to 'P' mode (paletted) for GIF format
        paletted_frames = []
        for frame in prepared_frames:
            if PALETTE_ADAPTIVE is not None:
                paletted_frames.append(frame.convert("P", palette=PALETTE_ADAPTIVE))
            else:
                paletted_frames.append(frame.convert("P"))

        if not paletted_frames:
            raise ValueError("No valid frames to save.")

        first, *rest = paletted_frames
        first.save(
            save_path,
            save_all=True,
            append_images=rest,
            duration=duration,
            loop=loop,
            optimize=False
        )