import re

def filterWords(inputText):
    # In this pattern [a-z] denotes a class of
    #  characters from a to z. The + operator denotes the multiple occurrences of this character class. 
    #  Hence, to extract out the names of fruits and vegetables you can use the pattern as follows:
    # google regular experssion for more details but you dont have to. Its irrelevant for now.
    words_pattern = '[a-z]+'
    # re is regular expression from package re
    return re.findall(words_pattern, inputText, flags=re.IGNORECASE)