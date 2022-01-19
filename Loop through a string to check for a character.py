def valid_parentheses(string):          ### Create the function
    str1 = str(string) ### If the parameter 'string' contains numbers and letters you must convert it all to a string
    open1 = 0  # Create an empty variable to count how many open parantheses
    close = 0  # Create empty var to count closed parantheses
    
    
    if str1[0] == ')':                      ## Checks if string starts with a 'close' parantheses . Auto reject if true
            return print('false')
    else:                                   ## Goes through each letter to check for '(' and adds to var open1
        for letters in range(len(string)):  ## IMPORTANT ## YOU MUST USE 'range(len(string)' in your loop statement or you will get an error saying 
            if string[letters] == '(':      ## TypeError: string indices must be integers
                open1 += 1
                
            elif string[letters] == ')':    # Goes through each letter to check for ')' and adds to var close
                close += 1

    if open1 == close:                      ## Returns true if there is a same amount of open and close parantheses. false if uneven amount. 
        return print("true")
    else:
        return print("false")


valid_parentheses("(())((()())())")
