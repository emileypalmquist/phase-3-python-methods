#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


def add(num1, num2):
    return num1 + num2


def halve(number):
    if int(number) != number:
        return None
    else:
        return number / 2
