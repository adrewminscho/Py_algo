    total = int(input())
    type = int(input())
    total_temp = 0

    for i in range(type) :
        a, b = map(int,input().split())
        temp = a*b
        total_temp = total_temp + temp

    if total == total_temp :
        print("yes")
    else :
        print("no")