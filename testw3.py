from math import ceil, floor
lines = [int(line.rstrip('\n')) for line in open('D:\QuickSort.txt')]
firstTen = lines

def partitionFirstElement (arr):
  r = len(arr)
  if(r == 1 or r == 0):
    return 0
  comparisons = len(arr) - 1
  p = arr[0]
  i = 1
  for j in range(1, r):
    if arr[j] < p:
      temp = arr[j]
      arr[j] = arr[i]
      arr[i] = temp
      i += 1
  arr[0] = arr[i - 1]
  arr[i - 1] = p
  # print(arr)
  # print('i - 1', arr[i - 1])
  # print('i - 2', arr[0:i - 1])
  count1 = partitionFirstElement(arr[0:i - 1]) 
  count2 = partitionFirstElement(arr[i:r]) 

  return comparisons + count1 + count2

print (partitionFirstElement(firstTen))

def partitionLastElement (arr):
  r = len(arr)
  if(r == 1 or r == 0):
    return 0
  comparisons = len(arr) - 1
  p = arr[0]
  arr[0] = arr[r - 1]
  arr[r - 1] = p
  i = 1
  for j in range(1, r):
    if arr[j] < arr[0]:
      temp = arr[j]
      arr[j] = arr[i]
      arr[i] = temp
      i += 1
  arr[0] = arr[i - 1]
  arr[i - 1] = p
  # print(arr)
  # print('i - 1', arr[i - 1])
  # print('i - 2', arr[0:i - 1])
  count1 = partitionLastElement(arr[0:i - 1]) 
  count2 = partitionLastElement(arr[i:r]) 

  return comparisons + count1 + count2

# print (partitionLastElement(firstTen))

def partitionMediumElement (arr):
  r = len(arr)
  if(r == 1 or r == 0):
    return 0
  if(r == 2):
    return 1
  comparisons = len(arr) - 1
  medium = int(ceil(float(r)/2)) - 1
  a = 0
  if(arr[0] < arr[medium] and arr[0] < arr[r-1]):
    if(arr[medium] < arr[r-1]):
      p = arr[medium]
      a = medium
    else:
      p = arr[r-1]
      a = r-1
  elif(arr[r-1] < arr[0] and arr[r-1] < arr[medium]):
    if(arr[0] < arr[medium]):
      p = arr[0]
    else:
      p = arr[medium]
      a = medium
  elif (arr[0] < arr[r-1]):
      p = arr[0]
  else:
      p = arr[r-1]
      a = r-1

  # print(arr)
  # print(arr[0], arr[medium], arr[r-1])
  # print('p', p)

  arr[0], arr[a] = arr[a], arr[0]

  i = 1
  for j in range(1, r):
    if arr[j] < arr[0]:
      temp = arr[j]
      arr[j] = arr[i]
      arr[i] = temp
      i += 1
  arr[0] = arr[i - 1]
  arr[i - 1] = p
  # print(arr)
  # print('i - 1', arr[i - 1])
  # print('i - 2', arr[0:i - 1])
  count1 = partitionMediumElement(arr[0:i - 1]) 
  count2 = partitionMediumElement(arr[i:r]) 

  return comparisons + count1 + count2

# print(firstTen)
# print(partitionMediumElement(firstTen))