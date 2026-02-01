import yt_dlp

def get_video_info(link, save_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': save_path + '/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        print(f"Title: {info['title']}")
        print("Download completed successfully.")

def main():
    user_input_link = input("Enter the video link: ")
    user_input_path = input("Enter the save path: ")
    get_video_info(user_input_link, user_input_path)

if __name__ == "__main__":
    main()