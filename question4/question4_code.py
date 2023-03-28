'''
In what situation would you recommend somebody to use Quick Sort? What about Merge Sort? Explain why.
'''

answer_quick_sort = '''
Quick Sort is best used when memory is a concern, but not the time. There is a certain level of randomness
in Quick Sort, based on the pivot selected, which can make the algorithm perform better or worse. I would
recommend someone to use Quick Sort on data sets that are smaller and where memory is more of a concern than
time complexity.
'''

answer_merge_sort = '''
Merge Sort algorithm's main disadvantage is that is uses a lot of extra memory in order to create all the sub-lists. 
On a data set of say 2.000.000 entries, there is a lot of extra space required. However, it must be noted that merge
sort fares better in terms of time complexity and especially for large data sets, it will fare better than Quick Sort.
It will also provide a more consistent performance, as the algorithm will always perform the same operations and there
is no random pivot involved - the guaranteed time complexity, regardless of input size is O(n log n).
'''