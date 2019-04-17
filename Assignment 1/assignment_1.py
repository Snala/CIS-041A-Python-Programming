"""
CIS 41A - Assignment 1
Name: David Rios
Date: 4-9-19
"""

# Exercise 3.2


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_two_times(function, variable):
    function(variable)
    function(variable)


do_two_times(print_twice, 'spam')


def do_four_times(function, variable):
    do_two_times(function, variable)
    do_two_times(function, variable)


do_four_times(print_twice, 'spam')


# Exercise 3.3

def do_twice(function):
    function()
    function()


def do_tall_wall(function):
    for i in range(0, 4):
        do_twice(function)
        print('|')


def print_pipe():
    print('|        ', end=' ')


def print_meeting():
    print('+ - - - -', end=' ')


def print_level():
    do_twice(print_meeting)
    print('+')


def print_cubby():
    print_level()
    do_tall_wall(print_pipe)


def print_grid():
    do_twice(print_cubby)
    print_level()


print_grid()