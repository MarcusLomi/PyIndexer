import os
from occurrence import occurrence

masterWordList = {} # will hold word : occurrenceObject key value pairs
currentFileWordDict = {}
currentFile = None
currentLineWordArray = None


rootDir = 'C:/Users/marca/Desktop/pytest/'

def main():
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)          # Name of the current directory
        for fname in fileList:
            print('\t%s' % fname)
            currentFile = open(dirName+"/"+fname)       # Opens file with the name at the exact path
            if currentFile is not None:
                print("successfully opened ", fname)
                # perform file operations here.
                for line in currentFile:
                    currentLineWordArray = line.split(" ")
                    for word in currentLineWordArray:
                        word = word.strip('\n')
                        word = word.strip('\t')
                        word = word.strip('.')
                        word = word.strip(',')
                        word = word.strip()
                        if word.isspace() or word == "":  # Skipping over blank words
                            continue
                        else:
                            word = word.strip()
                            updateMasterDict(word, fname)
                currentFile.close()
    for key in masterWordList:
        print("{", key, ":", masterWordList.get(key), "}")

def updateMasterDict(word, fname):
    # Main idea         Master = {"word":[(file1, 20), (file2, 14)]}
    # No idea how I will sort this stuff.
    if masterWordList.get(word) is None:
        masterWordList[word] = occurrence(fname, word)
    elif masterWordList.get(word) is not None:
        # Means that there is an entry here
        masterWordList.get(word).update(word,fname)          # Getting the occurence object
        #newentry = occurrenceentry.update(word, fname)       # Creating a new entry reference and updating it
        #masterWordList[word] = newentry                     # Placing the new entry back in

        # If there is a new filename, create the new occurrence

def updateoccurrence(occ):

    return None

main()