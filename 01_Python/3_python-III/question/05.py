'''
Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
depending on the operation they want to perform on the dictionary:
1. A - Add a student
2. B - Update marks
3. C - Search for a student
4. D - Display all students and marks    
    
    
'''


dit = {
    "Gaurav" :17, 
    "Vikas" : 18,
    "Atul" :20,
}

print("-| WELCOME TO THE DICTIONARY MENU |-")

print("A - Add a student")
print("B - Update marks")
print("C - Search for a student")
print("D - Display all students and marks")

user = input("Enter the input :")
if user == 'A' :
    name = input("Enter the name :")
    marks = int(input("Enter the marks :"))
    dit[name] = marks
    print(dit)

elif user =='B':
    updates = input("Which value you want to update the key :")
    value = input("Enter the updated value :")
    dit[updates] = value
    print(dit)

elif user == 'C':
    name = input("Enter the name for search :")
    if name in dit:
        print(f"The {name} is present in dict")
        print(dit)
    else:
        print(f"The {name} is not present in dict")
        print(dit)
elif user =='D':
    dit.items()
    print(dit)

else:
    print("ERROR")


