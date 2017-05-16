import re

class CompressionTxt:

    NUMBER = 3

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

    def stripText(self, number):
        return  re.findall( ".{1," + str(number) + "}", str.upper(self.text))

    def makeDictSortElementsRepeated(self):
        listSortElementsRepeated = []
        listStripped = self.stripText(self.NUMBER)
        for el in listStripped:
            count = 0
            for i in range(len(listStripped)):
                if (el == listStripped[i]):
                    count = count + 1
                    # if (count > 1):
                    if (count > 1):
                        listStripped[i] = False
            if(el):
                listSortElementsRepeated.append((el, [count, ""]))
        return dict(listSortElementsRepeated)

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

            textCompressed = self.stripText(self.NUMBER)
            #convert three characters by 2 characters

            for i in range(len(textCompressed)):
                 textCompressed[i] = dictSortElementsRepeated[textCompressed[i]][1]

        return (''.join(textCompressed))

    def saveCompressedText(self):
        with open("textCompressed.txt", "w") as f:
            f.write(self.compression())

    def decompression(txt):
        pass

#///////////////////////////////////////////////////////////////////////
