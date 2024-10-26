import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and feedback != 'C':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), Is it too low (L), or is it Correct (c)')
        if feedback == 'H' or feedback == 'h':
            guess -= 1
        elif feedback == 'L' or feedback == 'l':
            guess += 1

    print(f'Your guess {guess} was correct')



decision = input("select the level of difficulty or cancel: Easy(1-50), Normal(1-100), Hard(1-200), or Cancel: ")
if decision == 'Cancel' or decision == 'cancel':
    print("Canceling")
    exit()
elif decision == 'Easy' or decision == 'easy':
    computer_guess(random.randint(1,50))
elif decision == 'Normal' or decision == 'normal':
    computer_guess(random.randint(1,100))
elif decision == 'Hard' or decision == 'hard':
    computer_guess(random.randint(1,200))
else:
    print('Error: Incorrect input')