import random
#This is Tic Tac Toe with another player
win = "X"
bot = "O"
player = "X"
playerturn = True
bot = input("Type anything to play against a bot. If not, just press ENTER. ")
if bot != "":
    bot = input("Does the bot go first or last ? (1 or 2) ")
    if bot == "1":
        bot = "X"
        player = "O"
        playerturn = False
    elif bot == "2":
        bot = "O"
        player = "X"
        playerturn = True
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
    if playerturn == True:
        selected = input("Select a square : ")
        if squares[0] == " " and selected == "1":
            squares[0] = player
        elif squares[1] == " " and selected == "2":
            squares[1] = player
        elif squares[2] == " " and selected == "3":
            squares[2] = player
        elif squares[3] == " " and selected == "4":
            squares[3] = player
        elif squares[4] == " " and selected == "5":
            squares[4] = player
        elif squares[5] == " " and selected == "6":
            squares[5] = player
        elif squares[6] == " " and selected == "7":
            squares[6] = player
        elif squares[7] == " " and selected == "8":
            squares[7] = player
        elif squares[8] == " " and selected == "9":
            squares[8] = player
        else:
            print("That imput is invalid")
            continue
        showGrid()
#Checks for 3 in a row
    if squares[0] == player and squares[1] == player and squares[2] == player or squares[3] == player and squares[4] == player and squares[5] == player or squares[6] == player and squares[7] == player and squares[8] == player or squares[0] == player and squares[3] == player and squares[6] == player or squares[1] == player and squares[4] == player and squares[7] == player or squares[2] == player and squares[5] == player and squares[8] == player or squares[0] == player and squares[4] == player and squares[8] == player or squares[2] == player and squares[4] == player and squares[6] == player:
        win = player
        break
    if " " not in squares:
        win = False
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
        if (squares[2] == bot and squares[1] == bot or squares[4] == bot and squares[8] == bot or squares[3] == bot and squares[6] == bot) and squares[0] == " ":
            squares[0] = bot
        elif (squares[2] == bot and squares[0] == bot or squares[4] == bot and squares[7] == bot) and squares[1] == " ":
            squares[1] = bot
        elif (squares[1] == bot and squares[0] == bot or squares[4] == bot and squares[6] == bot or squares[5] == bot and squares[8] == bot) and squares[2] == " ":
            squares[2] = bot
        elif (squares[6] == bot and squares[0] == bot or squares[4] == bot and squares[5] == bot) and squares[3] == " ":
            squares[3] = bot
        elif (squares[8] == bot and squares[0] == bot or squares[1] == bot and squares[7] == bot or squares[2] == bot and squares[6] == bot or squares[3] == bot and squares[5] == bot) and squares[4] == " ":
            squares[4] = bot
        elif (squares[2] == bot and squares[8] == bot or squares[4] == bot and squares[3] == bot) and squares[5] == " ":
            squares[5] = bot
        elif (squares[3] == bot and squares[0] == bot or squares[4] == bot and squares[2] == bot or squares[7] == bot and squares[8] == bot) and squares[6] == " ":
            squares[6] = bot
        elif (squares[1] == bot and squares[4] == bot or squares[6] == bot and squares[8] == bot) and squares[7] == " ":
            squares[7] = bot
        elif (squares[0] == bot and squares[4] == bot or squares[2] == bot and squares[5] == bot or squares[6] == bot and squares[7] == bot) and squares[8] == " ":
            squares[8] = bot
#If it has no win, it will look for threats and stop them
        else:
            if (squares[2] == player and squares[1] == player or squares[4] == player and squares[8] == player or squares[3] == player and squares[6] == player) and squares[0] == " ":
                squares[0] = bot
            elif (squares[2] == player and squares[0] == player or squares[4] == player and squares[7] == player) and squares[1] == " ":
                squares[1] = bot
            elif (squares[1] == player and squares[0] == player or squares[4] == player and squares[6] == player or squares[5] == player and squares[8] == player) and squares[2] == " ":
                squares[2] = bot
            elif (squares[6] == player and squares[0] == player or squares[4] == player and squares[5] == player) and squares[3] == " ":
                squares[3] = bot
            elif (squares[8] == player and squares[0] == player or squares[1] == player and squares[7] == player or squares[2] == player and squares[6] == player or squares[3] == player and squares[5] == player) and squares[4] == " ":
                squares[4] = bot
            elif (squares[2] == player and squares[8] == player or squares[4] == player and squares[3] == player) and squares[5] == " ":
                squares[5] = bot
            elif (squares[3] == player and squares[0] == player or squares[4] == player and squares[2] == player or squares[7] == player and squares[8] == player) and squares[6] == " ":
                squares[6] = bot
            elif (squares[1] == player and squares[4] == player or squares[6] == player and squares[8] == player) and squares[7] == " ":
                squares[7] = bot
            elif (squares[0] == player and squares[4] == player or squares[2] == player and squares[5] == player or squares[6] == player and squares[7] == player) and squares[8] == " ":
                squares[8] = bot
#If there is no win or threat, the bot will select a random square
            else:
                botChoice = random.choice(randChoice)
                squares[botChoice] = bot
        showGrid()
        if squares[0] == bot and squares[1] == bot and squares[2] == bot or squares[3] == bot and squares[4] == bot and squares[5] == bot or squares[6] == bot and squares[7] == bot and squares[8] == bot or squares[0] == bot and squares[3] == bot and squares[6] == bot or squares[1] == bot and squares[4] == bot and squares[7] == bot or squares[2] == bot and squares[5] == bot and squares[8] == bot or squares[0] == bot and squares[4] == bot and squares[8] == bot or squares[2] == bot and squares[4] == bot and squares[6] == bot:
            win = bot
            break
        if " " not in squares:
            win = False
            break
        playerturn = True

#End of game
if win == False:
    print("DRAW")
else:
    print(f"{win} WINS")

