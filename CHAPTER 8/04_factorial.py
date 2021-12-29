# n! = 1*2*3*....n
'''
n=4
product = 1
for i in range(n):
    product = product*(i+1)
print(product)
'''
'''
def fact(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return product

f = fact(5)
print(f)
'''

def fact_rec (n):
    if n==1 or n==0:
        return 1
    return n*fact_rec(n-1)
f = fact_rec(5)
print(f)