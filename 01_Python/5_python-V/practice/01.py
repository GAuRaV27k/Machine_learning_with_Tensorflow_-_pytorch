with open("names.txt","w") as file:
    temp = input("Enter names separated by commas: ")
    file.writelines(temp)
    file.seek(0)