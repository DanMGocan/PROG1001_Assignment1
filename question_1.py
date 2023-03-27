import time

'''
Question 1 - 20 marks
The empirical analysis of sorting algorithms studies the relation between the input size and the running time. 
An example of empirical analysis is presented in week 3 slides 13, 14 and 15, where the Bubble Sort algorithm running time is tested considering nine different input sizes. 
The time it takes to run each input was measured using the Python time module.
For this question, you are asked to work on an empirical analysis of the Merge Sort algorithm using a programming language of your preference.

In this question, you are expected to provide:
-	A brief explanation of how you carried out the empirical analysis.
-	The code used for the empirical analysis. This can be provided by a link to an online IDE (such as Trinket) or by submitting your code in a separate file.
-	A graph demonstrating how the running time of Merge Sort behaves in relation to the input size. This graph can be plotted using the tool of your preference, such as Microsoft Excel or a Python library like 
-	A table with two columns: one for the input sizes you selected and another with the running time for each input.
Notes: You can reuse the Merge Sort code example provided by the lecturer. If you decide to use an online IDE, beware that it might take a while to sort large data. 
'''

# The code used for this analysis #
''' Please see below. The "merge_sort" function is where the algorithm is defined.'''

data_list = [2, 8, 5, 3, 9, 4, 1, 7]

def merge_sort(data):

    if len(data) > 1:

        # We use the // operator to round down the lenght of the list and to find the midpoint of the list.
        list_mid = len(data)//2

        # Using Python tools, we split the list in two, the left side and the right side, using the previously
        # found mid-point as the end / start of these sub-lists
        list_left = data[:list_mid]
        list_right = data[list_mid:]

        merge_sort(list_left)
        print(list_left, "is the left side of the list")
        merge_sort(list_right)
        print(list_right, "is the right side of the list")

        i = j = k = 0
        
        while i < len(list_left) and j < len(list_right):
            if list_left[i] < list_right[j]:
                data[k] = (list_left[i]) # reassigning the first element of the data list
                i += 1 # tracking the left side 

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
    
    print(data)


merge_sort(data_list)




     

def create_graph(data):
    pass

def create_table(data):
    pass