import random

options = ('Rock', 'Paper', 'Sissors')



def rungame():
    user_points = 0
    pc_points = 0
    rounds = 1

    while True:
        print ('*' * 20)
        print('Round '+ str(rounds))
        print('*' * 20)

        if user_points == 2:
            print('You: ' + str(user_points))
            print('Pc: ' + str(pc_points))
            print('Player wins!!!!!')
            

