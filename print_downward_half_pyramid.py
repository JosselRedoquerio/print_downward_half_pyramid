# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

print("\n")
for x in range(9, 0, -1):
    for y in range(0, x - 1):
        print("*", end= " ")
    print(" ")        