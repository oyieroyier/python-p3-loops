#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print('Happy New Year!')


def square_integers(int_list):
    return [number ** 2 for number in int_list]


def fizzbuzz():
    for number in range(1, 101):
        if not number % 15:
            print("FizzBuzz")
        elif not number % 5:
            print("Buzz")
        elif not number % 3:
            print("Fizz")
        else:
            print(number)