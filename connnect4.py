import ai
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
def draw(gridarray):
    for i in range(6):
        stringo=" "
        for j in range(6):
            if(gridarray[i][j]==""):
                stringo+="+"
            else:
                stringo+=str(gridarray[i][j])
            stringo+=" "
        print(stringo)
def turn(player,row,gridarra,Candraw):
    for i in range(6):
        if(gridarra[5-i][row]==""):
            gridarra[5-i][row]=player
            break
    else:
        return 0
    if(Candraw):
        draw(gridarra)
        print("")
    return gridarra
keys={}
player1=input()
if(player1!="human"):
    keys[1]=int(player1)
else:
    keys[1]="human"
player2=input()
if (player2 != "human"):
    keys[0] = int(player2)
else:
    keys[0]="human"
turnC=1
gridarray=[['','','','','',''],['','','','','',''],['','','','','',''],['','','','','',''],['','','','','',''],['','','','','','']]
print(keys)
while(win(gridarray)<0):
    player=turnC%2
    if(keys[player]=="human"):
        move=int(input())
        if(turn(player,move,gridarray,True)==0):
            turnC-=1
    else:
        move=ai.ai_move(gridarray,player,(player+1)%2,keys[player])
        turn(player, move[0], gridarray,True)
    turnC+=1
print(win(gridarray))