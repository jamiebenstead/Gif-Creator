import imageio
from pygifsicle import gifsicle
import tkinter as tk
from tkinter import filedialog, Text
import os

def loadFile():
    filename = filedialog.askopenfilename(initialdir="/Users/jamie/Apps/Coding/PythonGifCreator", title="Select MP4", 
    filetypes=(("mp4", "*.mp4"), ("all files", "*.*")))

    gifMaker(filename, '.gif')
    #print(filename)

root = tk.Tk()
root.title("Gif Creator")

canvas = tk.Canvas(root, height=300, width=300, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.75, relheight=0.75, relx=0.1, rely=0.1)

selectGif = tk.Button(root, text="Select MP4", padx=10, pady=5, fg="white", bg="#263D42", command=loadFile)
selectGif.pack()

clip = os.path.abspath('shipman-lowres.mp4')

def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    creatingGif = tk.Label(frame, text="Creating the gif")
    creatingGif.pack()

    for frames in reader:        
        writer.append_data(frames)

    finishedGif = tk.Label(frame, text="Finished creating the gif")
    finishedGif.pack()

    writer.close()

    OptomizingGif = tk.Label(frame, text="Optomizing...")
    OptomizingGif.pack()

    gifsicle(outputPath)

    finishedOptomizingGif = tk.Label(frame, text="Finished optomizing")
    finishedOptomizingGif.pack()

root.mainloop()