import sys

while True :
    a,b = map(int,sys.stdin.readline().split())
    if a > 10 or a < 0 or b > 10 or b < 0 :
        break
    c = a + b
    print(c)
    
    