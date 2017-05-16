from compression import *
from tkinter.filedialog import askopenfilename

fname = askopenfilename(filetypes= [("All files", "*.txt")] )
textExemple = ""
with open(fname) as fileToCompress:
    for line in fileToCompress:
        textExemple = textExemple + line

compression = CompressionTxt(textExemple)
compression.saveCompressedText()
