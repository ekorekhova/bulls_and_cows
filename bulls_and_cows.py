# -*- coding: utf-8 -*-

from bulls_and_cows_engine import randomizer, user_number_check, is_gameover
from termcolor import cprint, colored


def game():
    randomizer()
    cprint('A number is chosen', color='grey', on_color='on_green')
    i = 0
    while True:
        user_guess = input(colored('Enter your guess between 1000 and 9999: ', color='yellow'))
        try:
            if 999 < int(user_guess) < 10000:
                number_check = user_number_check(user_number=int(user_guess))
                i += 1
            else:
                cprint('Incorrect! Try again', color='red')
                continue
        except ValueError:
            cprint('Incorrect! Try again', color='red')
            continue
        if is_gameover():
            print('Congratulations! You guessed the number in ', i, ' attempts')
            user_decision = input(colored('If you want to play again enter +', color='yellow'))
            if user_decision == '+':
                game()
            else:
                cprint('Farewell, my friend! Farewell...', color='grey', on_color='on_blue')
            break


game()
