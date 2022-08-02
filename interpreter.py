from logging import raiseExceptions


input_file = open('language.txt', 'r')
input_text = input_file.read()

program_lines = input_text.split('\n') #Divides the text into lines and starts 
                                       #interpreting the separate lines
keywords = ["VAR", "PRINT", "IF"]

"""
'VAR' keyword declares a variable. Enter the keyword VAR, then the identifier (variable name) 
then a spase(' '), the equals symbol('='), a spase(' ') and the value you want to assign to 
the identifier. The value can be an expression, for example 5*5, but you cannot use any spaces in it.
"""
"""
'PRINT' keywoard prints the expression that comes after the space following the keyword.
For example 'PRINT Hello' will print 'Hello'.
"""
# def do_var():
#     my_dict = {splitted[1]: splitted[-1]}
# def do_print(word):
#     print(word, end = ' ')    

for line in program_lines:
    splitted = str(line).split(' ') 
    
    if splitted[0] == 'PRINT':
        splitted.remove('PRINT')
        for ele in splitted: 
            print(ele, end = ' ')
        print()
    
    if splitted[0] == 'VAR':
        my_dict =  {splitted[1]: splitted[-1]}
        var = splitted[1]
            
    # if 'VAR' in splitted:
    #     do_var()
    #     var = splitted[1]
    # if var in splitted:
    #     print(var)
    
    # elif 'IF' in splitted:
    #     if splitted[1]:
    #         if 'VAR' in splitted:
    #             dict1 = {splitted[3]: splitted[-1]}
    #         elif 'PRINT' in splitted:
    #             print(splitted[-1])
    #         else:
    #             raise Exception("SyntaxError")
