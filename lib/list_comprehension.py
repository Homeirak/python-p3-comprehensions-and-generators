#!/usr/bin/env python3

#List comprehensions automatically create and populate a new list → No need for .append()
num_list = []
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [f"{sentence}!" for sentence in sentence_list]

#additional practice -
# squared_minus_one = list()

# for n in range(1, 11):
#     squared_minus_one.append((n ** 2) -1)

# print(squared_minus_one)

#a list comprehension allows us to instantiate a list object and perform a for loop to populate its values in a single line.
# squared_minus_one = [(n **2) -1 for n in range(1, 11)]

# print(squared_minus_one)

# syntax of a list comprehension:
# new_list = [optional_operation(item) for item in old_list if optional_condition == True]

