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

        user_selection = input('Rock, Paper, Sissors, Go!: ')
        user_selection = user_selection.lower()
        user_selection = user_selection.strip()
        user_selection = user_selection.capitalize()

        pc_selection = random.choice(options)

        if not user_selection in options:
            print('Esa no es una opcion')
            print(user_selection)
            continue

        if user_selection == pc_selection:
            rounds += 1
            print(pc_selection + ', Empate!!')
            print('Jugador: ' + str(user_points))
            print('Computador: ' + str(pc_points))
        else:
            while pc_selection == 'Piedra':
                if user_selection == 'Papel':
                    rounds += 1
                    print(pc_selection + ', Ganaste!!!')
                    user_points += 1
                else:
                    rounds += 1
                    print(pc_selection + ', Perdiste!!!')
                    pc_points += 1
                    print('Jugador: ' + str(user_points))
                    print('Computador: ' + str(pc_points))
                    break
            while pc_selection == 'Papel':
                if user_selection == 'Tijera':
                    rounds += 1
                    print(pc_selection + ', Ganaste!!!')
                    user_points += 1
                else:
                    rounds += 1
                    print(pc_selection + ', Perdiste!!!')
                    pc_points += 1
                    print('Jugador: ' + str(user_points))
                    print('Computador: ' + str(pc_points))
                    break
            while pc_selection == 'Tijera':
                if user_selection == 'Piedra':
                    rounds += 1
                    print(pc_selection + ', Ganaste!!!')
                    user_points += 1
                else:
                    rounds += 1
                    print(pc_selection + ', Perdiste!!!')
                    pc_points += 1
                    print('Jugador: ' + str(user_points))
                    print('Computador: ' + str(pc_points))
                    break

        if user_points == 2:
            print('You: ' + str(user_points))
            print('Pc: ' + str(pc_points))
            print('Player wins!!!!!')
            break
        if pc_points == 2:
            print('You: ' + str(user_points))
            print('Pc: ' + str(pc_points))
            print('Computer wins!!!!!')
            break
if __name__ == '__main__':
    rungame()


