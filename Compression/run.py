from compression        import *
from decompression      import *
from tkinter.filedialog import askopenfilename
from toolbox import *

fname = askopenfilename(filetypes= [("All files", "*.txt")] )
text = ""

with open(fname) as fileToCompress:
    for line in fileToCompress:
        text = text + line

compression = CompressionTxt(text)
compression.saveCompressedText()

# decompression = DecompressionTxt(text)
# decompression.saveDeCompressedText()
