target = 66

while True:
    value = input("Enter an integer between 1 and 100: ")
    try:
        value = int(value)
    except ValueError:
        print("I said enter an integer!")
        break
    if value > target:
        print(value, "is too high")
    elif int(value) < target:
        print("too low")
    else:
        print("Perfect!\n now closing Game")
        break
