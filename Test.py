import string
def readfile(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def filterWords(inputText):
    filterresult = ''
    filterresult.join([x for x in inputText if x in string.ascii_letters + '\'- '])
    return filterresult

print(filterWords(readfile("README.md"))) 
print("bla")