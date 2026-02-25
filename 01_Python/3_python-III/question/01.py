# we will check the string the palindrome or not 

s = input("Give the string to check :")

n = len(s)
left = 0 
right = n-1
answer = True
while left <= right:
    if s[left] != s[right]:
        answer = False
        break
    left += 1
    right -= 1

if answer:
    print(f"the string '{s}' is palindrome")
else:
    print(f"the string '{s}' is not palindrome")