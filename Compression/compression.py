from collections import OrderedDict
import re

class CompressionTxt:

    def __init__(self, text):
        self.text = text
        dictAlph1Char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        dictAlph1Char = re.findall('.', str.upper(dictAlph1Char))
        dictAlph2Char = []
        for i in range(len(dictAlph1Char)):
            for j in range(len(dictAlph1Char)):
                dictAlph2Char.append(dictAlph1Char[i] + dictAlph1Char[j])
        self.dictAlph1Char = dictAlph1Char
        self.dictAlph2Char = dictAlph2Char

    def stripText(self):
        listStripped = []
        countStrip = 0
        strip = ""
        for letter in self.text:
            if (countStrip == 0):
                strip = letter
            elif (countStrip < 2):
                strip = strip + letter
            else:
                countStrip = -1
                strip = strip + letter
                listStripped.append(strip)
            countStrip +=1
        if (strip != 3):
            listStripped.append(strip)

        for a in listStripped:
            if (len(a) < 3):
                print (a)
        # print (listStripped)
        return listStripped
        # return  re.findall( ".{1," + str(number) + "}", str.upper(self.text))

    def makeDictSortElementsRepeated(self):
        listSortElementsRepeated = []
        listStripped = self.stripText()
        # print(listStripped)
        for el in listStripped:
            count = 0
            for i in range(len(listStripped)):
                if (el == listStripped[i]):
                    count = count + 1
                    if (count > 1):
                        listStripped[i] = False
            if(el):
                listSortElementsRepeated.append((el, [count, ""]))
        return (OrderedDict(listSortElementsRepeated))

    def compression(self):
        dictSortElementsRepeated = self.makeDictSortElementsRepeated()
        indexEncoded = 0
        for key, value in dictSortElementsRepeated.items():
            # if(value[0] == 1):
            #     value[1] = dictAlph2Char[indexEncoded]
            #     indexEncoded +=1
            if(indexEncoded == len(self.dictAlph2Char)):
                return "error : not enough keys to compress the file"
            value[1] = self.dictAlph2Char[indexEncoded]
            indexEncoded +=1

        textCompressed = self.stripText()
        for i in range(len(textCompressed)):
             textCompressed[i] = dictSortElementsRepeated[textCompressed[i]][1]

        return (''.join(textCompressed))

    def saveCompressedText(self):
        with open("textCompressed.txt", "w") as f:
            f.write(self.compression())

    def decompression(txt):
        pass

#///////////////////////////////////////////////////////////////////////
