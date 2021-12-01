# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Truong Hoang Tuan Kiet (s3926873)
# Created date: 13/11/2021 11:10
# Last modified date: 28/11/2021 23:34

import math
import random

def main():
    print("The estimate Pi result is:",estimate_pi(1000))

def generate_n_random_points(n):
    """
    This function created to generate an empty list to store the n random points over the circle
    :param n: the total amount of random points
    :return: list consist of n random points
    """
    list_of_n_random_points = []
    for i in range(n):
        #Random the x-coordinate and y-coordinate of the points
        x = random.uniform(-1, 1)
        y = random.uniform(-1 ,1)
        #generates a random points with [x,y] to store in the list
        random_points = [x, y]
        #Add the random points to the list
        list_of_n_random_points.append(random_points)
    return list_of_n_random_points

def check_the_distance_of_the_random_point(points):
    """
    This function created to check the distance of the points with the circle
    If the distance > 1 -> The points is outside the circle
    Else the distance <= 1 -> The points is in the circle or inside the circle
    :param points :
    :return: if the points inside the circle -> return True / else return False (boolean)
    """
    #Calculate the distance of the points with the circle by the provided formula
    distance = math.sqrt(points[0]**2 + points[1]**2)
    if distance > 1:
        return False
    else:
        return True

def count_the_total_points_inside_the_circle(list_of_n_random_points):
    """
    This function created to count the total of points that lays inside a circle
    :param list_of_n_random_points:
    :return:the total amount of points inside the circle (integer)
    """
    #Create a count variable to count the random points inside the circle
    cnt = 0
    for points in list_of_n_random_points:
        if check_the_distance_of_the_random_point(points):
            cnt += 1
    return cnt
def estimate_pi(N):
    """
    This function created to calculate approximate pi of a circle with n random points
    :param N: random points generated over the circle
    :return: estimate pi (float)
    """
    list_of_n_random_points = generate_n_random_points(N)
    total_points_inside_the_circle = count_the_total_points_inside_the_circle(list_of_n_random_points)
    estimate_pi = ( total_points_inside_the_circle * 4 ) / N
    return estimate_pi
main()