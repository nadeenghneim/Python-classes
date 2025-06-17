print("welcome to tic tac toe!")
board=[' 'for _ in range(9)]
def boardview():
    print()
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i<2:
            print("---*---*---")
    print()

def winner(player):
    wincombos=[(1,2,3),(4,5,6),(7,8,9),
               (1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for a, b,c in wincombos:
        if board[a]== board[b]==board[c]==player:
            return True
    return False


def draw():
    if " " not in board:
        print("it is a draw.")
        
def move(position,player):
    if board[position]==" ":
        board[position]==player
        return True
    return False

def position():
    while True:
        posi=input("enter your position(1,9)")
        if posi in range(9) and board[posi]==" ":
            return posi
        
        else:
            print("choose a valid position.")

def game():
    currentplayer='X'
    boardview()
    
    while True:
        print(f"player (currentplayer)'s turn")
        posi=position()
        move(position,currentplayer)
        boardview()
        if winner(currentplayer):
            print(f"player {currentplayer} wins ")
            break
        elif draw():
            print("it's a draw")
            break
game()