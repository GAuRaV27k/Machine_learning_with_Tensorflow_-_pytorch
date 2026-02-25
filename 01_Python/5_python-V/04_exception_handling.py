try: 
    x  =int(input("Enter a number: "))
    y = 10 / x
    print(f"10 divided by {x} is {y}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")