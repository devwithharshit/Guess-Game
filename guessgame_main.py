from random import randint

print("Welcome to Guess Game!")
print()
rn = randint(1,100)
ugn = -1
guess = 1


while(ugn != rn):
    ugn = int(input("Guess any Number b/w 1 & 100: "))
    print()
    if ugn > rn:
        print("Lower the Guess Please!")
        print()
        guess += 1
    elif ugn < rn:
        print("Increase the Guess Please!")
        print()
        guess += 1

print(f"Congoo! You have Guessed the Number {ugn} Correctly in {guess} Attempts!")

