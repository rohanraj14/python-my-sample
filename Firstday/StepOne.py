ip = raw_input()
print(ip)
ip = ip.split(' ')
print(ip)
operation = ip[0]
int1 = int(ip[1])
int2 = int(ip[2])
if operation == '+':
    print(int1 + int2)
if operation == '-':
    print(int1 - int2)
if operation == '*':
    print(int1 * int2)
if operation == '/':
    print(int1 / int2)
