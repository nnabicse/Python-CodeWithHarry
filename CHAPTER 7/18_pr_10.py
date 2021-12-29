num = int(input("Enter Number: "))
mullist = []
for i in range(1,11):
    #print(str(num) + "X" + str(i) + "=" + str(i*num) )
    mullist.append(num*i)
mullist.reverse()
print(mullist)