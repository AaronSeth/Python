from random import randint


name=str(input("Hello what is your name?"))
print("Hello", name)
num=randint(1,10)
guess=int(input("I have a number in my head between 1 and 10, Can you guess it?"))

while(num!=guess):
    if guess > num:
        print("Oops! that's too high! try again")
        guess=int(input("I have a number in my head between 1 and 10, Can you guess it?"))
    elif guess < num:
        print("Whoa! Your Guess is too low")
        guess=int(input("I have a number in my head between 1 and 10, Can you guess it?"))
    if guess==num:
        print("Nicely Done! You got it right!")
        break

              





