def basic_op(operator, value1, value2):
    operator = str(operator)    #converts first parameter to a str object and stores in var 
    
    value1 = int(value1)        #converts the second parameter to an int so we can do math operations
    
    value2 = int(value2)
    
    if operator == "+":             # if first param is + , add both numbers
        return (value1 + value2)
        
    if operator == "-":
        return (value1 - value2)
        
    if operator == "*":
        return (value1 * value2)
        
    if operator == "/":
        return (value1 / value2)


basic_op(+, 4, 3) #calls the function and adds 4 and 3 together