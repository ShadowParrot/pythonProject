#modifying the print() function
with open("tmp.txt", "w") as tmp:
    print("Hello", "World", end="End", sep="-", file=tmp)
