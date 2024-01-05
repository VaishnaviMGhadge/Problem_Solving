import random
number=random.randint(1,5)
user_input=int(input('enter the number'))
while True:
    if(user_input==number):
        print("yes the guess is right")
        break
    else:
        user_input=int(input('enter the number'))

