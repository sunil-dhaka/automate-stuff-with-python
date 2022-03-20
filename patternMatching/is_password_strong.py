"""
meta info:
    Author: @sunil-dhaka
    A simple script that checks whether a passowrd is strong or not.
    Definition of what is considered a strong password can be changed.
"""
import re

def strong_password_check(password):
    return_str=''
    if len(password)<8:
        return_str+= 'Password shall have at least 8 chars.'
    else:
        tmp_regex=re.compile(r'[0-9]')
        digit_check=tmp_regex.findall(password)
        if not bool(digit_check):
            return_str+='Password does not contain any digits.\n'
        tmp_regex=re.compile(r'[a-z]')
        lower_alpha_check=tmp_regex.findall(password)
        if not bool(lower_alpha_check):
            return_str+='Password does not contain any lower chars.\n'

        tmp_regex=re.compile(r'[A-Z]')
        upper_alpha_check=tmp_regex.findall(password)
        if not bool(upper_alpha_check):
            return_str+='Password does not contain any upper chars.'

    if bool(return_str):
        return return_str
    else:
        return 'Password is strong enough.'

if __name__=="__main__":
    password=input('password > ')
    print(strong_password_check(password))