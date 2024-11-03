from PIL import Image
import os


def split_gif_to_frames(gif_path: str, output_folder: str) -> None:
    """
    Splits a GIF file into individual frames and saves them as PNG files.

    Parameters:
    gif_path (str): The file path to the GIF to be split.
    output_folder (str): The directory where the individual frames should be saved.

    Raises:
    FileNotFoundError: If the specified GIF file or output folder does not exist.
    ValueError: If the provided file is not a valid GIF format.
    """

    # Check if the GIF file exists
    if not os.path.isfile(gif_path):
        raise FileNotFoundError(f"GIF file not found: {gif_path}")

    # Check if the output directory exists, create it if it doesn't
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError as e:
            raise OSError(f"Failed to create output directory: {output_folder}") from e

    # Try opening the GIF file
    try:
        with Image.open(gif_path) as gif:
            if gif.format != "GIF":
                raise ValueError(f"Provided file is not a valid GIF format: {gif_path}")

            # Process each frame in the GIF
            frame_number = 0
            while True:
                # Construct the output file path for each frame
                frame_path = os.path.join(output_folder, f"frame_{frame_number:03}.png")

                # Save the current frame as a PNG
                gif.save(frame_path, "PNG")

                # Move to the next frame
                frame_number += 1
                try:
                    gif.seek(frame_number)
                except EOFError:
                    # Break loop if no more frames are available
                    break
            print(f"GIF split into {frame_number} frames and saved to {output_folder}.")
    except Exception as e:
        raise RuntimeError(f"Failed to split GIF into frames: {e}")


split_gif_to_frames("example.gif", "result")
