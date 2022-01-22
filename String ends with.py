"""
Complete the solution so that it returns true if the first 
argument(string) passed in ends with the 2nd argument (also a string).

Examples: 

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

"""

def solution(string, ending):
    
    end_length = len(ending)        ## Getting the length of the ending string
    str_last = string[-(end_length):]   ## Slicing the original string in reverse order, using the negative index as a 
                                        ## starting point. so if ending is 2 letters long, we are slicing the last 2 letters
                                        ## of the string to compare

    if ending == '':                # If ending string is empty, return true
        return True
    elif ending == str_last:        # If the ending letters match our sliced string, return True 
        return True
    else:
        return False



solution('abc', 'bc') # Calling the function



