
class ToolBox:

    def splitText(self, number, text):
        listSplitted = []
        countStrip = 1
        split = ""
        for letter in text:
            if (countStrip == 1):
                split = letter
            elif (countStrip < (number)):
                split = split + letter
            else:
                countStrip = 0
                split = split + letter
                listSplitted.append(split)
            countStrip += 1

        if (countStrip != 1):
            listSplitted.append(split)
        return listSplitted

    def toString(self, el):
        return (''.join(el))

    def saveTxt(self, text, namefile):
        with open(namefile + ".txt", "w") as f:
            f.write(text)
