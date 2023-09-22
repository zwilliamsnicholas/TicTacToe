board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

def printboard():
    #function prints the tic tac toe board
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    
player = 1;
def updateboard(player):
    move = int(input("Enter the number of the space on the board you'd like to move to."))
    move = move - 1
    while board[move] != "-":
        printboard()
        move =int(input("Invalid input. Enter the number of a space that hasn't already been taken.")) -1
    if player == 1:
            board[move] = "O";
    elif player == 2:
            board[move] = "X";
    printboard()

print("Welcome to Tic Tac Toe! Player 1 uses O, Player 2 uses X.")
endcounter = 0; #play until wincounter equals 1 
player =1; #switches betwen player 1 and 2, maybe division remainder of turnct? 
while endcounter != 1:
    #player 1 plays 
    updateboard(player); 
    #check for win
    if board[0] == board[1] == board[2]=="O" or board[3] == board[4] == board[5]=="O" or board[6] == board[7] == board[8]=="O" or board[0] == board[3] == board[6]=="O" or board[1] == board[4] == board[7]=="O" or board[2] == board[5] == board[8]=="O" or board[0] == board[4] == board[8]=="O" or board[2] == board[4] == board[6]=="O" or board[0] == board[1] == board[2]=="X" or board[3] == board[4] == board[5]=="X" or board[6] == board[7] == board[8]=="X" or board[0] == board[3] == board[6]=="X" or board[1] == board[4] == board[7]=="X" or board[2] == board[5] == board[8]=="X" or board[0] == board[4] == board[8]=="X" or board[2] == board[4] == board[6]=="X":
        print("Player", player, " wins!"); 
        endcounter = 1; 
    #elif #board is full and no more moves can be made 
    else: #change player 
        turnct = turnct+1; 
        player = turnct%2 + 1; 
        print(player);
