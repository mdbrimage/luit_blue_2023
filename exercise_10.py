"""
Write a function named unique. The function should accept one parameter, 
which is a list with any number of elements inside. 
The default value for the parameter should be an empty list ([]).

The function should return a new list with all duplicate elements removed. 
The function should preserve the original order of elements.

Example 1: for unique([1, 1, 4, 5, 1]), the output should be [1, 4, 5]
Example 2: for unique(['Mark', 'Mark', 'John', 'Anne']), the output should be  ['Mark', 'John', 'Anne']
"""

non_unique1 = [1, 1, 4, 5, 1]

non_unique2 = ['Mark', 'Mark', 'John', 'Anne']

def unique(duplicate_list = []):
    newList = []
    
    for item in range(len(duplicate_list)):
        if duplicate_list[item] not in newList:
            newList.append(duplicate_list[item])
            
    return newList
    
print(unique(non_unique1))
print(unique(non_unique2))