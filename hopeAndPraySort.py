import random as rand
def hopeAndPraySort(arr):
    '''
    Returns either a sorted list or an unsorted list given any list
    Parameters:
        arr: A list
    Returns:
        arr: A list containing the same elements which are either sorted or unsorted
    '''
    rand.shuffle(arr)
    return arr
