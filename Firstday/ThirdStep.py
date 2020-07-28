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
            append_new_line(os.path.abspath('Firstday/OutputStep3.txt'), 'Already reached once : '+ new_statement)
           

def append_new_line(file_name, text_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as f:
        # Move read cursor to the start of file.
        f.seek(0)
        # If not empty file then enter new line
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        # Append the text at end of file
        f.write(text_append)


with open(os.path.abspath('Firstday/input2.txt'), 'r') as calculator:
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
    
