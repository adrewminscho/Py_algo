num = int(input())


for i in range(num) :
    y = ' '*(num-i-1)
    x = x + '*'
    print(f"{y}{x}")