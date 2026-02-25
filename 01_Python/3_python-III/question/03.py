
lts1 = []
lts2 = []
n = int(input("Enter the lenght of list :"))
for i in range(n):
    n1 = int(input("Write the value of the first list :"))
    lts1.append(n1)
    n2 = int(input("Write the value of the second list :"))
    lts2.append(n2)

answer = list(set(lts1).union(set(lts2)))
answer.sort()
print(answer)

    

    
    
    
