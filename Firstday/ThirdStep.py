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
        print(int1 // int2)

def checkGoto(x)
    ip = x.split(' ')
    if ip[0]=='goto':
        if ip[1] != 'calc':
            return int(ip[1])
        else:
            return calcBreakin(ip[1]+' '+ip[2]+' '+ip[3]+' '+ip[4])


with open('input.txt', 'r') as calculator:
    each_ip = calculator.read().splitlines()
    line_count = len(each_ip)
    currentLine = 0
    while currentLine < line_count:
        current_statement = each_ip[currentLine]
        
        each_ip(int(checkGoto(current_statement))
        currentLine = currentLine+1
    
    
