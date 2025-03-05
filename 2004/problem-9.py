import math

a = 0

for i in range(1, 201):
    if math.gcd(i, 15) == 1 or math.gcd(i, 24) == 1:
        print(i)
        a += 1

print("Answer: " + str(a))

