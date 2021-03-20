import string
import re
import WordsLogic
import ReadWriteOperations

fileName = "README.md"
print(WordsLogic.filterWords(ReadWriteOperations.readFile(fileName)))
