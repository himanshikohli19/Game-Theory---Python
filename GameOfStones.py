'''
GAME OF STONES:

Two players called P1 and P2 are playing a game with a starting number of stones.
Player 1 always plays first, and the two players move in alternating turns.

The gamE's rules are as follows:

In a single move, a player can remove either 2, 3, or 5 stones from the game board.
If a player is unable to make a move, that player loses the game.
Given the starting number of stones, find and print the name of the winner.
P1 is named First and P2 is named Second. Each player plays optimally,
meaning they will not make a move that causes them to lose the game if a winning move exists.
'''

import math
import os
import random
import re
import sys

def gameOfStones(n):
    # Write your code here
    for i in range(n):
        if n%7==0 or n%7==1:
            return "Second"
        else:
            return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
