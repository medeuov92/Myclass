


class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
        self.freq = 0
        self.isEndOfWord = False
  
class MyTrie: 
      
    def __init__(self): 
        self.root = self.getNode()
  
    def getNode(self): 
        return TrieNode() 
  
    def _charToIndex(self,ch): 
        return ord(ch)-ord('A')

    def _indexToChar(self,index):
        return chr(ord('A')+index)
  
    def insert(self,key):
        if not self.search(key):
            pCrawl = self.root 
            length = len(key) 
            for level in range(length):
                if key[level].isupper():
                    index = self._charToIndex(key[level]) 
                    if not pCrawl.children[index]: 
                        pCrawl.children[index] = self.getNode()
                    pCrawl = pCrawl.children[index]
                    pCrawl.freq += 1
            pCrawl.isEndOfWord = True
        else:
            self.updateFreq(key)
  
    def search(self, key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length):
            if key[level].isupper():
                index = self._charToIndex(key[level])
                if not pCrawl.children[index]: 
                    return False
                pCrawl = pCrawl.children[index]
  
        return pCrawl != None and pCrawl.isEndOfWord

    def updateFreq(self,key):
        pCrawl = self.root 
        length = len(key) 
        for level in range(length):
            if key[level].isupper():
                index = self._charToIndex(key[level])
                if not pCrawl.children[index]: 
                    pCrawl.children[index] = self.getNode()
                pCrawl = pCrawl.children[index]
                pCrawl.freq += 1
  
        pCrawl.isEndOfWord = True

    def printAll(self,pCrawl,wrd):
        maxFreq = pCrawl.freq
        for i in range(26):
            if pCrawl.children[i] and pCrawl.children[i].freq >= maxFreq:
                maxFreq = pCrawl.children[i].freq
        for i in range(26):
            if pCrawl.children[i] and pCrawl.children[i].freq == maxFreq:
                print(wrd + self._indexToChar(i),end=", ")
                self.printAll(pCrawl.children[i],wrd + self._indexToChar(i))

    def printMaxFreq(self):
        self.printAll(self.root,"")
        

