import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'
print(choose_first())
