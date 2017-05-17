import re

class KeyMaker:

    KEYS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def makeKeys(self):
        dictAlph1Char = re.findall('.', self.KEYS)
        dictAlph2Char = []
        for i in range(len(dictAlph1Char)):
            for j in range(len(dictAlph1Char)):
                dictAlph2Char.append(dictAlph1Char[i] + dictAlph1Char[j])

        return dictAlph2Char
