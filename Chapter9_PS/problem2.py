'''The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file 'Hi-score.txt' which is either blank or contains the
previous Hi-score. You need to write a program to update the Hi-score whenever the
game() function breaks the Hi-score.'''

import random


def game() :
    print("You are playing the game....")
    scroe = random.randint(1, 99)
    # fetch the highScore
    with open("/workspaces/python/Chapter9_PS/2_highscore.txt") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your score : {scroe}")
    if scroe > highscore :
        # write this highscore to the file
        with open("/workspaces/python/Chapter9_PS/2_highscore.txt","w") as f:
            f.write(str(scroe))
    return scroe

game()