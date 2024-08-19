import random

def guessNumber(x):
    randon_number = random.randint(1, x)
    guess = 0
    try:
        while guess != randon_number:
            guess = int(input(f'Enter a number between 1 to {x}: '))
            if guess > randon_number:
                print('Sorry, guess again. Too High')
            elif guess < randon_number:
                 print('Sorry, guess again, Too Low')
        print(f'Wow Congrats. you have guessed the number I have in mind {randon_number} correctly. You are Genius')
    except:
        print('Error is being accured')



guessNumber(50)


    
