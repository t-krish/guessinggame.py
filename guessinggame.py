import random
gno=random.randint(1, 100)
guessed = False
while guessed == False:
    guess = input('What number do you think it is?: ')
    guess = int(guess)
    if guess > gno:
        print('Try a little lower')
    if guess < gno:
        print('Try a little higher')
    if guess == gno:
        print('CORRECT!!!')
        guessed = True
