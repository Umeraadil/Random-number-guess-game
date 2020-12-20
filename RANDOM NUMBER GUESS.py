import random as r
rn = r.randint(1, 10000)
g = None
gs = 0
print("GUESS NUMBER GAME BY UMER AADIL")
while(g != rn):
    g = int(input(" Guess Your Number: "))
    gs += 1
    if(g==rn):
        print("ooooooo right guess your great!")
    else:
        if(g > rn):
            print("hahahah Sorry  wrong guess!")
        else:
            print("hahaha wrong guess! enter another number ")

print(f"You guessed the number in {gs} gs")
with open("h.txt", "r") as f:
    h = int(f.read())

if(gs<h):
    print("OOOOOOOO YOU broken RECORD!")
    with open("h.txt", "w") as f:
        f.write(str(gs))
