written = ""

for i in range(1, 100):
    for _ in range(1, i + 1):
        written += str(i)

print("Answer: " + written[2004])
