'''
Following the lecture notes guidelines, demonstrate the pseudocode for the Quick Sort algorithm in its original implementation (no variations).
'''

# Pseudocode taken from the wiki page: https://en.wikipedia.org/wiki/Quicksort
# All my comments are marked with the "#" symbol inside the pseudocode definition

'''
A = [3, 1, 2, 9, 5, 0, 4, 8, 7, 6]

// Sorts a (portion of an) array, divides it into partitions, then sorts those

# In this case, the A is the list defined above, lo is = 0 and hi is = 9 (list length - 1)
# Since lo is smaller than hi, we proceed to the partition function of the 
# algorithm
algorithm quicksort(A, lo, hi) is
  if lo >= 0 && hi >= 0 && lo < hi then
    p := partition(A, lo, hi) 
    quicksort(A, lo, p) // Note: the pivot is now included
    quicksort(A, p + 1, hi) 

# In the partition function, we define the pivot. In this implementation of the
# algorith, the pivot is in the middle of the list. The pivot for this list is 5
# the element at index [4](floor(9 - 0)/2 + 0) 
// Divides array into two partitions
algorithm partition(A, lo, hi) is 
  // Pivot value
  pivot := A[ floor((hi - lo)/2) + lo ] // The value in the middle of the array

  # We initiate the left and right indexes. They will keep track of what elements in the
  # list are compared and where the swaps need to be done. 
  // Left index
  i := lo - 1 # initiated as -1
  j := hi + 1 # initiated as 10

  # This is the loop that continues to go through and compare all the elements. 

  # We keep decrementing the right index by one until we find an element smaller than
  # or equal with the pivot. In this case, 4

    # We keep incrementing the left index by one until we find an element greater than
  # or equal with the pivot. In this case, 9
  // Right index
  loop forever 
    // Move the left index to the right at least once and while the element at
    // the left index is less than the pivot
    do i := i + 1 while A[i] < pivot
    
    // Move the right index to the left at least once and while the element at
    // the right index is greater than the pivot
    do j := j - 1 while A[j] > pivot

    
    // If the indices crossed, return
    if i >= j then return j

    # Whenever both indices have values without crossing each other, the values are swapped.
    # In this case, the 9 and the 4 move on the other side of the pivot and the new list is
    # A = [3, 1, 2, 4, 5, 0, 9, 8, 7, 6]

    // Swap the elements at the left and right indices
    swap A[i] with A[j]

    # Loop until the list is sorted
    '''



