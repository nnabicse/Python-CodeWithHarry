def sum_rec(n):
    if n>=1:
        return sum_rec(n-1)+n
    else:
        return 0
s = sum_rec(2)
print(s)