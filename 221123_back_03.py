a,b,c = map(int,input().split())

if a == b == c :
    x = 10000 + a*1000
    print(x)
elif a == b or a == c or b == c :
    if a == b or a == c :
        x = 1000 + 100*a
        print(x)
    else :
        x = 1000 + 100*b
        print(x)
elif a != b != c :
    x = [a, b, c]
    y = max(x)
    x = 100*y
    print(x)
