def inversionCount(x):
    count = 0
    if len(x) > 1:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]

        count += inversionCount(left)
        count += inversionCount(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                x[k] = left[i]
                i += 1
            else:
                count += len(left[i:])
                x[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    return count

def fileInversionCount():
    finalArray = []
    filename = 'w2.txt'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for integer in lines:
        finalArray.append(int(integer))
    return inversionCount(finalArray)

print(fileInversionCount())