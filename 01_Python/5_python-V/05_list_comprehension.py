nums = [x for x in range(10)]
print(nums)

sq = [i*i for i in range(10)]
print(sq)

sq_even = [i*i for i in range(10) if i%2==0]
print(sq_even)

name = ["python", "java", "c++", "c#", "javascript"]
name = [n.upper()for n in name]
print(name)

number = [-1,-4,-5,1, 2, 3, 4, 5]
number = [0 if number<0 else number for number in number]

print(number)