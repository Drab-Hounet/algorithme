import tkinter as tk
from tkinter import messagebox

from tkinter.filedialog import askopenfilename

import compression
import decompression
import toolbox

class Window:
    def __init__(self):
        self.toolbox = toolbox.ToolBox()

    def popup(self, message):
        messagebox.showinfo("Information", message)

    def interfaceCompression(self, path):
        fname = askopenfilename(filetypes= [("All files", "*.txt")] )
        path.set(fname)

    def execute(self, path):
        fname = path.get()
        text=''
        if (fname):
            with open(fname) as fileToCompress:
                for line in fileToCompress:
                    text = text + line
            # task = compression.CompressionTxt(text)
            task = decompression.DecompressionTxt(text)

            message = task.runProcess()['message']
            self.popup(message)

    def interface(self):
        window = tk.Tk()
        window.title('Compression - Decompression ')
        canvaWindow = tk.Canvas(window, bg = '#80A0D8', height = '300', width = '500')
        window.resizable(0,0)

        labelCompress = tk.Label(window, text ='fichier à compresser', bg = '#80A0D8')
        canvaWindow.create_window(80, 100, window = labelCompress)

        path = tk.StringVar()

        pathCompress = tk.Label(window, textvariable = path, width = '30', anchor = 'w')
        canvaWindow.create_window(250, 100, window = pathCompress)

        buttonChooseFileCompress = tk.Button(window, text  = 'Choisir ...', command = lambda : self.interfaceCompression(path))
        canvaWindow.create_window(420, 100, window = buttonChooseFileCompress, width = "100")

        buttonRunProcess = tk.Button(window, text  = 'Run', command = lambda : self.execute(path))
        canvaWindow.create_window(420, 250, window = buttonRunProcess, width = "100")

        canvaWindow.pack()
        window.mainloop()
