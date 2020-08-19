import argparse

def isMultipleThree(x):
    if x%3==0:
        return 'Fizz'
    else:
        return x

def isMultipleFive(x):
    if x%5==0:
        return 'Buzz'
    else:
        return x

def isMultipleSeven(x):
    if x%7==0:
        return 'Bang'
    else:
        return x

def isMultipleEleven(x):
    if x%11==0:
        return 'Bong'
    else:
        return x
        
def isMultipleThirteen(x):
    if x%13==0:
        return 'Fezz'
    else:
        return x


x=1
# Take a argument in commandline 
parser = argparse.ArgumentParser(description='Enter some integer.')
parser.add_argument('inp', metavar='N', type=int,
                    help='an integer input')
args = parser.parse_args()
inp = int(args.inp)
# Asks for an input integer
#inp=int(input())
while x <= inp:
    y=x
    if x%11==0:
        y=isMultipleEleven(x)
    elif x%3==0 and x%5==0 and x%7==0:
        y=isMultipleThree(x)+isMultipleFive(x)+isMultipleSeven(x)
    elif x%3==0 and x%5==0:
        y=isMultipleThree(x)+isMultipleFive(x)
    elif x%3==0 and x%7==0:
        y=isMultipleThree(x)+isMultipleSeven(x)
    elif x%3==0:
        y=isMultipleThree(x)
    elif x%5==0:
        y=isMultipleFive(x)
    elif x%7==0:
        y=isMultipleSeven(x)


    if y!=x and len(y)==4 and x%13==0 and y[0]=='B':
        y=isMultipleThirteen(x)+y
    elif y!=x and len(y)==4 and x%13==0 and y[0]!='B':
        y=y+isMultipleThirteen(x)
    elif y!=x and len(y)>4 and x%13==0 and y[4]=='B':
        y=y[0:4]+isMultipleThirteen(x)+y[4:]
    elif x%13==0:
        y=isMultipleThirteen(x)

    if y!=x and len(y)>4 and x%17==0:
        y=y[8:]+y[4:8]+y[0:4]

    print(y)
    x=x+1