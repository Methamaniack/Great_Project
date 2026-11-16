import random
#This is Tic Tac Toe with another player
bot = "O"

bot = input("Type anything to play against a bot. If not, just press ENTER. ")
if bot != "":
    bot = "O"
    
player = "X"
squares = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

squares[0] = " "
squares[1] = " "
squares[2] = " "
squares[3] = " "
squares[4] = " "
squares[5] = " "
squares[6] = " "
squares[7] = " "
squares[8] = " "
win = "no"
def showGrid():
    print(f"___________\n {squares[0]} | {squares[1]} | {squares[2]}\n {squares[3]} | {squares[4]} | {squares[5]}\n {squares[6]} | {squares[7]} | {squares[8]}")
while win == "no":
    selected = int(input("Select a square : "))
    if squares[0] == " " and selected == 1:
        squares[0] = player
    if squares[1] == " " and selected == 2:
        squares[1] = player
    if squares[2] == " " and selected == 3:
        squares[2] = player
    if squares[3] == " " and selected == 4:
        squares[3] = player
    if squares[4] == " " and selected == 5:
        squares[4] = player
    if squares[5] == " " and selected == 6:
        squares[5] = player
    if squares[6] == " " and selected == 7:
        squares[6] = player
    if squares[7] == " " and selected == 8:
        squares[7] = player
    if squares[8] == " " and selected == 9:
        squares[8] = player
    showGrid()
#Checks for 3 in a row
    if squares[0] == player and squares[1] == player and squares[2] == player or squares[3] == player and squares[4] == player and squares[5] == player or squares[6] == player and squares[7] == player and squares[8] == player or squares[0] == player and squares[3] == player and squares[6] == player or squares[1] == player and squares[4] == player and squares[7] == player or squares[2] == player and squares[5] == player and squares[8] == player or squares[0] == player and squares[4] == player and squares[8] == player or squares[2] == player and squares[4] == player and squares[6] == player:
        win = player
        break
#Alternates players turn and verifies if bot is on
    if bot == "":
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
#Analyzes wich square is unoccupied
        randChoice = []
        for index, square in enumerate(squares):
            if square == " ":
                randChoice.append(index)
#Will always go for a win if it has one
        if (squares[2] == "O" and squares[1] == "O" or squares[4] == "O" and squares[8] == "O" or squares[3] == "O" and squares[6] == "O") and squares[0] == " ":
            squares[0] = "O"
        elif (squares[2] == "O" and squares[0] == "O" or squares[4] == "O" and squares[7] == "O") and squares[1] == " ":
            squares[1] = "O"
        elif (squares[1] == "O" and squares[0] == "O" or squares[4] == "O" and squares[6] == "O" or squares[5] == "O" and squares[8] == "O") and squares[2] == " ":
            squares[2] = "O"
        elif (squares[6] == "O" and squares[0] == "O" or squares[4] == "O" and squares[5] == "O") and squares[3] == " ":
            squares[3] = "O"
        elif (squares[8] == "O" and squares[0] == "O" or squares[1] == "O" and squares[7] == "O" or squares[2] == "O" and squares[6] == "O" or squares[3] == "O" and squares[5] == "O") and squares[4] == " ":
            squares[4] = "O"
        elif (squares[2] == "O" and squares[8] == "O" or squares[4] == "O" and squares[3] == "O") and squares[5] == " ":
            squares[5] = "O"
        elif (squares[3] == "O" and squares[0] == "O" or squares[4] == "O" and squares[2] == "O" or squares[7] == "O" and squares[8] == "O") and squares[6] == " ":
            squares[6] = "O"
        elif (squares[1] == "O" and squares[4] == "O" or squares[6] == "O" and squares[8] == "O") and squares[7] == " ":
            squares[7] = "O"
        elif (squares[0] == "O" and squares[4] == "O" or squares[2] == "O" and squares[5] == "O" or squares[6] == "O" and squares[7] == "O") and squares[8] == " ":
            squares[8] = "O"
#If it has no win, it will look for threats and stop them
        else:
            if (squares[2] == player and squares[1] == player or squares[4] == player and squares[8] == player or squares[3] == player and squares[6] == player) and squares[0] == " ":
                squares[0] = "O"
            elif (squares[2] == player and squares[0] == player or squares[4] == player and squares[7] == player) and squares[1] == " ":
                squares[1] = "O"
            elif (squares[1] == player and squares[0] == player or squares[4] == player and squares[6] == player or squares[5] == player and squares[8] == player) and squares[2] == " ":
                squares[2] = "O"
            elif (squares[6] == player and squares[0] == player or squares[4] == player and squares[5] == player) and squares[3] == " ":
                squares[3] = "O"
            elif (squares[8] == player and squares[0] == player or squares[1] == player and squares[7] == player or squares[2] == player and squares[6] == player or squares[3] == player and squares[5] == player) and squares[4] == " ":
                squares[4] = "O"
            elif (squares[2] == player and squares[8] == player or squares[4] == player and squares[3] == player) and squares[5] == " ":
                squares[5] = "O"
            elif (squares[3] == player and squares[0] == player or squares[4] == player and squares[2] == player or squares[7] == player and squares[8] == player) and squares[6] == " ":
                squares[6] = "O"
            elif (squares[1] == player and squares[4] == player or squares[6] == player and squares[8] == player) and squares[7] == " ":
                squares[7] = "O"
            elif (squares[0] == player and squares[4] == player or squares[2] == player and squares[5] == player or squares[6] == player and squares[7] == player) and squares[8] == " ":
                squares[8] = "O"
#If there is no win or threat, the bot will select a random square
            else:
                botChoice = random.choice(randChoice)
                squares[botChoice] = "O"
        showGrid()
        if squares[0] == bot and squares[1] == bot and squares[2] == bot or squares[3] == bot and squares[4] == bot and squares[5] == bot or squares[6] == bot and squares[7] == bot and squares[8] == bot or squares[0] == bot and squares[3] == bot and squares[6] == bot or squares[1] == bot and squares[4] == bot and squares[7] == bot or squares[2] == bot and squares[5] == bot and squares[8] == bot or squares[0] == bot and squares[4] == bot and squares[8] == bot or squares[2] == bot and squares[4] == bot and squares[6] == bot:
            win = bot
            break

#End of game
print(f"{win} WINS")

