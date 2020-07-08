import random

print("*******************TIC_TAC_TOE**********************")
# making a list of static variable
game_input =["null","x","0","x","0","x","0","x","0","x"]
#board infrastructure
def board(game_input):
   print(game_input[7]+"|"+game_input[8]+"|"+game_input[9])
   print(game_input[4]+"|"+game_input[5]+"|"+game_input[6])
   print(game_input[1]+"|"+game_input[2]+"|"+game_input[3])
#board(game_input)
#assigning the markerb to players
def player_input():
    marker=""
    while marker!="x" and marker!="0":
     marker = input("player1: please enter your choice x or 0")
    if marker=="x":
        return("x","0")
    else:
        return("0","x")

#player_input()
#player1,player2=player_input()
#print(player1)
#print(player2)
#marking the values at position on game_input
def put_marker(game_input,marker,position):
    game_input[position]= marker


#winning critarea:)
def win(marker,game_inut):

    return ((game_input[1]==game_input[2]==game_input[3]==marker) or
           (game_input[4] == game_input[5] == game_input[6] == marker) or
           (game_input[7]==game_input[8]==game_input[9]==marker) or
           (game_input[7]==game_input[4]==game_input[1]== marker) or
           (game_input[8]==game_input[5]==game_input[2]==marker) or
           (game_input[9]==game_input[6]==game_input[3]==marker) or
           (game_input[7]==game_input[5]==game_input[3]==marker) or
           (game_input[9]==game_input[5]==game_input[1]==marker))

#randomly choosing the player:)
def choose_player():
    player= random.randint(1,2)  #random.randint is a function which will ramdomly select value
    if(player==1):
        return "player 1"
    else:
        return "player 2"
#function to verify that only vacant space can write the marker but not to overwrite
def check(game_input,position):
    return game_input[position]==" "

#function to check that either full board is empty
def check_fullboard(game_input):
    for i in range(1,10):
        if check(game_input,i):
            return False

    return True

#placee the marker according to player choice
def player_choice(game_input):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not check(game_input,position):
        position = int(input("please choose ur position(1-9) on board:"))
    return position

#ask if they want to play again
def play_again():
    choice=input("would you like to play again [Y/N]:")
    return choice=="Y"

#GAME MEHANIC
while True:
    the_board=[" "]*10
    player1,player2=player_input()
    print(player1  +  "is the sign of player1")
    print(player2  + "is the sign of player2")

    turn= choose_player()
    print(turn + "will play first")

    play_game=input("are you ready to play[Y/N]")
    if play_game=="Y":
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn== "player1":

           board(the_board)
           position= player_choice(the_board)
           put_marker(the_board,player1,position)
           if win(the_board,player1):
               board(the_board)
               print("PLAYER1 HAS WON THE GAME CONGRATULATIONS!!!!!!!!!!")
               game_on=False
           else:
               if check_fullboard(the_board):
                   board(the_board)
                   print("!!THE GAME IS TIE!!")
                   game_on = False
               else:
                   turn="player2"

        else:
            board(the_board)
            position = player_choice(the_board)
            put_marker(the_board, player2, position)
            if win(the_board, player2):
                board(the_board)
                print("PLAYER2 HAS WON THE GAME CONGRATULATIONS!!!!!!!!!!")
                game_on = False
            else:
                if check_fullboard(the_board):
                    board(the_board)
                    print("!!THE GAME IS TIE!!")
                    game_on = False
                else:
                    turn = "player1"

    if not play_again():
        break

