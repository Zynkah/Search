def seq_search(number_list, n):
    # searches if the number is in the list
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


numbers = range(0, 100)
s1 = seq_search(numbers, 2)
print(s1) # True
s2 = seq_search(numbers, 202)
print(s2) # False
