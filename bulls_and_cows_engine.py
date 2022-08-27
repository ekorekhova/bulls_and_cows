# -*- coding: utf-8 -*-

from random import randint


def randomizer():
    global computer_number
    global computer_digit_list
    computer_number = randint(1000, 10000)
    computer_digit_list = str(computer_number)


def user_number_check(user_number):
    global check_result
    check_result = {'bulls': 0, 'cows': 0}
    user_digit_list = str(user_number)
    x = 0
    for _ in user_digit_list:
        if int(user_digit_list[x]) == int(computer_digit_list[x]):
            check_result['bulls'] += 1
            check_result['cows'] += 0
        elif (user_digit_list[x]) in computer_digit_list:
            check_result['bulls'] += 0
            check_result['cows'] += 1
        else:
            check_result['bulls'] += 0
            check_result['cows'] += 0
        x += 1
    print(check_result)


def is_gameover():
    return check_result['bulls'] == 4
