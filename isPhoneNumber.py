import sys

if len(sys.argv)>1:
    text=sys.argv[1]
else:
    print('give any string that you wish to check as phine number')

def isPhoneNumber(text):
    if '-' not in text:
        return False
    else:
        split_data=text.split('-')
        if len(split_data)==3:
            if len(split_data[0])==3 and len(split_data[1])==3 and len(split_data[2])==4 and split_data[0].isnumeric() and split_data[1].isnumeric() and split_data[2].isnumeric():
                return True
            else:
                return False
        else:
            return False

if __name__=='__main__':
   print (isPhoneNumber(text))