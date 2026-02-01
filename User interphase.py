#user interphase 
import tkinter as tk 
from tkinter import filedialog 
from logic import get_video_info

def browse_save_path(): 
    folder = filedialog.askdirectory()
    if folder:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder)

def download_video():
    link = url_entry.get()
    save_path = path_entry.get()
    get_video_info(link, save_path)

window = tk.Tk()
window.title("Extractor")

#video url label + input
tk.Label(window, text = "video Link").pack(pady=5)
url_entry = tk.Entry(window, width = 60)
url_entry.pack(pady= 5) 

#save path 
tk.Label(window, text = "Save Path").pack(pady=5)

path_frame = tk.Frame(window)
path_frame.pack(pady=5)

path_entry = tk.Entry(path_frame, width=45)
path_entry.pack(side =tk.LEFT)
tk.Button(path_frame, text ="Browse" , command = browse_save_path).pack(side = tk.LEFT, padx=5)

tk.Button(window, text = "Download", command = download_video).pack(pady=20)



window.mainloop()