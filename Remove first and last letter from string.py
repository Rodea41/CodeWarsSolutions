def remove_char(s):
    new_str = str(s)        ##Converts s parameter into a string object so
    front_slice = new_str[1:]  ## Slices the first letter of the string and stores in a var
    back_slice = front_slice[:-1] # takes the new sliced string and slices off the last letter

    return back_slice ## Returns the string after removing the first & last letter
    
 