

class Node:

    word = ""
    frequency = 1
    nextNode = None

    def __init__(self, inputWord = "", inputNextNode = None):
        self.word = inputWord
        self.frequency = 1
        self.nextNode = inputNextNode

    def printNode(self):
        print "Name:", self.word
        print "Count:", self.frequency, "\n"


class WordsDictionary:

    rootNode = Node()
    leafNode = Node()


    def __init__(self, inputWord, inputNextNode = None):
        self.rootNode.word = inputWord
        self.rootNode.nextNode = inputNextNode
        self.leafNode = self.rootNode


    # A linear search adding for LinkedList
    def insert(self, inputWord):

        # check if the rootNode needs to be changed
        if (inputWord < self.rootNode.word):
            self.rootNode = Node(inputWord, self.rootNode)
            return

        previousNode = Node(0, self.rootNode)
        currentNode = self.rootNode

        # iterate through the list
        while ((currentNode.nextNode != None) and (currentNode.word < inputWord)):
            previousNode = currentNode
            currentNode = currentNode.nextNode

        # case 1: word is in the dictionary
        if (inputWord == currentNode.word):
            currentNode.frequency = currentNode.frequency + 1;

        # case 2: word is not in the dictionary, insert it in the middle
        if ((previousNode.word < inputWord) and (inputWord < currentNode.word)):
            previousNode.nextNode = Node(inputWord, currentNode)

        # case 3: word is not in the dictionary, insert it to the end
        if (currentNode.word < inputWord):
            currentNode.nextNode = Node(inputWord, currentNode.nextNode)
            # change the leaf node
            self.leafNode = self.leafNode.nextNode

    def get(self, lookupWord):

        currentNode = self.rootNode

        while (currentNode.nextNode != None):
            if (currentNode.word == lookupWord):
                return currentNode
            currentNode = currentNode.nextNode

        return None

    def delete(self, deleteWord):

        # check the root node
        if (self.rootNode.word == deleteWord):
            self.rootNode = self.rootNode.nextNode
            print deleteWord, "is deleted"
            return

        currentNode = self.rootNode

        while (currentNode.nextNode != None):
            if (currentNode.nextNode.word == deleteWord):
                currentNode.nextNode = currentNode.nextNode.nextNode
                return
            currentNode = currentNode.nextNode



    def min(self):
        return self.rootNode

    def max(self):
        return self.leafNode

    def printDictionary(self):
        currentNode = self.rootNode
        while(currentNode != None):
            print currentNode.word,  currentNode.frequency
            currentNode = currentNode.nextNode;
        print