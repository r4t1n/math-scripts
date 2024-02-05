#!/usr/bin/env python3

import math

def get_user_input():
    identifier_1 = input("> Enter the first identifier: ")
    value_1 = float(input("> Enter the first value: ")) 
    identifier_2 = input("> Enter the second identifier: ")
    value_2 = float(input("> Enter the second value: "))

    calculate_scenario(identifier_1, value_1, identifier_2, value_2)

def calculate_scenario(identifier_1, value_1, identifier_2, value_2): # There are only 9 possible scenarios in a right-angled triangle with two inputs
    if identifier_1 in ["a", "b"] and identifier_2 in ["b", "c"]: # First three scenarios (both identifiers are side lengths)
        if identifier_1 == "a":
            if identifier_2 == "b":
                calculate_a_and_b(value_1, value_2)
            if identifier_2 == "c":
                calculate_a_and_c(value_1, value_2)

        if identifier_1 == "b" and identifier_2 == "c":
            calculate_b_and_c(value_1, value_2)

    elif identifier_1 in ["a", "b", "c"] and identifier_2 in ["A", "B"]: # Last six scenarios (one side length and one angle)
        if identifier_1 == "a":
            if identifier_2 == "A":
                calculate_a_and_A(value_1, value_2)
            if identifier_2 == "B":
                calculate_a_and_B(value_1, value_2)

        if identifier_1 == "b":
            if identifier_2 == "A":
                calculate_b_and_A(value_1, value_2)
            if identifier_2 == "B":
                calculate_b_and_B(value_1, value_2)

        if identifier_1 == "c":
            if identifier_2 == "A":
                calculate_c_and_A(value_1, value_2)
            if identifier_2 == "B":
                calculate_c_and_B(value_1, value_2)
        
    else:
        print("The identifiers are either not valid or not in correct order, check the README.md")

def calculate_a_and_b(value_1, value_2):
    a = value_1
    b = value_2
    c = math.sqrt(a**2 + b**2)

    A = math.degrees(math.atan(b / a))
    B = 90 - A

    print_values(a, b, c, A, B)

def calculate_a_and_c(value_1, value_2):
    a = value_1
    c = value_2
    b = math.sqrt(c**2 - a**2)

    A = math.degrees(math.acos(a / c))
    B = 90 - A

    print_values(a, b, c, A, B)

def calculate_b_and_c(value_1, value_2):
    b = value_1
    c = value_2
    a = math.sqrt(c**2 - b**2)

    A = math.degrees(math.acos(a / c))
    B = 90 - A

    print_values(a, b, c, A, B)

def calculate_a_and_A(value_1, value_2):
    A = value_2
    B = 90 - A

    a = value_1
    b = a * math.tan(math.radians(A))
    c = math.sqrt(a**2 + b**2)

    print_values(a, b, c, A, B)

def calculate_a_and_B(value_1, value_2):
    B = value_2
    A = 90 - B

    a = value_1
    b = a * math.tan(math.radians(A))
    c = math.sqrt(a**2 + b**2)

    print_values(a, b, c, A, B)

def calculate_b_and_A(value_1, value_2):
    A = value_2
    B = 90 - A

    b = value_1
    a = b / math.tan(math.radians(B))
    c = math.sqrt(a**2 + b**2)

    print_values(a, b, c, A, B)

def calculate_b_and_B(value_1, value_2):
    B = value_2
    A = 90 - B

    b = value_1
    a = b / math.tan(math.radians(B))
    c = math.sqrt(a**2 + b**2)

    print_values(a, b, c, A, B)

def calculate_c_and_A(value_1, value_2):
    A = value_2
    B = 90 - A

    c = value_1
    a = c * math.sin(math.radians(A))
    b = math.sqrt(c**2 - a**2)

    print_values(a, b, c, A, B)

def calculate_c_and_B(value_1, value_2):
    B = value_2
    A = 90 - B

    c = value_1
    a = c * math.sin(math.radians(A))
    b = math.sqrt(c**2 - a**2)

    print_values(a, b, c, A, B)

def print_values(a, b, c, A, B):
    print(f"\n  a: {a:.2f}")
    print(f"  b: {b:.2f}")
    print(f"  c: {c:.2f}")
    print(f"  A: {A:.2f}")
    print(f"  B: {B:.2f}")
    print("  C: 90")

if __name__ == "__main__":
    get_user_input()
