lts = []
n = int(input("Enter the total number of element :"))
for i in range(n):
    num = int(input(f"enter the value :"))
    lts.append(num)

average = sum(lts) / n 
print(f"the average of given list is {average}")
