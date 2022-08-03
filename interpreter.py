from logging import raiseExceptions
from operator import index


input_file = open('language.txt', 'r')
input_text = input_file.read()

program_lines = input_text.split('\n') #Divides the text into lines and starts 
                                       #interpreting the separate lines
keywords = ["VAR", "PRINT", "IF"]

for line in program_lines:
    splitted = str(line).split(' ') 
    
    if splitted[0] in keywords:
        """
    'PRINT' keywoard prints the expression that comes after the space following the keyword.
    For example 'PRINT Hello world' will print 'Hello world'.
    """ 
        if splitted[0] == 'PRINT':
            if (len(splitted) == 2) and (splitted[-1] == var):      
                print(value)
            elif len(splitted) >= 2:    
                splitted.remove('PRINT')
                for ele in splitted: 
                    print(ele, end = ' ')
                print()
            
        """
    'VAR' keyword declares a variable. Enter the keyword VAR, 
    then the identifier (variable name), then a spase(' '), 
    the equals symbol('='), a spase(' ') and the value you want to assign to 
    the identifier. The value can be an expression, but you cannot use any spaces in it.
    """
        
        if splitted[0] == 'VAR':
            var = splitted[1]
            value = splitted[-1]
            dict = {var: value}

        
        """
    'IF' checks the condition given after the kewywoard (separated with a space). 
    In case it returnes True value the set of code present after the condition will be executed.  
    IF condition operation. 
    """ 
        def my_extend(self, other_list, index):
            self[index:index] = other_list
        if splitted[0] == 'IF':
            cond = splitted[1]
            if cond:
                new_line = line[4 + len(cond)::]
                my_extend(program_lines, list(new_line.split("\n")), program_lines.index(line) + 1)


    else:
        raise SyntaxError("The firs word of the line must be a keywoard.")   
    