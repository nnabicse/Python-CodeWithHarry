f = open('poem.txt', 'r')
t = f.read()

if "twinkle" in t:
    print("Present")
else:
    print("Not Present")
f.close()