from pytube import YouTube

def download_youtube_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Display details about the video
        print(f"Downloading: {yt.title}")
        print(f"Resolution: {video_stream.resolution}")
        print(f"Filesize: {video_stream.filesize / 1024 / 1024:.2f} MB")

        # Download the video to the current directory
        video_stream.download()

        print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input YouTube video URL from the user
    video_url = input("Enter the YouTube video URL: ")
    
    # Download the video
    download_youtube_video(video_url)
