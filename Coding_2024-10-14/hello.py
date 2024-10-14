import datetime
import sys

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:]) #join all provided parameters with spaces
    # call like this: python .\hello.py Marci
    # when no parameters are provided, we would get the index out of range error wthout the if
else:
    name = input('Please enter your name now! ')
print(f'Hello {name}, it is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')
