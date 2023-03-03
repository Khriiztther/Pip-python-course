import random

options = ('Piedra', 'Papel', 'Tijera')

pc_option = random.choice(options)

def run():
    user_option = input('Piedra, Papel o Tijera, YA!: ')
    user_option = user_option.lower()
    user_option = user_option.capitalize()
    user_option = user_option.strip()


    if user_option == pc_option:
        print('Empate!')
    elif user_option == 'Piedra':
        if pc_option == 'Tijera':
            print('Ganaste!!!')
        else:
            print('Perdiste!!!')
    elif user_option == 'Papel':
        if pc_option == 'Piedra':
            print('Ganaste!!!')
        else:
            print('Perdiste!!!')
    elif user_option == 'Tijera':
        if pc_option == 'Papel':
            print('Ganaste!!!')
        else:
            print('Perdiste!!!')

    


if __name__ == '__main__':
    run()
