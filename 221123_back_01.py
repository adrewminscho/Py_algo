h, m = map(int, input().split())
m_c = m-45

if m_c >= 0 :
    print(f"{h} {m}")
else :
    h = h - 1
    m = 60 + m_c
    if h >= 0 :
        print(f"{h} {m}")
    else : 
        h = 23
        print(f"{h} {m}")