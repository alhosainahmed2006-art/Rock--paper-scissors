# start the game
# Ask the user to make a move (r , p , s)
# pc would select a move randomaly
# pc == player -> Tie 
# (player == p and pc == Rock) or (player == R and pc == scissors) or (player ==scissors and pc ==paper)
## user won / you won

# Any other case 
## pc won / you lose 

import random

user = input ("What's your chooice ?'r' for rock , 'p' for pepar , and 's' for scissors : ")
pc = random.choice(['r' , 'p' , 's'])

print("user played : " + user)
print("pc played : " + pc)


if user == pc:
    print('Its a tie')
    
elif (user == 'p' and pc =='r') or (user == 'r' and pc == 's') or (user =='s' and pc =='p'):
    print('you won !')
    
else:
    print('you lose !')
    
    
    
 
    