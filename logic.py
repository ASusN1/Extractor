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

link = "https://www.youtube.com/watch?v=pyBEvMXVfL0" # input yt url here , this is a test sample link
save_path = r"D:\HackClubProjectList\video_test"# user input their own path here  #Make sure the path exists # error encouter: path does not exist ??? --> solution: add r before the save path so that python does not treat 
#\ as escape character
get_video_info(link, save_path)
