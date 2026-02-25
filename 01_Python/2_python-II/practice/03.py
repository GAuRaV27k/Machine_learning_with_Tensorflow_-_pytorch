def digi(n):
    while n > 0:
        print(n % 10, end=" , ")
        n //= 10

digi(98789)
