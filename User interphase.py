import tkinter as tk
from tkinter import filedialog
from logic import get_video_info


def browse_folder():
    """Open folder picker and set the path"""
    folder = filedialog.askdirectory()
    if folder:
        save_path_input.delete(0, tk.END)
        save_path_input.insert(0, folder)


def start_download():
    """Get inputs and start download"""
    video_url = url_input.get()
    save_location = save_path_input.get()
    get_video_info(video_url, save_location)


# Create main window
window = tk.Tk()
window.title("Video Extractor")
window.geometry("600x800")

# Save path section
tk.Label(window, text="Save Path").pack(pady=5)

path_section = tk.Frame(window)
path_section.pack(pady=5)

save_path_input = tk.Entry(path_section, width=30)
save_path_input.pack(side=tk.LEFT)

browse_button = tk.Button(path_section, text="Browse", command=browse_folder)
browse_button.pack(side=tk.LEFT, padx=5)

# Download button
download_button = tk.Button(window, text="Download", command=start_download)
download_button.pack(pady=20)

# Video URL section - center right with spacing
video_section = tk.Frame(window)
video_section.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10, pady=10)

tk.Label(video_section, text="Video URL").pack()
url_input = tk.Entry(video_section, width=40)
url_input.pack(pady=5)

# Start the app
window.mainloop()