import sys
num = int(input())

for i in range(num) :
    a,b = map(int,sys.stdin.readline().split())
    c = a + b
    print(f"Case #{i+1}: {c}")