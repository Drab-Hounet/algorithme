import tkinter as tk
from tkinter import messagebox

from tkinter.filedialog import askopenfilename

import compression
import decompression
import toolbox

class Window:
    def __init__(self):
        self.toolbox = toolbox.ToolBox()
        self.TypeOperation = "compression"

    def popup(self, message):
        messagebox.showinfo("Information", message)

    def swapCheckbuttonCompress(self, stateCompressCheck, stateDecompressCheck, label):
        if (stateCompressCheck and stateDecompressCheck):
            self.TypeOperation = "compression"
            label.set("fichier à compresser")
            self.checkbuttonDecompress.toggle()
        elif(stateCompressCheck and not stateDecompressCheck):
            self.TypeOperation = "compression"
            label.set("fichier à compresser")

    def swapCheckbuttonDecompress(self, stateCompressCheck, stateDecompressCheck, label):
        if (stateCompressCheck and stateDecompressCheck ):
            self.TypeOperation = "decompression"
            label.set("fichier à décompresser")
            self.checkbuttonCompress.toggle()
        elif(not stateCompressCheck and stateDecompressCheck):
            self.TypeOperation = "decompression"
            label.set("fichier à décompresser")

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
            if(self.TypeOperation == "compression"):
                task = compression.CompressionTxt(text)
            else:
                task = decompression.DecompressionTxt(text)

            message = task.runProcess()['message']
            self.popup(message)

    def interface(self):
        window = tk.Tk()
        window.title('Compression - Decompression ')
        canvaWindow = tk.Canvas(
                            window,
                            bg      = '#80A0D8',
                            height  = '300',
                            width   = '500')
        window.resizable(0,0)

        label = tk.StringVar()
        label.set("fichier à compresser")
        labelCompress = tk.Label(
                            window,
                            textvariable    = label,
                            bg              = '#80A0D8')
        canvaWindow.create_window(10, 100, window = labelCompress, anchor = "w")

        path = tk.StringVar()
        pathCompress = tk.Label(
                            window,
                            textvariable    = path,
                            width           = '30',
                            anchor          = 'w')
        canvaWindow.create_window(250, 100, window = pathCompress)

        checkVarCompress = tk.IntVar()
        checkVarDecompress = tk.IntVar()
        self.checkbuttonCompress = tk.Checkbutton(
                                            window,
                                            text        = "Compression",
                                            bg          = '#80A0D8',
                                            onvalue     = True,
                                            offvalue    = False,
                                            variable    = checkVarCompress,
                                            command     = lambda : self.swapCheckbuttonCompress(checkVarCompress.get(), checkVarDecompress.get(), label))
        canvaWindow.create_window(200, 150, window = self.checkbuttonCompress, anchor = "w")

        self.checkbuttonDecompress = tk.Checkbutton(
                                            window,
                                            text        = "Decompression",
                                            bg          = '#80A0D8',
                                            onvalue     = True,
                                            offvalue    = False,
                                            variable    = checkVarDecompress,
                                            command     = lambda : self.swapCheckbuttonDecompress(checkVarCompress.get(), checkVarDecompress.get(), label))
        canvaWindow.create_window(200, 175, window = self.checkbuttonDecompress, anchor = "w")


        buttonChooseFileCompress = tk.Button(
                                        window,
                                        text        = 'Choisir ...',
                                        command     = lambda : self.interfaceCompression(path))
        canvaWindow.create_window(420, 100, window = buttonChooseFileCompress, width = "100")

        buttonRunProcess = tk.Button(
                                window,
                                text        = 'Run',
                                command     = lambda : self.execute(path))
        canvaWindow.create_window(420, 250, window = buttonRunProcess, width = "100")

        canvaWindow.pack()
        window.mainloop()
