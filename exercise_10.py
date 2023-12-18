"""
Write a function named unique. The function should accept one parameter, 
which is a list with any number of elements inside. 
The default value for the parameter should be an empty list ([]).

The function should return a new list with all duplicate elements removed. 
The function should preserve the original order of elements.

Example 1: for unique([1, 1, 4, 5, 1]), the output should be [1, 4, 5]
Example 2: for unique(['Mark', 'Mark', 'John', 'Anne']), the output should be  ['Mark', 'John', 'Anne']
"""

def unique(duplicate_list = []):
    newList = [] #creating a new list
    
    for item in range(len(duplicate_list)): #iterating over the list with duplicates
        if duplicate_list[item] not in newList: #comparing the list with duplicates to the new list
            newList.append(duplicate_list[item]) #appending values to the new list
            
    return newList
    
