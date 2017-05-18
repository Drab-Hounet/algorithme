from collections import OrderedDict
from toolbox import *
from keyMaker import *

class CompressionTxt:

    def __init__(self, text):
        self.toolbox = ToolBox()
        self.text = text
        keyMaker = KeyMaker()
        self.dictAlph2Char = keyMaker.makeKeys()

    def makeDictSortElementsRepeated(self):
        listElementsRepeatedWithCount = []
        listTrigramme = []
        listStripped = self.toolbox.splitText(3, self.text)
        for el in listStripped:
            count = 0
            for i in range(len(listStripped)):
                if (el == listStripped[i]):
                    count = count + 1
                    if (count > 1):
                        listStripped[i] = False
            if(el):
                listElementsRepeatedWithCount.append((el, [count, ""]))
                listTrigramme.append(el)
        return {'dict' : (OrderedDict(listElementsRepeatedWithCount)), 'trigrammes' : listTrigramme}

    def compression(self, dictSortElementsRepeated, listTrigramme ):
        indexEncoded = 0
        for key, value in dictSortElementsRepeated.items():
            if(indexEncoded == len(self.dictAlph2Char)):
                return False
            value[1] = self.dictAlph2Char[indexEncoded]
            indexEncoded +=1

        textCompressed = self.toolbox.splitText(3, self.text)
        for i in range(len(textCompressed)):
             textCompressed[i] = dictSortElementsRepeated[textCompressed[i]][1]
        return format(len(listTrigramme),"08d") + self.toolbox.toString(listTrigramme) + self.toolbox.toString(textCompressed)

    def saveCompressedText(self, textCompressed):
        self.toolbox.saveTxt(textCompressed, "textCompressed")
        return True

    def runProcess(self):
        dictSortElementsRepeated    = self.makeDictSortElementsRepeated()['dict']
        listTrigramme               = self.makeDictSortElementsRepeated()['trigrammes']
        textCompressed              = self.compression(dictSortElementsRepeated, listTrigramme)

        if (not textCompressed):
            return {'state' : False, 'message' : "the size of the lengh key is too small"}

        if (not self.saveCompressedText(textCompressed)):
            return {'state' : False, 'message' : "error process to save the result file"}

        return {'state' : True, 'message' : "Compression file are done"}

#///////////////////////////////////////////////////////////////////////
