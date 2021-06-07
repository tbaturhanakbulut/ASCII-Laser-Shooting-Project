
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
onLine = True
l = []
c=[]
time = 0
scoreCounter = 0
starDestNum = 0
for i in range (x+g+1):
    l = []
    if(i<x):
        for j in range (y):
            l.append("*")
    elif(x<=i<x+g):
        for j in range (y):
            l.append(" ")
    elif(i==x+g):
        for j in range (y):
            if(y%2==0):
                if(j==y/2-1):
                    l.append("@")
                else:
                    l.append(" ")
            else:
                if(j==int(y/2)):
                    l.append("@")
                else:
                    l.append(" ")
    c.append(l)
if(x!=0):
    for k in range(len(c)):
        for l in range(y):
            print(c[k][l], end="")
        print()
    print("------------------------------------------------------------------------")
space=0
while(onLine):
    playerPosition = c[-1].index("@")
    count = 0
    for i in range(space,x+space):
        try:
            if(c[i][playerPosition]=="*"):
                count+=1
        except:
            pass
    i = len(c) - 2
    if(x!=0):
        actionInput = input("Choose your action!\n")
        actionInput = actionInput.lower()
        if(actionInput=="exit" or actionInput=="exıt"):
            for k in range(len(c)):
                for l in range(y):
                    print(c[k][l], end="")
                print()
            print("------------------------------------------------------------------------")
            for k in range(len(c)):
                for l in range(y):
                    if(c[k][l]=="*"):
                        scoreCounter = scoreCounter + 1
            print("YOUR SCORE:",x*y-scoreCounter)
            break
        elif(actionInput=="fire" or actionInput=="fıre"):

            destCont = False
            for i in range (len(c)-2,count-1+space,-1):
                c[i][playerPosition] = "|"
                if(destCont==True):
                    c[i+1][playerPosition] = " "
                destCont=True
                for k in range(len(c)):
                    for l in range(y):
                        print(c[k][l], end="")
                    print()
                print("------------------------------------------------------------------------")
            c[i][playerPosition] = " "
            if((count!=0 and count+space<len(c)-1)):
                c[i - 1][playerPosition] = " "
                starDestNum+=1
            elif(count!=0 and count+space==len(c)-1):
                starDestNum+=1
            if (space != 0 and count == 0):
                for a in range(space, 0, -1):
                    c[a][playerPosition] = " "
                    c[a - 1][playerPosition] = "|"

                    for k in range(len(c)):
                        for l in range(y):
                            print(c[k][l], end="")
                        print()
                    print("------------------------------------------------------------------------")
                c[0][playerPosition] = " "
                if (time % 5 != 4):
                    for k in range(len(c)):
                        for l in range(y):
                            print(c[k][l], end="")
                        print()
                    print("------------------------------------------------------------------------")
            else:
                if (time % 5 != 4 and starDestNum!=x*y):
                    for k in range(len(c)):
                        for l in range(y):
                            print(c[k][l], end="")
                        print()
                    print("------------------------------------------------------------------------")
            time=time+1
        elif (actionInput == "right" or actionInput=="rıght"):
            if(playerPosition<y-1):
                c[-1][playerPosition]=" "
                c[-1][playerPosition+1]="@"
            if (time % 5 != 4):
                for k in range(len(c)):
                    for l in range(y):
                        print(c[k][l], end="")
                    print()
                print("------------------------------------------------------------------------")
            time=time+1
        elif (actionInput == "left" or actionInput=="left"):
            if (playerPosition > 0):
                c[-1][playerPosition] = " "
                c[-1][playerPosition - 1] = "@"
            if(time%5!=4 ):
                for k in range(len(c)):
                    for l in range(y):
                        print(c[k][l], end="")
                    print()
                print("------------------------------------------------------------------------")
            time=time+1
        else:
            if(time%5!=4):
                for k in range(len(c)):
                    for l in range(y):
                        print(c[k][l], end="")
                    print()
                print("------------------------------------------------------------------------")
            time=time+1
    if (starDestNum==x*y):
        print("YOU WON!")
        for k in range(len(c)):
            for l in range(y):
                print(c[k][l], end="")
            print()
        print("------------------------------------------------------------------------")
        for k in range(len(c)):
            for l in range(y):
                if (c[k][l] == "*"):
                    scoreCounter = scoreCounter + 1
        print("YOUR SCORE:",x * y - scoreCounter)
        break
    if(time%5==0 and time!=0):
        if (c[-2].count("*")!=0):
            print("GAME OVER")
            for k in range(len(c)):
                for l in range(y):
                    if (c[k][l] == "*"):
                        scoreCounter = scoreCounter + 1
            for k in range(len(c)):
                for l in range(y):
                    print(c[k][l], end="")
                print()
            print("------------------------------------------------------------------------")
            print("YOUR SCORE:", x * y - scoreCounter)
            break
        c.insert(0, [" "] * y)
        c.pop(len(c) - 2)
        space += 1
        for k in range(len(c)):
            for l in range(y):
                print(c[k][l], end="")
            print()
        print("------------------------------------------------------------------------")
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
