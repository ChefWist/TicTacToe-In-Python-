from random import randint
Top = [0,0,0]
Middle = [0,0,0]
Bottom = [0,0,0]
def Render():
    Game = [Top,Middle,Bottom]
    for i in Game:
        print(i, end="")
        print(" ")
def askRow():
    row = 0
    try:
        row = int(input("Which row? [left-right] (1-3): "))
        if row > 3 or row < 1:
            print("Pick A Number in the range!")
            return False
        

        return row
    
    except ValueError:
        print("Pick a number")
        return False
def askCollum():
    Collum = 0
    try:
        Collum = int(input("Which Collum? [Up-Down] (1-3): "))
        if Collum > 3 or Collum < 1:
            print("Pick A Number in the range!")
            return False
        return Collum
    except ValueError:
        print("Pick a number")
        return False
def RobotRow():
    return randint(1,3)
def RobotCollum():
    return randint(1,3)

def place(row,collum,player):
    if collum == 1 and Top[row] == 0:
         Top[row] = player
    elif collum == 2 and Middle[row] == 0:
         Middle[row] = player
    elif collum == 3 and Bottom[row] == 0:
         Bottom[row] = player

def CheckWin(player):
    if Top == [player,player,player] or Middle == [player,player,player] or Bottom == [player,player,player]:
        printWin(player)
        return True
    elif Top[0] == player and Middle[0] == player and Bottom[0] == player:
        printWin(player)
        return True
    elif Top[1] == player and Middle[1] == player and Bottom[1] == player:
        printWin(player)
        return True
    elif Top[2] == player and Middle[2] == player and Bottom[2] == player:
        printWin(player)
        return True
    elif Top[0] == player and Middle[1] == player and Bottom[2]:
        printWin(player)
        return True
    elif Top[2] == player and Middle[1] == player and Bottom[0]:
        printWin(player)
        return True
    else:
        return False
def printWin(winner):
    if winner == 1:
        print("You Won!")
    elif winner == 2:
        print("You Lost!")

running = True
while running:
    Render()
    if CheckWin(1):
        break
    
    if CheckWin(2):
        break
    if not(0 in Top and 0 in Middle and 0 in Bottom):
        print("Draw!")
        break
    accepted = False
    while accepted == False:
        accepted = askRow()
    row = accepted - 1
    accepted = False
    while accepted == False:
        accepted = askCollum()
    collum = accepted
    place(row,collum,1)
    row = RobotRow() - 1
    collum = RobotCollum()
    place(row,collum,2)
