import tkinter as tk
from tkinter import messagebox

from compression        import *
from decompression      import *
from tkinter.filedialog import askopenfilename
from toolbox            import *

def compression():
    fname = askopenfilename(filetypes= [("All files", "*.txt")] )
    path.set(fname)

def runProcess():
    print(path.get())
    fname = path.get()
    text=''
    if (fname):
        with open(fname) as fileToCompress:
            for line in fileToCompress:
                text = text + line
        compression = CompressionTxt(text)
        compression.saveCompressedText()


window = tk.Tk()
window.title('Compression - Decompression ')
canvaWindow = tk.Canvas(window, bg = '#80A0D8', height = '300', width = '500')
window.resizable(0,0)

labelCompress = tk.Label(window, text ='fichier à compresser', bg = '#80A0D8')
canvaWindow.create_window(80, 100, window = labelCompress)

path = tk.StringVar()

pathCompress = tk.Label(window, textvariable = path, width = '30', anchor = 'w')
canvaWindow.create_window(250, 100, window = pathCompress)

buttonChooseFileCompress = tk.Button(window, text  = 'Choisir ...', command = compression)
canvaWindow.create_window(420, 100, window = buttonChooseFileCompress, width = "100")

buttonRunProcess = tk.Button(window, text  = 'Run', command = runProcess)
canvaWindow.create_window(420, 250, window = buttonRunProcess, width = "100")

canvaWindow.pack()

window.mainloop()

# fname = askopenfilename(filetypes= [("All files", "*.txt")] )
# text = ""
# if (fname):
#
#     with open(fname) as fileToCompress:
#         for line in fileToCompress:
#             text = text + line

    # compression = CompressionTxt(text)
    # compression.saveCompressedText()

    # decompression = DecompressionTxt(text)
    # decompression.saveDeCompressedText()
