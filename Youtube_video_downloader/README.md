
# YouTube Video Downloader

This script allows users to download YouTube videos in the highest resolution available using the `pytube` library.

## How to Use:

1. Make sure you have Python installed on your system.
2. Install the `pytube` library:
   ```bash
   pip install pytube
   ```
3. Run the script:
   ```bash
   python youtube_downloader.py
   ```
4. Enter the YouTube video URL when prompted.

## Example:

```bash
Enter the YouTube video URL: https://www.youtube.com/watch?v=xyz123
Downloading: Example Video Title
Resolution: 1080p
Filesize: 20.34 MB
Download completed successfully!
```

## Prerequisites:

- Python 3.x
- `pytube` library (can be installed using `pip install pytube`)


# Explanation of the YouTube Video Downloader Python Script

This Python script allows users to download videos from YouTube using the `pytube` library. Below is an explanation of how each part of the code works.

## 1. Importing the Library

```python
from pytube import YouTube
```

The `pytube` library is used to interact with YouTube and download videos. Here, we are importing the `YouTube` class from the `pytube` module.

## 2. Defining the Download Function

```python
def download_youtube_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)
```
This function `download_youtube_video` accepts a `url` as input. The `YouTube` object is created by passing the YouTube video URL to the `YouTube` class, which helps retrieve the video metadata and streams.

## 3. Retrieving the Highest Quality Video Stream

```python
        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
```

Using the `streams` attribute of the `YouTube` object, the method `get_highest_resolution()` retrieves the highest quality video stream available for download.

## 4. Displaying Video Information

```python
        print(f"Downloading: {yt.title}")
        print(f"Resolution: {video_stream.resolution}")
        print(f"Filesize: {video_stream.filesize / 1024 / 1024:.2f} MB")
```

Here, we display some basic information about the video:
- `yt.title`: The title of the YouTube video.
- `video_stream.resolution`: The resolution of the video (e.g., 720p, 1080p).
- `video_stream.filesize`: The size of the video file in bytes, converted to megabytes (MB) using division by 1024 twice.

## 5. Downloading the Video

```python
        video_stream.download()
```

The `download()` method is used to download the video to the current working directory.

## 6. Handling Errors

```python
    except Exception as e:
        print(f"An error occurred: {e}")
```

If any error occurs during the download process (e.g., invalid URL or connection issues), the error is caught and printed to the console.

## 7. Main Execution Block

```python
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)
```

- The `__name__ == "__main__"` block ensures that the script runs only when executed directly, not when imported as a module.
- The user is prompted to input a YouTube video URL, and the `download_youtube_video` function is called with the provided URL.

## Summary:

This script:
1. Accepts a YouTube video URL from the user.
2. Retrieves the highest quality video stream available.
3. Downloads the video to the user's device.
