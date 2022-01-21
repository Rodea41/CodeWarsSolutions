"""" code using comprehensions is considered more ‘Pythonic’ — better fitting
Python’s style guidelines. """




##EXAMPLE 1
"""

some_list = [(i) for i in range(10)] ## Syntax for looping through list

#print(some_list)

"""



#EXAMPLE 2 
"""

some_list = [1,2,3,4,5,6,7,8,9]     ## Original list 

only_even = [n for n in some_list if n%2==0] ### Iterates through list and keeps if they are divisible by 2
only_odd = [n for n in some_list if n%2!=0]  ### Iterates through list and keeps if they are not divisible by 2

"""

some_list = [1,2,3,4,5,6,7,8,9]

def even(n):            ## Create a function and pass it through 
  return n%2 == 0       ## the list below 

only_even_prettier = [n for n in some_list if even(n) ]


#print(only_even)
#print(only_odd)
print(only_even_prettier)
