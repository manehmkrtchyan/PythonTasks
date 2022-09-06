string = str(input('Enter the data you want to check: '))

def data_validator(string):

    import re
    regular_expression_email = '^[a-zA-Z]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
    regular_expression_url = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    regular_expression_date = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
    regular_expression_number = "^[0-9]+[\.]?[0-9]+$"
    regular_expression_card_number = "^[0-9]{4,}[-][0-9]{4,}[-][0-9]{4,}[-][0-9]{4,}$"
    regular_expression_mobile = "^\\+?[1-9][0-9]{7,14}$"

    if re.search(regular_expression_email, string):   
        print("Valid Email")   
    elif re.search(regular_expression_url, string):   
        print("Valid URL")
    elif re.search(regular_expression_date, string):
        print("Valid Date")
    elif re.search(regular_expression_number, string):
        print("Valid Number")
    elif re.search(regular_expression_card_number, string):
        print("Valid Credit Card Number")
    elif re.search(regular_expression_mobile, string):
        print("Valid Mobile Phone Number")
    else:   
        print("Invalid Data")

data_validator(string)