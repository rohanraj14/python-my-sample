import os.path

def calcBreakin(x) :
    ip = x.split(' ')
    operation = ip[1]
    int1 = int(ip[2])
    int2 = int(ip[3])
    if operation == '+':
        print(int1 + int2)
    if operation == '-':
        print(int1 - int2)
    if operation == '*':
        print(int1 * int2)
    if operation == '/':
        print(int1 / int2)

with open(os.path.abspath('Firstday/input.txt'), 'r') as calculator:
    each_ip= calculator.read().splitlines()
    line_count = len(each_ip)
    currentLine = 0
    while currentLine < line_count:
        calcBreakin(each_ip[currentLine])
        currentLine = currentLine+1
    
    
