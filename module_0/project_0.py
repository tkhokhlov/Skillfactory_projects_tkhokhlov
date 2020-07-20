#!/usr/bin/env python
# coding: utf-8

# # Итоговое задание. Проект 0
# 
# Написать прогрумму, которая угадывает загаданное компьютером натуральное число от 1 до 100 за минимальное количество попыток

# In[ ]:


import numpy as np


def guess_number_game(number):
    '''Функция принимает на вход натуральное число от 1 до 100 и выдает результат, за сколько попыток было угадано число.
       Поиск числа начинается с середины всего интеравала от 1 о 100 (с числа 50).
       Если искомое число меньше среднего в интервале, то берется левая часть интервала и повторяется операция поиска.
       В противном случае - берется правая часть интервала и повторяется операция поиска.'''
    count = 1
    predict_number = 50  #переменная, в которой хранится предполагаемое загаданное число
    top_range = 100      #верхняя граница интервала
    bottom_range = 1     #нижняя граница интервала
    
    while predict_number != number:
        count += 1
        if number < predict_number:
            top_range = predict_number - 1
            predict_number = top_range - int((top_range - bottom_range)//2)
        else:
            bottom_range = predict_number + 1
            predict_number = bottom_range + int((top_range - bottom_range)//2)
    
    return count


def score_game(game):
    '''Функция принимает на вход функицю, в которой реализован механизм поиска загаданного числа, запускает игру 1000 раз, 
       и выводит информацию о том, как быстро, в среднем, переданная на вход функция угадывает число'''
    random_numbers = np.random.randint(1, 101, size=(1000)) #собираем список из 1000 случайных натуральных чисел от 1 до 100
    
    count_list = []
    for number in random_numbers: #запускаем функцию поиска загаданного числа и записываем результат каждого запуска в список
        count_list.append(game(number))
    
    score_mean = int(np.mean(count_list))
    
    return(print("В среднем, алгоритм угадывает число за {} попыток.".format(score_mean)))


comp_number = np.random.randint(1,101)       #компьютер загадывает число
count_score = guess_number_game(comp_number) #вызываем функцию, чтобы узнать, с какой попытки наш алгоритм угадает число

print('Загаданное компьютером число {} алгоритм угадал с {} попытки.\n'.format(comp_number, count_score))
score_game(guess_number_game)


# In[ ]:




