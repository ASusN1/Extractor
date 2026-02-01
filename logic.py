import yt_dlp

def get_video_info(link, save_path):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path + '/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            print(f"Title: {info['title']}")
            print("Download completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

link = "" # input yt url here
save_path = ""# user input their own path here
get_video_info(link, save_path)