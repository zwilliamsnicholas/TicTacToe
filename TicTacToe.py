board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

def printboard():
    #function prints the tic tac toe board
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    
sboard = ["1","2","3",
         "4","5","6",
         "7","8","9",]

def printsboard():
    #function prints the tic tac toe board
    print(sboard[0] + "|" + sboard[1] + "|" + sboard[2])
    print(sboard[3] + "|" + sboard[4] + "|" + sboard[5])
    print(sboard[6] + "|" + sboard[7] + "|" + sboard[8])    

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

print("Welcome to Tic Tac Toe! Player 1 uses O, Player 2 uses X. Board spaces are numbered across.")
printsboard();
endcounter = 0; #play until endcounter equals 1 
player =1; #switches betwen player 1 and 2, maybe division remainder of turnct? 
turnct =0;
while endcounter != 1:
    #player 1 plays 
    updateboard(player); 
    #check for win
    if board[0] == board[1] == board[2]=="O" or board[3] == board[4] == board[5]=="O" or board[6] == board[7] == board[8]=="O" or board[0] == board[3] == board[6]=="O" or board[1] == board[4] == board[7]=="O" or board[2] == board[5] == board[8]=="O" or board[0] == board[4] == board[8]=="O" or board[2] == board[4] == board[6]=="O" or board[0] == board[1] == board[2]=="X" or board[3] == board[4] == board[5]=="X" or board[6] == board[7] == board[8]=="X" or board[0] == board[3] == board[6]=="X" or board[1] == board[4] == board[7]=="X" or board[2] == board[5] == board[8]=="X" or board[0] == board[4] == board[8]=="X" or board[2] == board[4] == board[6]=="X":
        print("Player", player, " wins!"); 
        endcounter = 1; 
    elif board[0]!= '-' and board[1]!= '-' and board[2]!= '-' and board[3]!= '-' and board[4]!= '-' and board[5]!= '-' and board[6]!= '-' and board[7]!= '-' and board[8]!= '-':
        print("Board full. Draw!"); 
        endcounter = 1;
    else: #change player 
        turnct = turnct+1; 
        player = turnct%2 + 1; 
        print("Player", player, "'s turn!");
        
