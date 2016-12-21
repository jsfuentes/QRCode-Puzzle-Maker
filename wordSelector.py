f = open('words.txt', 'r')
words = f.read().split()
import itertools 
#you need a function or something to map every letter to a block number
def makeWord(num:str):
    numAlphabet = '23456789'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    letters = ''
    mySet = set()

    dictionary = dict()
    for x in numAlphabet:
        if(x == '7' or x == '9'):
            dictionary[x] = alphabet[i] + alphabet[i+1] + alphabet[i+2] + alphabet[i+3]
            i += 4
        else:
            dictionary[x] = alphabet[i] + alphabet[i+1] + alphabet[i+2]
            i += 3
    for q in num:
        if(q != 1 and q != 0):
            letters += dictionary[q]
    for j in itertools.permutations(letters):
        print(''.join(j))
makeWord('23')
#each word gets all its letters converted to blocknumbers
#make the block numbers a set or ascending string so every word that fills those blocks has the same key
#add word to a list with the block numbers filled as the key
