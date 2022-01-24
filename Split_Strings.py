""""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing 
second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

"""


def solution(s):
    #Get length of string
    lengthOfString = len(s)
    
    #Create varialble that stores our original string
    #and adds a underscore '_' to the string passed through.
    odd = s + '_'
    
    #Create an empty object to be returned if the string passed through
    #is empty
    empty_container = []
    
    #This variable will be used for incrementing in our list comprehensions below
    n=2
    
    ## String Comprehension - Takes the list created in var odd, then slices the 
    ## string starting at odd[0: 0 + 2] and increments by 2 (because var n is set to 2)
    ## interation ==> odd[0: 0 + 2] then odd[2: 2 + 2] then odd[4: 4 + 2] which is all stored
    ## into variable named odd_split. We use this variable if the string length isnt an even number
    odd_split = [odd[index : index + n] for index in range(0, len(odd), n)]
    

   
    ## String comprehension - Takes the original string 's' and slices it starting at s[0: 0+2]
    ## then icrements it by 2, so next slice would be s[2: 2 + 2], and then s[4:4+2]     
    split_strings = [s[index : index + n] for index in range(0, len(s), n)]

    

    #If the string passed through is empty, we return var empty_container ==> []
    if s == '':
        print(empty_container)
    
    #If only 1 letter is passed (ex => 'a') we add an underscore and return that string (ex => 'a_')
    if len(s) == 1:
        return [str(s) + '_']

    #If the length of string is odd, we return the list created in 'odd_splits'
    #If it is even, then we return the list created in 'split_strings'
    if lengthOfString %2 != 0:
        return odd_split
    else:
        return split_strings
       

solution('asdfads')