a,b =  map(int, input().split())
c=[a+b,a-b,a*b,a/b,a%b]
c = map(int, c)
for i in c :
    print(f"{i}")