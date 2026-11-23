import random
#This is Tic Tac Toe with another player
Grid = True
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
squares1 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares2 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares3 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares4 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares5 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares6 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares7 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares8 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
squares9 = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
table = [squares1, squares2, squares3, squares4, squares5, squares6, squares7, squares8, squares9]

        
win = "no"
def showGrid():
    print(f"""______________________________________
 {squares1[0]} | {squares1[1]} | {squares1[2]} || {squares2[0]} | {squares2[1]} | {squares2[2]} || {squares3[0]} | {squares3[1]} | {squares3[2]}
 {squares1[3]} | {squares1[4]} | {squares1[5]} || {squares2[3]} | {squares2[4]} | {squares2[5]} || {squares3[3]} | {squares3[4]} | {squares3[5]}
 {squares1[6]} | {squares1[7]} | {squares1[8]} || {squares2[6]} | {squares2[7]} | {squares2[8]} || {squares3[6]} | {squares3[7]} | {squares3[8]}
======================================
 {squares4[0]} | {squares4[1]} | {squares4[2]} || {squares5[0]} | {squares5[1]} | {squares5[2]} || {squares6[0]} | {squares6[1]} | {squares6[2]}
 {squares4[3]} | {squares4[4]} | {squares4[5]} || {squares5[3]} | {squares5[4]} | {squares5[5]} || {squares6[3]} | {squares6[4]} | {squares6[5]}
 {squares4[6]} | {squares4[7]} | {squares4[8]} || {squares5[6]} | {squares5[7]} | {squares5[8]} || {squares6[6]} | {squares6[7]} | {squares6[8]}
======================================
 {squares7[0]} | {squares7[1]} | {squares7[2]} || {squares8[0]} | {squares8[1]} | {squares8[2]} || {squares9[0]} | {squares9[1]} | {squares9[2]}
 {squares7[3]} | {squares7[4]} | {squares7[5]} || {squares8[3]} | {squares8[4]} | {squares8[5]} || {squares9[3]} | {squares9[4]} | {squares9[5]}
 {squares7[6]} | {squares7[7]} | {squares7[8]} || {squares8[6]} | {squares8[7]} | {squares8[8]} || {squares9[6]} | {squares9[7]} | {squares9[8]}""")
       
