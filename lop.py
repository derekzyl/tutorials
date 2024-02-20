total = []

for precious in range(10):
    x = input(f"insert a grocery list: {precious +1 } of 10  ")
    if(x.isalpha()):
        total.append(x)

total.sort()


print(f'the sorted list:  {total}')     