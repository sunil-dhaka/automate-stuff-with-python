"""
meta info:
    Author: @sunil-dhaka
    A simple script implements strip() function using regex
"""
import re,sys

def regex_strip(input_str,seperater=' '):
    
    match_regex=re.compile(f'([^\{seperater}]+)') #IMPORTANT STEP
    match_result=match_regex.findall(input_str)
    return match_result

if __name__=="__main__":
    """TODO: using argparse it can be done more nicely and effectively"""
    # if len(sys.argv)>1:
    #     input_str=sys.argv[1:-1]
    #     try:
    #         seperater=sys.argv[-1]
    #     except IndexError:
    #         # default is  " "
    #         seperater=' '
    # else:
    #     print('Input formate: <input-string> <seperater>; default seperater is " ".')
    #     sys.exit()
    input_str=input('str input > ')
    seperater=input('seperater > ')
    print(regex_strip(input_str,seperater))