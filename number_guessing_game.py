import random 

random_number = int(random.randint(1, 100))

while True:
    number = input("pick a number> ")
    try:
        if int(number) > random_number:
            print("Too high!")
        elif int(number) < random_number:
            print("Too low!")
        else:
            print("Congradulations")
            break
    except:
        print("Invalid!")