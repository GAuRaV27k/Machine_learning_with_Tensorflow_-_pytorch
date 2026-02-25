# Given a list, print all elements that appear more than once in the list.

lst = [1,22,523,36,2,4]

check = []

for item in lst:
    if item in check:
        print(item,end= " ")
    else:
        check.append(item)

        
            