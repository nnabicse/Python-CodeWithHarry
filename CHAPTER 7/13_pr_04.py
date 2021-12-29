num = int(input("Enter Number: "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
    else:
        prime = True
    break

if prime:
    print("Prime")
else:
    print("Not Prime")
