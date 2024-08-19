import random

def computer_guess(y):
    lowest = 1 
    highest = y
    humanfeedback = ''
    try:
        while humanfeedback != 'c':
            if lowest != highest: 
                guess = random.randint(lowest, highest)
            else:
                guess = lowest #it could be one of them lowest or highest 
            humanfeedback = input(f'is {guess} too high (l) or too Low (l) or Correct (c): ')
            if humanfeedback == 'h':
                highest = guess - 1
            elif humanfeedback == 'l':
                lowest = guess + 1
        
        print(f'I guessed your number {guess} correctly. cap of binary for me :)')
    except:
         print('oops some error accured ')


computer_guess(100)
