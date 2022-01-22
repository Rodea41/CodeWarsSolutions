""""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
Its guaranteed that array contains at least 3 numbers.
"""


def find_uniq(arr):
    uniq = [var for var in arr if arr.count(var) <= 1] # Uses list comprehension to filter out any number

    return print(uniq[0]) #Returns the value of the unique number
    


find_uniq([ 1, 1, 1, 2, 1, 1 ])

