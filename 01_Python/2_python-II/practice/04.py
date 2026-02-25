def count(n):
    coute = 0
    while n > 0:
        N = n%10
        coute +=1
        n //= 10

    return coute

print(count(12345))

