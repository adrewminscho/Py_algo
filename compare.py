#a = open('C:\Users\seoun\Desktop\Andrew\Python\test.txt','W')

col1 = [1,2,3,4,5,6,7,8,9,10]
col2 = [1,3,4,5,11]
col3 = [0,0,0,0,0,0,0,0]
re = 0

#Reference List
if len(col1) >= len(col2) :
    re = len(col1)
else : 
    re = len(col2)

print("Reference range is : {}".format(re))

j = 0
for i in range(8) :
    k = i-j
    if k == len(col2) :
        break
    
    if col1[i] != col2[i-j] :
        col3[j] = col1[i]
        j = j + 1
        print(j)

print(col3)

