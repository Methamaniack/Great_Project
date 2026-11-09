#This is base Tic Tac Toe without any opponent
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
        s1 = "X"
    if s2 == " " and selected == 2:
        s2 = "X"
    if s3 == " " and selected == 3:
        s3 = "X"
    if s4 == " " and selected == 4:
        s4 = "X"
    if s5 == " " and selected == 5:
        s5 = "X"
    if s6 == " " and selected == 6:
        s6 = "X"
    if s7 == " " and selected == 7:
        s7 = "X"
    if s8 == " " and selected == 8:
        s8 = "X"
    if s9 == " " and selected == 9:
        s9 = "X"
    showGrid()
    if s1 == "X" and s2 == "X" and s3 == "X" or s4 == "X" and s5 == "X" and s6 == "X" or s7 == "X" and s8 == "X" and s9 == "X" or s1 == "X" and s4 == "X" and s7 == "X" or s2 == "X" and s5 == "X" and s8 == "X" or s3 == "X" and s6 == "X" and s9 == "X" or s1 == "X" and s5 == "X" and s9 == "X" or s3 == "X" and s5 == "X" and s7 == "X":
        win = "X"
        break
    
#End of game
if win == "X":
    print("YOU WIN")

