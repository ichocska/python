import random
numbers = []

for i in range(5):
    numbers.append(random.randint(0, 100))
    sum = 0
    for x in str(numbers[i]):
        sum += int(x)
    if sum % 2 == 0:
        print(numbers[i])

print(numbers)



