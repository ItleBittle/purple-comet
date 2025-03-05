import math

a = 0
tenFac = math.factorial(10)

for i in range(1, tenFac + 1):
    if tenFac % i == 0:
        print(i)
        a += 1

print("Answer: " + str(a))