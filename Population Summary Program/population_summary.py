# Title: Population Summary Program
# Program created by William Schaeffer
# CPS 313
# P. 428, Exercise 9, Population Summary Program
# 02.01.22

# This program will read the contents of the USPopulation.txt and place files into a list
# From the list, we will display average annual change in population, greatest increase, and smallest increase
# This program is not long enough to justify separating functions into new files, but it is good practice

# imports

import popcalc

# Main Function

def main():
    
    welcome_function()                                                      # Call welcome function
    
    population_file = open('USPopulation.txt', 'r')                         # open USPopulation.txt
    
    population_list = [int(line.strip()) for line in population_file]       # example 7.17 in the book is...unnecessary

    #print(f'{population_list}')                                            # commented print of population list for test verification

    # call function to create change in population list
    change_in_population = popcalc.create_change_in_population(population_list)    

    # call function to calculate average annual change in population
    popcalc.average_annual_change(change_in_population)                             

    # call function to calculate the greatest increase in population
    popcalc.greatest_population_increase(change_in_population)                      

    # call function to calculate the least increase in population
    popcalc.least_population_increase(change_in_population)                         

    population_file.close()                                                 # close USPopulation.txt

    # Function Definition

def welcome_function():                                 # Function to welcome user

    print(f'Welcome to the Population Summary Program!\n')

main()                                                  # Call main function

