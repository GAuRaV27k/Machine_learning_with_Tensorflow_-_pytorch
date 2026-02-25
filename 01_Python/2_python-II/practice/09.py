def is_prime(n):
    answer = True
    if n <2:
        answer = False
    else:
        for i in range(2,n-1):
                answer = False if n%i == 0 else True
    print(answer)            


is_prime(1)    