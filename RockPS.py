import random
def play():
    user = input("Please Input your choice'r' for rock, 'p' for paper, and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print ('tie')
    
    if win(user, computer):
        print("YOU WIN!")
    elif win(computer, user):
        print("YOU LOSE!")

    another = input("Would you like to play again, type (y)es or (n)o: ")
    if another == 'y':
        print(play())
    else:
        print("GoodBye!")
        exit()



    
def win(player, opponent):
    if player == 'r' and opponent == 's':
        return True
    elif player == 's' and opponent == 'p':
        return True
    elif player == 'p' and opponent == 'r':
        return True
    
play()