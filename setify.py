# Create a function that sorts a list and removes all duplicate items from it.
# Examples

# setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]

# setify([4, 4, 4, 4]) ➞ [4]

# setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]

# setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]


# A set is a collection of unique items.
# A set can be formed from a list by removing all duplicate items.



def setify(lst):
    return sorted(set(lst))

# Examples
print(setify([1, 3, 3, 5, 5]))  
print(setify([4, 4, 4, 4]))  
print(setify([5, 7, 8, 9, 10, 15]))  
print(setify([3, 3, 3, 2, 1])) 




# If you prefer not to use the set() built-in function, 
# you can manually implement the process of removing duplicates and then sorting the list.
# Here’s how you can do it:



# def setify(lst):
#     unique_lst = []
#     for item in lst:
#         if item not in unique_lst:
#             unique_lst.append(item)