def readFromFile(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

# function to write content to file. by default we append content to existing file
def writeToFile(filename, value, append=True):
    #if we pass value false to function then operation is 'w' meaning we delete existing content
    operation = 'a' if append else 'w' 
    f = open(filename, operation )
    f.write(value)
    f.close()
