import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f"Please input a number between 1 and {x} or type exit to leave: ")
        if guess == 'Exit' or guess == 'exit':
            print("You Suck!!")
            exit()

        guess = int(guess)

        if guess < random_number:
            print('Higher')
        elif guess> random_number:
            print('Lower')
        elif guess == random_number:
            print("Congrats You Got it!!!")


decision = input("select the level of difficulty or cancel: Easy(1-50), Normal(1-100), Hard(1-200), or Cancel: ")
if decision == 'Cancel' or decision == 'cancel':
    print("Canceling")
    exit()
elif decision == 'Easy' or decision == 'easy':
    guess(random.randint(1,50))
elif decision == 'Normal' or decision == 'normal':
    guess(random.randint(1,100))
elif decision == 'Hard' or decision == 'hard':
    guess(random.randint(1,200))
else:
    print('Error: Incorrect input')