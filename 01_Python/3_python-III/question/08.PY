'''
Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]


1 2  2 3 
7 5 6 6 

'''

lst1 = [1, 2, 3]
lst2 = [3, 4]

total = len(set(lst1)) + len(set(lst2))
answer = set(lst1).union(set(lst2))

print(len(answer))
print(total)
if (len(answer) < total):
    print("share the common elements")
else:
    print("share the no  common elements")
