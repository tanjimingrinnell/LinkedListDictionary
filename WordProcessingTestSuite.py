from Dictionary import *
import time

def readToDictionary(file):
    newDictionary = WordsDictionary("aaaaPlaceHolder")
    for line in file:
        for word in line.split():
            newDictionary.insert(word)

    newDictionary.delete("aaaaPlaceHolder")
    return newDictionary

def testCase(wordDictionary, getKey, insertKey, deleteKey):
    startMin = time.time()
    wordDictionary.min()
    endMin = time.time()

    startMax = time.time()
    wordDictionary.max()
    endMax = time.time()

    startGet = time.time()
    wordDictionary.get(getKey)
    endGet = time.time()

    startInsert = time.time()
    wordDictionary.insert(insertKey)
    endInsert = time.time()

    startDelete = time.time()
    wordDictionary.delete(deleteKey)
    endDelete = time.time()

    timerList = [endMin - startMin, endMax - startMax, endGet - startGet, endInsert - startInsert, endDelete - startDelete]
    returnList = [x * 1000 for x in timerList]
    return returnList

def testCasePrint(testData):
    print "Min takes ", testData[0], "ms"
    print "Max takes ", testData[1], "ms"
    print "Get takes ", testData[2], "ms"
    print "insert takes ", testData[3], "ms"
    print "delete takes ", testData[4], "ms"
    print ""

# import text files to files in python
Holmes = open("Holmes.txt", "r")
OxfordMedical = open("OxfordMedical.txt", "r")
words = open("words.txt", "r")
words2 = open("words2.txt", "r")


# turn files into dictionaries
HolmesDictonary = readToDictionary(Holmes)
OxfordMedicalDictonary = readToDictionary(OxfordMedical)
words2Dictonary = readToDictionary(words2)

# run the test
testDataHolmes = testCase(HolmesDictonary, "Holmes", "wumpus", "king")
testDataOxfordMedical = testCase(OxfordMedicalDictonary, "Anteater", "aardvark", "the")
testDatawords2 = testCase(words2Dictonary, "likely", "hyphenation", "brisk")

# print results
print("Test for Holmes.txt\n")
testCasePrint(testDataHolmes)
print("Test for OxfordMedical.txt\n")
testCasePrint(testDataOxfordMedical)
print("Test for words2.txt\n")
testCasePrint(testDatawords2)

# close all files
Holmes.close()
OxfordMedical.close()
words.close()
words2.close()

