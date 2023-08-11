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


class Podracer: # Podracer class with max_speed, condition and price defined.
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer): # New class that inherits the Podracer class.
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)


    def boost(self): # Boost function that increases speed by 2x.
        self.max_speed *= 2

class SebulbasPod(AnakinsPod): # New class that inherits the -AnkinsPod class.
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"

