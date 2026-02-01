from pytube import YouTube
from sys import argv 

link = argv[1]
youtube = YouTube(link)

print("Title: ", youtube.title)
print("Number of views: ", youtube.views)

yd = youtube.streams.get_highest_resolution() #dowanlod the highest resolution of the video 

yd.download('D:\\HackClubProjectList\\video_test') #subject to change, the user input their own path here 