even1 = []
odd2 = []
n = int(input("enter the lenght of tuple :"))
for i in range(n):
    num = int(input("enter the item of tuple :"))
    if (num%2 == 0):
        even1.append(num)
    else:
        odd2.append(num)


tup1 = tuple(even1)
tup2 = tuple(odd2)

print(tup1)
print(tup2)