#!/usr/bin/env python3

def happy_new_year():
    counter = 11
    while counter > 1:
        counter-=1
        print(counter)
        if counter == 1:
            print("Happy New Year!")

def square_integers(int_list):
    squared_list = [number * number for number in int_list]
    return squared_list
    

def fizzbuzz():
    for i in range(1 , 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
