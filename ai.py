from copy import deepcopy
import random
def win(gridarray):
    for i in range(6):
        for j in range(3):
            if(gridarray[i][j]==gridarray[i][j+1] and gridarray[i][j]==gridarray[i][j+2] and gridarray[i][j]==gridarray[i][j+3]):
                if(gridarray[i][j]!=''):
                    return gridarray[i][j];
    for i in range(3):
        for j in range(6):
            if(gridarray[i][j]==gridarray[i+1][j] and gridarray[i][j]==gridarray[i+2][j] and gridarray[i][j]==gridarray[i+3][j]):
                if (gridarray[i][j] != ''):
                    return gridarray[i][j];
    for i in range(3):
        for j in range(3):
            if(gridarray[i][j]==gridarray[i+1][j+1] and gridarray[i][j]==gridarray[i+2][j+2] and gridarray[i][j]==gridarray[i+3][j+3]):
                if(gridarray[i][j]!=''):
                    return gridarray[i][j];
    for i in range(3):
        for j in range(3):
            if(gridarray[5-i][j]==gridarray[4-i][j+1] and gridarray[5-i][j]==gridarray[3-i][j+2] and gridarray[5-i][j]==gridarray[2-i][j+3]):
                if (gridarray[5-i][j] != ''):
                    return gridarray[5-i][j];
    allfill=True
    for i in range(6):
        for j in range(6):
            if(gridarray[i][j]==""):
                allfill=False
    if(allfill==True):
        return -2
    return -1;
def pointstotal(name,gridarray):
    count=0
    if(win(gridarray)==name):
        count+=10000000000000000000
        return count
    for i in range(6):
        for j in range(6):
            tcount=0
            r=0
            for k in range(6-j):
                if(gridarray[i][j+k]==name):
                    tcount+=1
                else:
                    r=k
                    break
            if(j==0):
                if(gridarray[i][j+r]!=""):
                    continue
            else:
                if (gridarray[i][j - 1] == name):
                    continue
                if(gridarray[i][j+r]!="" and gridarray[i][j-1]!=""):
                    continue
            count+=tcount**2
    for i in range(6):
        for j in range(6):
            tcount=0
            r=0
            for k in range(6-i):
                if(gridarray[i+k][j]==name):
                    tcount+=1
                else:
                    r=k
                    break
            if(i==0):
                if(gridarray[i+r][j]!=""):
                    continue
            else:
                if (gridarray[i-1][j] == name):
                    continue
                if(gridarray[i+r][j]!="" and gridarray[i-1][j]!=""):
                    continue
            count+=tcount**2
    for i in range(6):
        for j in range(6):
            tcount=0
            r=0
            for k in range(6-max(i,j)):
                if(gridarray[i+k][j+k]==name):
                    tcount+=1
                else:
                    r=k
                    break
            if(i==0 or j==0):
                if(gridarray[i+r][j+r]!=""):
                    continue
            else:
                if (gridarray[i-1][j-1] == name):
                    continue
                if(gridarray[i+r][j+r]!="" and gridarray[i-1][j-1]!=""):
                    continue
            count+=tcount**2
    for i in range(6):
        i=5-i
        for j in range(6):
            tcount=0
            r=0
            for k in range(6-max(i,j)):
                if(gridarray[i+k][j+k]==name):
                    tcount+=1
                else:
                    r=k
                    break
            if(i==0 or j==0):
                if(gridarray[i+r][j+r]!=""):
                    continue
            else:
                if (gridarray[i-1][j-1] == name):
                    continue
                if(gridarray[i+r][j+r]!="" and gridarray[i-1][j-1]!=""):
                    continue
            count+=tcount**2
    return count
def draw(gridarray):
    for i in range(6):
        stringo=" "
        for j in range(6):
            if(gridarray[i][j]==""):
                stringo+="+"
            else:
                stringo+=gridarray[i][j]
        print(stringo)
def turn(player,row,gridarra,Candraw):
    for i in range(6):
        if(gridarra[5-i][row]==""):
            gridarra[5-i][row]=player
            break
    if(Candraw):
        draw(gridarra)
        print("")
    return gridarra
def ai_move(gridarray,color,opcolor,depth):
    move_val=-100000000000000
    move=0
    innerarray = deepcopy(gridarray)
    if(depth==-1):
        return(random.randint(0,5),0)
    elif(depth==0):
        for i in range(6):
            if(gridarray[0][i]!=''):
                continue
            innerarray=turn(color,i,innerarray,False)
            score=(pointstotal(color, innerarray)-pointstotal(opcolor,innerarray))
            if move_val < (pointstotal(color, innerarray)-pointstotal(opcolor,innerarray)):
                move_val=score
                move=i
            innerarray=deepcopy(gridarray)
    else:
        move_val=-1000000000000000000*((-1)**depth)
        for i in range(6):
            if (gridarray[0][i] != ''):
                continue
            if(depth%2==0):
                innerarray=turn(color,i,innerarray,False)
                place,score=ai_move(innerarray,opcolor,color,depth-1)
                if (win(innerarray) == color):
                    return (i, 190990990988777)
                if move_val<score:
                    move_val=score
                    move=i
            if (depth % 2 == 1):
                innerarray = turn(color, i, innerarray, False)
                if(win(innerarray)==color):
                    return (i,-190990990988777)
                place, score = ai_move(innerarray, opcolor, color, depth - 1)
                if move_val > score:
                    move_val = score
                    move = i
            innerarray=deepcopy(gridarray)

    return (move,move_val)

gridarray=[['','','','','',''],['','','','','',''],['','','','','',''],['','','','','',''],['','','','','',''],['','','','','','']]
print(pointstotal('1',gridarray))

