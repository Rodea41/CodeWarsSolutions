"""Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
function should return true if the string is valid, and false if it's invalid.
"""


def valid_parentheses(string):          ### Create the function
    str1 = str(string) ### If the parameter 'string' contains numbers and letters you must convert it all to a string

    open1 = 0  # Create an empty variable to count how many open parantheses

    close = 0  # Create empty var to count closed parantheses
    
    outoforder = 0 
    
    strip_spaces = string.strip()           ## Strips the string of any leading spaces. For example "   ("
    
    rev_str = "".join(reversed(str1))
    chk_rev_open = rev_str.find('(')
    chk_rev_close = rev_str.find(')')
    
    chkopen = str1.find('(')   ## Find index of first '('. Returns value -1 if it is not in the string
    chkclose = str1.find(')')  ## Find index of first ')' . Returns value -1 if it is not in the string 

    if chkopen == chkclose == -1: ## If both () elements are not found in string return TRUE
        return True
    
    if chkopen == -1:           # return false if there is no open parantheses in string
        return False     
    
    if chkclose == -1:         # return false if no close parantheses in string
        return True

    if chkopen > chkclose:      ## check if a close parantheses appears first in the string before
       return False          ## an opening then it returns false. 

    if chk_rev_open < chk_rev_close:    ## Checks to make sure string doesnt end with an opening parantheses
        return False
    
    if string == "":
        return True
    
    if strip_spaces[0] ==')':                       
            return False
        
                                           
    for letters in range(len(strip_spaces)):
        if strip_spaces[letters] == '(':
            open1 += 1
                    
        elif strip_spaces[letters] == ')': 
            close += 1 
    
                
    print('Original string is ' + str(strip_spaces))
    print('First open index is at ' + str(chkopen))
    print('First open index is at ' + str(chkclose))
    print('Value of open1 is ' + str(open1))
    print('Value of close is ' + str(close))
    print('This is the reversed string ' + str(rev_str))
    print('Index of rev open ' +  str(chk_rev_open))
    print('This is the index of rev close ' +  str(chk_rev_close))


    if open1 == close:
       return print('True')
    else:
        return print('False')

    
valid_parentheses('())(()') """Call the function"""
