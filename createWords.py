import urllib.request
response = urllib.request.urlopen('https://raw.githubusercontent.com/dwy'
                          'l/english-words/master/words.txt')
print(response.read())