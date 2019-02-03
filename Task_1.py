postal_code_1 = "79-900"
postal_code_2 = "80-155"
print('Postal code 1 = ' + postal_code_1)
print('Postal code 2 = ' + postal_code_2)
print('Displaying postal codes between:')

def codes_between(var_min,var_max):
    custom_code_number = var_min + 1
    while custom_code_number < var_max:
        custom_code_string = str(custom_code_number)
        custom_postal_code = custom_code_string[:2] + "-" + custom_code_string[2:]
        print(custom_postal_code)
        custom_code_number += 1
codes_between(79900,80155)