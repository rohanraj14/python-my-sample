def return_multi_output(x, y):
    return x+y , x*y

inp= raw_input()
print(inp)
inp = inp.split(' ')
print(inp)
print(return_multi_output(int(inp[0]), int(inp[1])))
# Convert each into int??
print(return_multi_output(3, 4))

squred_odd_number = [x*x for x in range(20) if x/2 != 0]
print(squred_odd_number)
