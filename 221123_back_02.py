h,m = map(int, input().split())
c = int(input())

m_c = m+c

if m_c >= 60 :
    h = h + m_c//60
    m = m_c%60
    if h >= 24 : 
        h = h-24
        print(f"{h} {m}")
    else :
        print(f"{h} {m}")
else : 
    print(f"{h} {m_c}")