'''
How is the order of duplicate values handled in Quick Sort and Merge Sort? Provide an example where these different ways of handling duplicates impact the sorted output.
'''

answer = '''
As Merge Sort runs, it recursively creates lists from the original data. In these lists, the order / index of the original data is preserved,
when the sub-lists are remerged, sorted. Of course, if two elements are not equal and have been sorted, their index will change. However, if
two elements have the same value, Merge Sort will not move them, preserving their indexes and position. This qualifies Merge Sort as a stable algorithm.

Quick Sort is not a stable algorithm as elements can be moved relative to the pivot, regardless of their initial index / position in the list. 
Two elements that have been moved over the pivot might have their order reversed. This is particularily concering when sorting dictionaries or
other data structures by multiple keys and their position might change. For example, if we have a dictionary with employees and their remaining
vacation days and we have two employees with the same name, the order in a Quick Sort might be different than a Merge Sorted dictionary. 

'''