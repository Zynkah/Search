def binarySearch(alist, item):
    '''
    - start search from the middle of the list - divide and conquer
    - if item is what we are looking for - success
    - if the item we are searching for is greater than the middle item we search the lower half of the list and eliminate the other half of the list
    - if the item we are searching for is lower than the middle item we search the higher half of the list and eliminate the other half of the list
    - repeat the process till item is found or just one item remains, this then will return a boolean
    - recursive call to the binary search 
    '''
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3)) # False
print(binarySearch(testlist, 13)) # True