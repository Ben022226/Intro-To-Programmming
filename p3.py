# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Truong Hoang Tuan Kiet (s3926873)
# Created date: 14/11/2021 15:05
# Last modified date: 28/11/2021 23:34

import math

def main():
    total_flour_in_kg, decision, total_cost = flour_order(100,50,100,50)
    print("The total amount of flour:", total_flour_in_kg,"Kg")
    print("Selected provider:", decision)
    print("The total cost is:", int(total_cost), "VND")

def flour_order(large_thick, large_thin, medium_thick, medium_thin):
    """
    This function created to print the flour order including total flour, selected provider and total cost
    :param large_thick: the numbers of large thick pizzas
    :param large_thin: the numbers of large thin pizzas
    :param medium_thick: the numbers of medium thick pizzas
    :param medium_thin: the numbers of medium thin pizzas
    :return: total_flour ( integer ), selected_provider ( string ), total_cost ( integer )
    """
    total_flour = final_amount_of_flour_in_kg(large_thick, large_thin, medium_thick, medium_thin)

    provider_a_selling_cost = total_money_purchasing_from_a_provider(total_flour)

    provider_b_selling_cost = total_money_purchasing_from_b_provider(total_flour)

    selected_provider, total_cost = decision_between_two_providers(provider_a_selling_cost, provider_b_selling_cost)

    #Print out the flour order based on the requirement
    print("We need to order", int(total_flour),"kg of flour, which costs", int(provider_a_selling_cost), "VND if we buy from A and", int(provider_b_selling_cost),"VND if we buy from B.")

    return total_flour, selected_provider, total_cost

def final_amount_of_flour_in_kg(large_thick_pizzas_number, large_thin_pizzas_number, medium_thick_pizzas_number, medium_thin_pizzas_number):
    """
    This function created to calculate and convert from grams to kilograms then print out the final amount of flour in kilograms
    :param large_thick_pizzas_number - numbers of large thick pizzas
    :param large_thin_pizzas_number - numbers of large thin pizzas
    :param medium_thick_pizzas_number - numbers of medium thick pizzas
    :param medium_thin_pizzas_number - numbers of medium thin pizzas
    :return: total_flour_in_kg ( integer )
    """
    #Calculate the total of flour need to utilize and convert to kilograms by dividing for 1000
    total_flour_in_kg = (large_thick_pizzas_number * 550 + large_thin_pizzas_number * 500 + medium_thick_pizzas_number * 450 + medium_thin_pizzas_number * 400) / 1000

    #Given that 6% of the flour will be wasted during pizza making process
    #So we need to enumerate the total amount of flour with the waste
    total_flour_with_the_waste_in_kg = total_flour_in_kg + total_flour_in_kg * 0.06

    #Given that both providers deliver in bags of 2kg, so the order must be divisible by 2
    #So we need to round up the total amount of flour with the waste to an even number by creating a function to round up the number
    actual_amount_of_flour_in_kg = round_up_to_even_number(total_flour_with_the_waste_in_kg)
    return actual_amount_of_flour_in_kg

def round_up_to_even_number(final_flour_order):
    """
    This function created to round up the final amount of flour to even number for separating in bags of 2kg
    :param final_flour_order: the final amount of flour
    :return: final_flour_order (integer)
    """
    #I need to use a math function to round up which is math.ceil()
    #How this function works: rounds a number up to the nearest integer
    #Example: math.ceil(1.3) -> 2, math.ceil(-5.7) -> -5
    #In this case, i will modulus the number by 2 to check if it satisfies the condition
    #If the number is smaller than 1, i will add 1 to the number to round up to 2kg
    if final_flour_order % 2 < 1:
        flour_exact = math.ceil(final_flour_order + 1)
    else:
        flour_exact = math.ceil(final_flour_order)
    return flour_exact

def total_money_purchasing_from_a_provider(actual_amount_of_flour_in_kg):
    """
    This function created to return total money of provider A's selling price if I decided to buy from A
    :param actual_amount_of_flour_in_kg:  total amount of flour
    :return: provider_a_selling_cost (integer)
    """
    #Known that 1kg of flour costs 30.000VND from provider A
    provider_a_selling_price = actual_amount_of_flour_in_kg * 30000

    #For the discount, given that provider A gives a discount of 3% for orders of less than 30kg and 5% for orders of at least 30kg
    #So if the actual amount is smaller than 30kg, gain 3% discount, else will gain 5% discount
    if actual_amount_of_flour_in_kg < 30:
        provider_a_selling_price -= (provider_a_selling_price * 0.03)
    else:
        provider_a_selling_price -= (provider_a_selling_price * 0.05)
    return provider_a_selling_price

def total_money_purchasing_from_b_provider(actual_amount_of_flour_in_kg):
    """
    This function created to return total money of provider B's selling price if I decided to buy from B
    :param actual_amount_of_flour_in_kg: total amount of flour
    :return: provider_b_selling_price (integer)
    """
    #Known that 1kg of flour costs 31.000VND from provider B
    provider_b_selling_price = actual_amount_of_flour_in_kg * 31000

    #For the discount, provider B gives a discount of 5% for orders of less than 40kg and 10% for orders of at least 40kg
    # So if the actual amount is smaller than 40kg, gain 5% discount, else will gain 10% discount
    if actual_amount_of_flour_in_kg < 40:
        provider_b_selling_price -= (provider_b_selling_price * 0.05)
    else:
        provider_b_selling_price -= (provider_b_selling_price * 0.1)
    return provider_b_selling_price

def decision_between_two_providers(provider_a_selling_cost, provider_b_selling_cost):
    """
    This function created to decide which provider I will buy flour from
    :param provider_a_selling_cost: total money of a provider
    :param provider_b_selling_cost: total money of b provider
    :return: the provider i decided to buy (string), provider selling cost (integer)
    """
    #I will use an if condition to check the prices between 2 providers
    #If provider A's price is cheaper than provider B -> I will buy from provider A
    #Otherwise I will buy from provider B
    if provider_b_selling_cost > provider_a_selling_cost:
        return "A", provider_a_selling_cost
    else:
        return "B", provider_b_selling_cost
main()