import random

number=random.randint(1,9)

chances=0

while chances<5:
    usr=int(input("Enter Your Guess: "))
    if(number==usr):
        print("Congrats! You won!")
    elif(number>usr):
        print("Your guess was too low, come up")
    else:
        print("Your guess was too high, come down")

    chances += 1
