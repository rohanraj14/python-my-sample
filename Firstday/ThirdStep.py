import os.path

def calcBreakin(x) :
    ip = x.split(' ')
    operation = ip[1]
    int1 = int(ip[2])
    int2 = int(ip[3])
    if operation == '+':
        return int1 + int2
    if operation == '-':
        return int1 - int2
    if operation == '*':
        return int1 * int2
    if operation == '/':
        return int1 // int2

def checkGoto(x):
    ip = x.split(' ')
    if ip[0]=='goto':
        if ip[1] != 'calc':
            return int(ip[1])
        else:
            return calcBreakin(ip[1]+' '+ip[2]+' '+ip[3]+' '+ip[4])


def itrateMe( current_statement, line_count, list_stmts):
    newIndex = checkGoto(current_statement)
    if newIndex is not None and int(newIndex) < line_count:
        new_statement = each_line[int(newIndex) - 1]
        #evaluatye new statement
        if new_statement not in list_stmts :
            list_stmts.append(new_statement)
            itrateMe(new_statement, line_count, list_stmts)
        else:
            print('Already passed once : '+ new_statement)


with open(os.path.abspath('Firstday/input3.txt'), 'r') as calculator:
    each_line = calculator.read().splitlines()
    line_count = len(each_line)
    currentIndex = 0   
    list_stmts = []
    
    while currentIndex < line_count:
        current_statement = each_line[currentIndex]
        #Now go to calculated line and use that as new statement
        list_stmts.append(current_statement)
        itrateMe(current_statement, line_count, list_stmts)     
        currentIndex = currentIndex + 1
    
