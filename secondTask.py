def issetInArray(array, value):
	for i in array: 
		if (i == value):
			return True
	return False

def numberOfDublicateItems(array, item):
  count = 0
  for i in array:
    if i == item:
      count +=1
  return count

def removeDuplicateItems(array):
  for i in array:
    while (numberOfDublicateItems(array, i) > 1):
      array.remove(i)
      
a = [2,5,6,4]
b = [2,3,5,8]

removeDuplicateItems(a)
removeDuplicateItems(b)

firstArrayLen = len(a)

for i in range(0, len(a)):
  if (issetInArray(b, a[firstArrayLen - i - 1])):
    b.remove(a[firstArrayLen - i - 1])
  else:
    b.append(a[firstArrayLen - i - 1])
    a.remove(a[firstArrayLen - i - 1])
print (a)
print (b)
print (len(a)/len(b))
