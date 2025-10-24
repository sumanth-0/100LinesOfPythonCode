"""
YouTube Video Downloader with Resolution Selection
Downloads YouTube videos in user-specified resolution using yt-dlp
"""

import yt_dlp
import os

def get_available_resolutions(url):
    """Extract all available resolutions for a video"""
    ydl_opts = {'quiet': True, 'no_warnings': True}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        
        # Get unique resolutions with video codec
        resolutions = set()
        for f in formats:
            if f.get('height') and f.get('vcodec') != 'none':
                resolutions.add(f['height'])
        
        return sorted(resolutions, reverse=True), info.get('title', 'video')

def download_video(url, resolution, output_path='downloads'):
    """Download video with specified resolution"""
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"\n📥 Downloading in {resolution}p...")
        ydl.download([url])
        print("✅ Download completed!")

def main():
    """Main function for interactive video downloading"""
    print("=" * 50)
    print("🎬 YouTube Video Downloader")
    print("=" * 50)
    
    # Get video URL
    url = input("\n📌 Enter YouTube URL: ").strip()
    
    if not url:
        print("❌ No URL provided!")
        return
    
    try:
        # Fetch available resolutions
        print("\n🔍 Fetching available resolutions...")
        resolutions, title = get_available_resolutions(url)
        
        if not resolutions:
            print("❌ No video formats found!")
            return
        
        # Display video title
        print(f"\n📺 Video: {title}")
        
        # Display available resolutions
        print("\n📊 Available Resolutions:")
        for i, res in enumerate(resolutions, 1):
            print(f"  {i}. {res}p")
        
        # Get user choice
        choice = int(input(f"\n✨ Select resolution (1-{len(resolutions)}): "))
        
        if 1 <= choice <= len(resolutions):
            selected_resolution = resolutions[choice - 1]
            
            # Optional: Custom output path
            custom_path = input("\n📁 Output folder (press Enter for 'downloads'): ").strip()
            output_path = custom_path if custom_path else 'downloads'
            
            # Download video
            download_video(url, selected_resolution, output_path)
            
        else:
            print("❌ Invalid choice!")
            
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
    except KeyboardInterrupt:
        print("\n\n⚠️  Download cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
