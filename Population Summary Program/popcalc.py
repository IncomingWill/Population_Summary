# Title: Population Summary Program
# Program created by William Schaeffer
# CPS 313
# P. 428, Exercise 9, Population Summary Program
# 02.01.22

def average_annual_change(list):                        # Function to calculate average population change

    total = 0.0                                         # create accumulator

    for value in list:                                  # calculate total
        total += value

    average = total / len(list)                         # average equals total divided by number of elements in list

    print(f'The average increase in population during the period is {average:.0f}')


def greatest_population_increase(list):                 # Function to display maximum population increase

    maximumValue = max(list)
    maxIndex = (list.index(maximumValue) + 1950)        # Start year is 1950

    print(f'The greatest increase in population during the period is {maximumValue} and was in the year {maxIndex}')
    

def least_population_increase(list):                    # Function to display minimum population increase

    minimumValue = min(list)
    minIndex = (list.index(minimumValue) + 1950)        # Start year is 1950

    print(f'The least increase in population during the period is {minimumValue} and was in the year {minIndex}')

# Function to create a list with the change in population from year to year
    # Function will determine the difference between each subsequent value and add to a new list
    # Function will return the list for further calculations

def create_change_in_population(list):

    change_list = []                                    # initialize change in population list

    for i in range(len(list) - 1):                      # create range, index of last element is len(list) - 1
        change_list.append(list[i+1] - list[i])         # append the difference of each value to change_list

    return change_list                                  # return change_list to pass to other functions
    #print(f'{change_list}')                            # commented print of change_list for test verification