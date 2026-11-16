#This is base Tic Tac Toe without any opponent
player = "X"
s1 = " "
s2 = " "
s3 = " "
s4 = " "
s5 = " "
s6 = " "
s7 = " "
s8 = " "
s9 = " "
win = "no"
def showGrid():
    print(f" {s1} | {s2} | {s3}\n {s4} | {s5} | {s6}\n {s7} | {s8} | {s9}")
while win == "no":
    selected = int(input("Select a square : "))
    if s1 == " " and selected == 1:
        s1 = player
    if s2 == " " and selected == 2:
        s2 = player
    if s3 == " " and selected == 3:
        s3 = player
    if s4 == " " and selected == 4:
        s4 = player
    if s5 == " " and selected == 5:
        s5 = player
    if s6 == " " and selected == 6:
        s6 = player
    if s7 == " " and selected == 7:
        s7 = player
    if s8 == " " and selected == 8:
        s8 = player
    if s9 == " " and selected == 9:
        s9 = player
    showGrid()
    if s1 == player and s2 == player and s3 == player or s4 == player and s5 == player and s6 == player or s7 == player and s8 == player and s9 == player or s1 == player and s4 == player and s7 == player or s2 == player and s5 == player and s8 == player or s3 == player and s6 == player and s9 == player or s1 == player and s5 == player and s9 == player or s3 == player and s5 == player and s7 == player:
        win = player
        break
    if player == "X":
        player = "O"
    else:
        player = "X"
    
#End of game
print(f"{player} WINS")

