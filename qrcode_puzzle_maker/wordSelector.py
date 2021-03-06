

#you need a function or something to map every letter to a block number
def intializeDicts(wordsFile):
    f = open(wordsFile, 'r')
    words = f.read().split()
    numAlphabet = '23456789'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    letters = ''
    mySet = set()

    dictionary = dict()
    dic = dict()
    for x in numAlphabet:
        if(x == '7' or x == '9'):
            dictionary[x] = alphabet[i] + alphabet[i+1] + alphabet[i+2] + alphabet[i+3]
            i += 4
        else:
            dictionary[x] = alphabet[i] + alphabet[i+1] + alphabet[i+2]
            i += 3
    for p in words:
        failNumber = ''
        for a in p:
            for l in dictionary:
                if(a in dictionary[l]):
                    failNumber += l
        number = "".join(sorted(set(failNumber)))
        if number in dic:
            dic[number].append(p)
        else:
            dic[number] = [p]
    return dic

#each word gets all its letters converted to blocknumbers
#make the block numbers a set or ascending string so every word that fills those blocks has the same key
#add word to a list with the block numbers filled as the key
