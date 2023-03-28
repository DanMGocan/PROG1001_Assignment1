'''
How do Quick Sort and Merge Sort algorithms differ regarding space complexity? How does this difference impact the efficiency of each algorithm?
'''

answer = '''
Quick Sort is an in place algorithm, meaning that all the permutation and calculations are done on the array (or list) already fed to the program.
No additional memory is required and the recursivity will not create additional lists. In Merge Sort however, every iteration of the recursive function
will create 2 more additional lists (the two halves of the original list) and for a large data set, this can agglomerate the stack and occupy a lot of
extra space in memory. For a modern computer or device, this wouldn't be a problem - as noted in question 1, a list of 200000 elements can still be 
sorted in under a second, with a very, very small percentace of the total available memory. However, this can become an issue in certain IoT devices
or microcontrollers. 

The impact on the efficiency of each algorithm is highly dependant by the requirements and constraints of the problem at hand. For someone trying to 
sort large values using a smart fridge, probably Quick Sort is the best solution, while for someone trying to sort the atoms in the universe using
a billion quantum computers, maybe Merge Sort would work better. As with a lot of approaches and techniques, there is no correct answer and it all
depends on the variables, the problem and the tools available. 

'''