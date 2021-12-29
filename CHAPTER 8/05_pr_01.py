def maximum(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        return b

m = maximum(10,9,50)
print(m)