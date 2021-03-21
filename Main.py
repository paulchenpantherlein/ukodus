import string
import re
import WordsLogic
import ReadWriteOperations

fileName = "writefile.txt"
text = "super cool random text ##"
ReadWriteOperations.writeToFile(fileName,text, False)
print(WordsLogic.filterWords(ReadWriteOperations.readFromFile(fileName)))
