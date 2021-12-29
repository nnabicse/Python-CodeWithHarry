import random
def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == "S":
        if you == "W":
            return False
        elif you == "G":
            return True
    elif comp == "W":
        if you == "G":
            return False
        elif you == "S":
            return True
    elif comp == "G":
        if you == "W":
            return False
        elif you == "S":
            return True


print("Computer Turn: Snake(s), Water(W), Gun(G)")
randno = random.randint(1, 3)

if randno == 1:
    comp = 'S'
elif randno == 2:
    comp = "W"
elif randno == 3:
    comp = "G"
else:
    print("Invalid Input")

you = input("Your Turn: Snake(s), Water(W), Gun(G)")
a = gamewin(comp,you)

print(f"Comp Chose {comp}")
print(f"You Chose {you}")

if a == None:
    print("Tie")
elif a == True:
    print("You Win")

elif a == False:
    print("You Lose")
