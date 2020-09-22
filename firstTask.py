words = ['a','b','c','d','e','a','a','b','c']
myDict = dict((elem, [key for key, value in enumerate(words) if value == elem]) for elem in words)
print(myDict)
