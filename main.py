'''
Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

Remember, when writing in a functional style:
Keep variables immutable
Write only pure functions
Remember, functions may be higher order
'''

def flatten_and_sort(array): # New function for a flattened and sorted array
    flattened_and_sorted = [num for list in array for num in list] # Create a new list by iterating through the array
    new_list = sorted(flattened_and_sorted) # Applied sorted() function to print the new list accordingly
    return new_list

arr = [2, 10, 3], [0, 1, 9], [7, 7, 8], [2, 15, 4] # Lists of numbers to sort
result = flatten_and_sort(arr) # Apply array to the function flatten_and_sort 
print(result) # Print the result