while win == "no":
    if playerturn == True:
        if Grid == True:
            Grid = input("Select a grid : ")
        else:
            print(f"You are playing in grid {Grid}")
        selected = input("Select a square : ")
        if Grid == "1":
            index = 0
            for squares in table :
                for cell in squares1: 
                    index = index + 1
                    if cell == " " and selected == str(index):
                        Grid = str(index)
                        squares1[index] = player
            showGrid()

        if Grid == "2":
            if squares2[0] == " " and selected == "1":
                squares2[0] = player
                Grid = "1"
            elif squares2[1] == " " and selected == "2":
                squares2[1] = player
                Grid = "2"
            elif squares2[2] == " " and selected == "3":
                squares2[2] = player
                Grid = "3"
            elif squares2[3] == " " and selected == "4":
                squares2[3] = player
                Grid = "4"
            elif squares2[4] == " " and selected == "5":
                squares2[4] = player
                Grid = "5"
            elif squares2[5] == " " and selected == "6":
                squares2[5] = player
                Grid = "6"
            elif squares2[6] == " " and selected == "7":
                squares2[6] = player
                Grid = "7"
            elif squares2[7] == " " and selected == "8":
                squares2[7] = player
                Grid = "8"
            elif squares2[8] == " " and selected == "9":
                squares2[8] = player
                Grid = "9"
            else:
                print("That imput is invalid")
            continue
        if Grid == "3":
            if squares3[0] == " " and selected == "1":
                squares3[0] = player
                Grid = "1"
            elif squares3[1] == " " and selected == "2":
                squares3[1] = player
                Grid = "2"
            elif squares3[2] == " " and selected == "3":
                squares3[2] = player
                Grid = "3"
            elif squares3[3] == " " and selected == "4":
                squares3[3] = player
                Grid = "4"
            elif squares3[4] == " " and selected == "5":
                squares3[4] = player
                Grid = "5"
            elif squares3[5] == " " and selected == "6":
                squares3[5] = player
                Grid = "6"
            elif squares3[6] == " " and selected == "7":
                squares3[6] = player
                Grid = "7"
            elif squares3[7] == " " and selected == "8":
                squares3[7] = player
                Grid = "8"
            elif squares3[8] == " " and selected == "9":
                squares3[8] = player
                Grid = "9"
            else:
                print("That imput is invalid")
            continue
        if Grid == "4":
            if squares4[0] == " " and selected == "1":
                squares4[0] = player
                Grid = "1"
            elif squar4s3[1] == " " and selected == "2":
                squares4[1] = player
                Grid = "2"
            elif squares4[2] == " " and selected == "3":
                squares4[2] = player
                Grid = "3"
            elif squares4[3] == " " and selected == "4":
                squares4[3] = player
                Grid = "4"
            elif squares4[4] == " " and selected == "5":
                squares4[4] = player
                Grid = "5"
            elif squares4[5] == " " and selected == "6":
                squares4[5] = player
                Grid = "6"
            elif squares4[6] == " " and selected == "7":
                squares4[6] = player
                Grid = "7"
            elif squares4[7] == " " and selected == "8":
                squares4[7] = player
                Grid = "8"
            elif squares4[8] == " " and selected == "9":
                squares4[8] = player
                Grid = "9"
            else:
                print("That imput is invalid")
            continue
        if Grid == "5":
            if squares5[0] == " " and selected == "1":
                squares3[0] = player
                Grid = "1"
            elif squar5s3[1] == " " and selected == "2":
                squares3[1] = player
                Grid = "2"
            elif squares3[2] == " " and selected == "3":
                squares5[2] = player
                Grid = "3"
            elif squares3[3] == " " and selected == "4":
                squares5[3] = player
                Grid = "4"
            elif squares3[4] == " " and selected == "5":
                squares5[4] = player
                Grid = "5"
            elif squares3[5] == " " and selected == "6":
                squares5[5] = player
                Grid = "6"
            elif squares3[6] == " " and selected == "7":
                squares5[6] = player
                Grid = "7"
            elif squares3[7] == " " and selected == "8":
                squares5[7] = player
                Grid = "8"
            elif squares3[8] == " " and selected == "9":
                squares5[8] = player
                Grid = "9"
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
#    else:
#Analyzes wich square is unoccupied
#        randChoice = []
#        for index, square in enumerate(squares):
#            if square == " ":
#                randChoice.append(index)
#Will always go for a win if it has one
#        if (squares[2] == bot and squares[1] == bot or squares[4] == bot and squares[8] == bot or squares[3] == bot and squares[6] == bot) and squares[0] == " ":
#            squares[0] = bot
#        elif (squares[2] == bot and squares[0] == bot or squares[4] == bot and squares[7] == bot) and squares[1] == " ":
#            squares[1] = bot
#        elif (squares[1] == bot and squares[0] == bot or squares[4] == bot and squares[6] == bot or squares[5] == bot and squares[8] == bot) and squares[2] == " ":
#            squares[2] = bot
#        elif (squares[6] == bot and squares[0] == bot or squares[4] == bot and squares[5] == bot) and squares[3] == " ":
#            squares[3] = bot
#        elif (squares[8] == bot and squares[0] == bot or squares[1] == bot and squares[7] == bot or squares[2] == bot and squares[6] == bot or squares[3] == bot and squares[5] == bot) and squares[4] == " ":
#            squares[4] = bot
#        elif (squares[2] == bot and squares[8] == bot or squares[4] == bot and squares[3] == bot) and squares[5] == " ":
#            squares[5] = bot
#        elif (squares[3] == bot and squares[0] == bot or squares[4] == bot and squares[2] == bot or squares[7] == bot and squares[8] == bot) and squares[6] == " ":
#            squares[6] = bot
#        elif (squares[1] == bot and squares[4] == bot or squares[6] == bot and squares[8] == bot) and squares[7] == " ":
#            squares[7] = bot
#        elif (squares[0] == bot and squares[4] == bot or squares[2] == bot and squares[5] == bot or squares[6] == bot and squares[7] == bot) and squares[8] == " ":
#            squares[8] = bot
#If it has no win, it will look for threats and stop them
#        else:
#            if (squares[2] == player and squares[1] == player or squares[4] == player and squares[8] == player or squares[3] == player and squares[6] == player) and squares[0] == " ":
#                squares[0] = bot
#            elif (squares[2] == player and squares[0] == player or squares[4] == player and squares[7] == player) and squares[1] == " ":
#                squares[1] = bot
#            elif (squares[1] == player and squares[0] == player or squares[4] == player and squares[6] == player or squares[5] == player and squares[8] == player) and squares[2] == " ":
#                squares[2] = bot
#            elif (squares[6] == player and squares[0] == player or squares[4] == player and squares[5] == player) and squares[3] == " ":
#                squares[3] = bot
#            elif (squares[8] == player and squares[0] == player or squares[1] == player and squares[7] == player or squares[2] == player and squares[6] == player or squares[3] == player and squares[5] == player) and squares[4] == " ":
#                squares[4] = bot
#            elif (squares[2] == player and squares[8] == player or squares[4] == player and squares[3] == player) and squares[5] == " ":
#                squares[5] = bot
#            elif (squares[3] == player and squares[0] == player or squares[4] == player and squares[2] == player or squares[7] == player and squares[8] == player) and squares[6] == " ":
#                squares[6] = bot
#            elif (squares[1] == player and squares[4] == player or squares[6] == player and squares[8] == player) and squares[7] == " ":
#                squares[7] = bot
#           elif (squares[0] == player and squares[4] == player or squares[2] == player and squares[5] == player or squares[6] == player and squares[7] == player) and squares[8] == " ":
#               squares[8] = bot
#If there is no win or threat, the bot will select a random square
#           else:
#                botChoice = random.choice(randChoice)
#                squares[botChoice] = bot
#        showGrid()
#        if squares[0] == bot and squares[1] == bot and squares[2] == bot or squares[3] == bot and squares[4] == bot and squares[5] == bot or squares[6] == bot and squares[7] == bot and squares[8] == bot or squares[0] == bot and squares[3] == bot and squares[6] == bot or squares[1] == bot and squares[4] == bot and squares[7] == bot or squares[2] == bot and squares[5] == bot and squares[8] == bot or squares[0] == bot and squares[4] == bot and squares[8] == bot or squares[2] == bot and squares[4] == bot and squares[6] == bot:
#            win = bot
#            break
#        if " " not in squares:
#            win = False
#            break
#        playerturn = True

#End of game
if win == False:
    print("DRAW")
else:
    print(f"{win} WINS")

