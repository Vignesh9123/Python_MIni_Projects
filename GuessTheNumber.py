import random                #importing 'random' module
#tdujtjksrxg
secret_number = random.randint(1 , 19)
print("I am thinking a number between 1 and 19")

# Ask the player to guess the number

for guess_taken in range(1, 6):    # 5 guesses are allowed
    print("Take a guess.")
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        break         # correct guess condition

if guess == secret_number:
    print('Your guess is correct. You took ' + str(guess_taken) + ' chances')
else:
    print("Nope you couldn't guess the number . The number i thought was " + str(secret_number))
