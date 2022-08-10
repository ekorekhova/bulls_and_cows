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
    if int(user_digit_list[0]) == int(computer_digit_list[0]):
        check_result['bulls'] += 1
        check_result['cows'] += 0
    elif (user_digit_list[0]) in computer_digit_list:
        check_result['bulls'] += 0
        check_result['cows'] += 1
    else:
        check_result['bulls'] += 0
        check_result['cows'] += 0
    if int(user_digit_list[1]) == int(computer_digit_list[1]):
        check_result['bulls'] += 1
        check_result['cows'] += 0
    elif (user_digit_list[1]) in computer_digit_list:
        check_result['bulls'] += 0
        check_result['cows'] += 1
    else:
        check_result['bulls'] += 0
        check_result['cows'] += 0
    if int(user_digit_list[2]) == int(computer_digit_list[2]):
        check_result['bulls'] += 1
        check_result['cows'] += 0
    elif (user_digit_list[2]) in computer_digit_list:
        check_result['bulls'] += 0
        check_result['cows'] += 1
    else:
        check_result['bulls'] += 0
        check_result['cows'] += 0
    if int(user_digit_list[3]) == int(computer_digit_list[3]):
        check_result['bulls'] += 1
        check_result['cows'] += 0
    elif (user_digit_list[3]) in computer_digit_list:
        check_result['bulls'] += 0
        check_result['cows'] += 1
    else:
        check_result['bulls'] += 0
        check_result['cows'] += 0
    print(check_result)


def is_gameover():
    return check_result['bulls'] == 4
