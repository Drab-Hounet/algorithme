from keyMaker import *
from toolbox import *
from collections import OrderedDict

class DecompressionTxt:
    def __init__(self, text):
        self.toolbox = ToolBox()
        longueur = int(text[:8])
        self.textToDecompress = text[3*longueur + 7 : ]
        self.textKey = text[8:3*longueur + 7]
        keyMaker = KeyMaker()
        self.dictAlph2Char = keyMaker.makeKeys()

    def makeDictKey(self):
        textCompressedSplitted = self.toolbox.splitText(3,self.textKey)
        dictKey = []
        for index in range(len(textCompressedSplitted)):
            dictKey.append((self.dictAlph2Char[index], textCompressedSplitted[index]))
        return dict(dictKey)

    def decompression(self):
        dictKey = self.makeDictKey()
        textToDecompress = self.toolbox.splitText(2,self.textToDecompress)
        # print(''.join(textToDecompress))
        for index in range(len(textToDecompress)):
            textToDecompress[index] = dictKey[textToDecompress[index]]
        return self.toolbox.toString((textToDecompress))

    def saveDeCompressedText(self):
        self.toolbox.saveTxt(self.decompression(), "decompressionFile")
