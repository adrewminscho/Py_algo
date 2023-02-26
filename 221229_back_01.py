x = int(input())
num = 0
temp = 0
d = x
if x < 100 and x > 0 :
    while 1 :
        if temp == x :
            break
    
        temp = d
        num = num+1
        a = temp//10
        b = temp%10
        c = a + b
        if c > 9 :
            c = c%10
        d = 10*b + c
        temp = d
    

    print(num)