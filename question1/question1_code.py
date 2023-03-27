import time # if only it were this simple... 
import random # module to create a list of random numbers
import matplotlib.pyplot as plot # module used to create graphs
from tabulate import tabulate # module used to create the table


'''
A brief explanation of how you carried out the empirical analysis.
    First, we have written the merge sort algorithm and made sure it works.
    Then, we have devised a function that applies this algorithm to Python lists of increasing sizes. The initial size, maximum size and rate of growth
    for the length of these list can be modified through the function parameters, when the function is called. This function will save the number of 
    elements in the list and how long did it take to sort them and using this data (passed to other functions) graphs and tables are created. In these tables
    we can notive that the more data we have, the longer it takes for this data to be sorted. To be noted, that the duration of sorting grows proportionally 
    with the length of the list (e.g. a list of 2000 elements gets sorted twice as slow as a list of 1000 elements)


The code used for the empirical analysis. This can be provided by a link to an online IDE (such as Trinket) or by submitting your code in a separate file.
    All code used can be found below. Please note that certain modules might have to be installed in order to run the code (tabulate anad matplotlib especially)

    
A graph demonstrating how the running time of Merge Sort behaves in relation to the input size. This graph can be plotted using the tool of your preference, such as Microsoft Excel or a Python library
    question1_graph1 has been computed for this purpose. It shows that the sorting speed slows down proportionally with the length of data. 10 times more data
    will get sorted 10 times slower. However, this graph does not take into account memory used. 

    
A table with two columns: one for the input sizes you selected and another with the running time for each input.
    Please see question1_table.txt or run this program with an input of your choice. Please be aware that due to time constrains, error checking hasn't been
    implemented (inputting negative numbers, strings instead of integers, etc.)
'''


# The merge sort function, takes a list of numbers as the single parameter and
# returns the duration it takes to have the list sorted
def merge_sort(data):

    # Nanoseconds elasped since inception of time
    initial_time = time.perf_counter_ns()

    if len(data) > 1:

        # Using Python tools, we split the list in two, the left side and the right side, using the previously
        # found mid-point as the end / start of these sub-lists
        list_left = data[: len(data)//2]
        list_right = data[len(data)//2 :]

        merge_sort(list_left)
        merge_sort(list_right)

        i = j = k = 0
        
        while i < len(list_left) and j < len(list_right):
            if list_left[i] < list_right[j]:
                data[k] = (list_left[i]) 
                i += 1 

            else:
                data[k] = list_right[j]
                j += 1

            k += 1

        while i < len(list_left):
            data[k] = list_left[i]
            i += 1
            k += 1

        while j < len(list_right):
            data[k]=list_right[j]
            j += 1
            k += 1
    
    return time.perf_counter_ns() - initial_time

# Creates a predefined number of lists to be sorted by the merge_sort function.
# initial_data_length: how long is the initial list to be sorted
# maximum_length: the while loop will stop once the length of the list is over this value
# increments: every loop, the length of the data set is multiplied with this value
def create_data(initial_data_length, maximum_length, increments):

    results = {}

    i = initial_data_length
    test_iteration = 0
    while i <= maximum_length:
        test_iteration += 1
        # Initiating an empty dictionary for every data set that contains i number of elements
        results[f"{i} elements"] = {}
        

        # Creating lists of elements to be sorted
        data = random.sample(range(1, maximum_length), i-1)

        # The merge_sort function returns the duration it takes for itself to execute in nanoseconds 
        # and we convert it to miliseconds
        duration = merge_sort(data) / 1000000

        results[f"{i} elements"]["iteration"] = test_iteration

        # Add the duration and the ratio variables to the dictionary
        results[f"{i} elements"]["duration"] = round(duration, 2)


        # Calculation the ratio between the duration of sorting a list and the previous, 10 times shorter list
        # Then, adding the ratio to the results dictionary
        try:
            ratio = float(round(results[f"{i} elements"]["duration"] / results[f"{int(i/increments)} elements"]["duration"], 2)) 
        except:
            ratio = 0

        results[f"{i} elements"]["ratio"] = ratio

        # Incrementing i so the next list is 10 times longer    
        i *= increments

    

    return results

# The graphs for with the sorting durations are saved as separate .png images.
# If you want to check / recreate them, please call this function with "True" parameters
# (more details below)
def create_graph(data, duration=False, ratio=False):

    # Using MatPlotLib module to easily create the graphs for this analysis
    no_of_elements_list = data.keys()
    durations = []
    ratios = []
    for element in no_of_elements_list:
        durations.append(data[element]["duration"])
        ratios.append(data[element]["ratio"])

    if duration:
        plot.plot(no_of_elements_list, durations, label = "Durations")
        plot.xlabel("Length of list")
        plot.ylabel("Duration to sort in miliseconds")
        plot.title("The relations between input size and execution duration in Merge Sort algorithm")
        plot.legend()
        plot.show()

    if ratio:
        plot.plot(no_of_elements_list, ratios, label="Ratios")
        plot.xlabel("Length of list")
        plot.ylabel("Ratio between one element and the previous one")
        plot.title("The time ratio that it takes to sort lists of exponential length")
        plot.legend()
        plot.show()

# Using Tabulate module to create the table in the CLI 
def create_table(data):
    no_of_elements_list = data.keys()
    master_list = [["Iteration", "Length of list", "Duration to sort", "Ratio between sorting durations"]]

    for element in no_of_elements_list:
        empty_list = []
        empty_list.append(data[element]["iteration"])
        empty_list.append(element)
        empty_list.append(f'{data[element]["duration"]} miliseconds')
        empty_list.append(data[element]["ratio"])
        master_list.append(empty_list)

    pretty_table = tabulate(master_list, headers="firstrow", tablefmt="fancy_grid")
    with open ("question1/question1_table.txt", "w", encoding="utf-8") as f:
        f.write(str(pretty_table))
        f.close()

    print(pretty_table)

# In order to make sure that the graphs and the table have the same data, a variable is created
# and to it, we assign the return value of our create_data function
data = create_data(100, 100000, 2)

# Calling the function to create the graphs. If you wish to create the graphs change the
# default parameters to True (1st is for Duration, 2nd for Ratio between durations)
create_graph(data, False, False)

# Calling the function to create and print tables. It also saves the table in a .txt file
create_table(data)
