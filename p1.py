# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Truong Hoang Tuan Kiet (s3926873)
# Created date: 12/11/2021 8:03
# Last modified date: 28/11/2021 23:34

import random

def main():
    integer_list = create_random_list(20)
    #Print the list with random numbers
    print(integer_list)
    #Print the solution: the 16th number after sorted
    print("the number that satisfies the requirements:", find_split_80(integer_list))


def create_random_list(n):
    """
    This function created to generate a random list
    :param list: list consists of 20 random numbers
    :param n: length of the list
    :return: a random list with 20 numbers
    """
    #Create an empty list to store the random numbers
    integer_list = []

    #Using a for loop to generate the random numbers 20 times
    for numbers in range(n):
        numbers = random.randint(0, 100)
        #Add the numbers to the empty list
        integer_list.append(numbers)
    return integer_list

def find_split_80(integer_list):
    """
    This function created to find and return the numbers that satisfies the condition
    Solving idea: sort the input of the list to find the 16th number in the list
    :param integer_list: the integer list of 20 random numbers
    :return: the 16th value of the integer list after sorting process
    """

    #Sort the integer list to find the numbers
    integer_list.sort()
    split_80 = integer_list[16]

    #return the desire number
    return split_80
main()