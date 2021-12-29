def game():
    return 666

score = game()

with open('score.txt') as f:
    hscorestr = f.read()

if hscorestr== "":
    with open('score.txt',"w") as f:
        f.write(str(score))

elif int(hscorestr)<score:
    with open('score.txt',"w") as f:
        f.write(str(score))