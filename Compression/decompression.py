from keyMaker import *
import toolbox
from collections import OrderedDict

class DecompressionTxt:
    def __init__(self, text):
        self.textBrut = text
        self.toolbox = toolbox.ToolBox()
        keyMaker = KeyMaker()
        self.dictAlph2Char = keyMaker.makeKeys()

    def makeDictKey(self):
        try:
            longueur = int(self.textBrut[:8])
        except Exception as exception_retournee:
            # print("Voici l'erreur :", exception_retournee)
            return False

        self.textToDecompress = self.textBrut[3*longueur + 7 : ]
        self.textKey = self.textBrut[8:3*longueur + 7]
        textCompressedSplitted = self.toolbox.splitText(3,self.textKey)
        dictKey = []
        for index in range(len(textCompressedSplitted)):
            dictKey.append((self.dictAlph2Char[index], textCompressedSplitted[index]))
        return dict(dictKey)

    def decompression(self, dictKey):
        textToDecompress = self.toolbox.splitText(2,self.textToDecompress)
        for index in range(len(textToDecompress)):
            textToDecompress[index] = dictKey.get(textToDecompress[index], False)
            if (not textToDecompress[index]):
                return False
        return self.toolbox.toString((textToDecompress))

    def saveDeCompressedText(self,textDecompressed):
        self.toolbox.saveTxt(textDecompressed, "decompressionFile")
        return True

    def runProcess(self):
        dictKey = self.makeDictKey()
        if(not dictKey):
            return  {'state' : False, 'message' : "error ! impossible to find a correct key"}

        textDecompressed = self.decompression(dictKey)
        if(not textDecompressed):
            return  {'state' : False, 'message' : "error ! impossible to make a text decompressed from the file"}

        if(not self.saveDeCompressedText(textDecompressed)):
            return {'state' : False, 'message' : "error process to save the resultfile"}

        return {'state' : True, 'message' : "Decompression file are done"}
