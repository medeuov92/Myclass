from trie import *

my_sentence = open("input.txt","r+")

tree = my_sentence.read()

a = MyTrie()
words = tree.split()
for i in words:
    a.insert(i)

a.printMaxFreq()
