sub1 = int(input("Enter Marks of Subject 1: "))
sub2 = int(input("Enter Marks of Subject 2: "))
sub3 = int(input("Enter Marks of Subject 3: "))

if ((sub1+sub2+sub3)/3 >= 40):
    if(sub1>=33 and sub2>=33 and sub3>=33):
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")