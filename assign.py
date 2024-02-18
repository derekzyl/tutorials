# the expected outcome is to get a input and compute it e.g 1 + 1

m = input("enter your computational value: ")

val = m.strip().split(" ")



# # experiment 
[ax,bx,cx]= val

#certain
val1= float(val[0])
compute = val[1]
val2= float(val[2])

# you dont know this yet

# match(compute):
#     case "+":
#        total= val1 + val2
#     case '-':
#         total = val1-val2
#     case '*':
#         total= val1 *val2 
#     case '/':
#         if val1 != 0:
#             total = val1/val2

if compute == '+':
    total= val1 + val2
elif compute == '-':
    total= val1 - val2
elif compute == '*':
    total= val1 * val2
elif compute == '/':
    total= val1 / val2


print(f'{cx} {ax} {bx} experimente')
print(f'total value: {total}')                           


