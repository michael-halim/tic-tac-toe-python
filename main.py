from os import system,name
board = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']]
def clear():
    if name == 'nt':
        _ = system('cls')


def displayBoard():
    for i in range(3):
        for j in range(3):
            print(board[i][j],end = ' ')
            if j < 2:
                print(' | ',end = ' ')
            else:
                print()
        print('--------------')


def handleTurn(count,char):
    x = input(char + '\'s turn ')
    check = updateGame(int(x),char) # kalo 1 giliran x kalo 0 giliran y

    while check == 1 or int(x) > 9:
        x = input('Invalid Input, Try Again\n' + char + '\'s turn ')
        check = updateGame(int(x),char)

    count += 1
    if count >= 8: return False,count        

    results = checkGame(char) # kembalian ke [0] adalah bool kalo true artinya char yang ada di [1] menang

    if results[0]: return True,results[1]     
        
    return False,count

def checkCol():
    if (board[0][0] == board[1][0] == board[2][0]) or \
        (board[0][1] == board[1][1] == board[2][1]) or \
         (board[0][2] == board[1][2] == board[2][2]):
            return True
   

def checkRow():
    if (board[0][0] == board[0][1] == board[0][2]) or \
        (board[1][0] == board[1][1] == board[1][2]) or \
         (board[2][0] == board[2][1] == board[2][2]):
            return True
    

def checkDiag():
    if (board[0][0] == board[1][1] == board[2][2]) or \
        (board[0][2] == board[1][1] == board[2][0]):
            return True
    

def checkGame(val):
    if(checkCol() or checkRow() or checkDiag()):
        return True,val
    return False,0

def updateGame(val,char):
    if(val == 1): 
        if(board[0][0] == 'X' or board[0][0] == 'O'): return 1 # kalo sudah ditempati diulang turnnya
            
        else: board[0][0] = char # kalo ga tempati
           
    elif(val == 2):
        if(board[0][1] == 'X' or board[0][1] == 'O'): return 1
            
        else: board[0][1] = char
            
        
    elif(val == 3):
        if(board[0][2] == 'X' or board[0][2] == 'O'): return 1
            
        else: board[0][2] = char
            
              
    elif(val == 4):
        if(board[1][0] == 'X' or board[1][0] == 'O'): return 1
            
        else: board[1][0] = char
            
            
    elif(val == 5):
        if(board[1][1] == 'X' or board[1][1] == 'O'): return 1
            
        else: board[1][1] = char
            
              
    elif(val == 6):
        if(board[1][2] == 'X' or board[1][2] == 'O'): return 1
            
        else: board[1][2] = char
            
              
    elif(val == 7):
        if(board[2][0] == 'X' or board[2][0] == 'O'): return 1
            
        else: board[2][0] = char
            
              
    elif(val == 8):
        if(board[2][1] == 'X' or board[2][1] == 'O'): return 1
            
        else: board[2][1] = char
            
             
    elif(val == 9):
        if(board[2][2] == 'X' or 'O'): return 1
            
        else: board[2][2] = char
            
    displayBoard()
    return 0

def playGame():
    winner = ''
    count = 0 
    while True:
        if count % 2 == 0: char = 'X' # untuk ganti karakter
        else: char = 'O'    
            
        displayBoard()

        results = handleTurn(count,char)
        count = results[1]
        
        if(count == 9): break
                   
        if(results[0]):
            winner = results[1]
            break
        clear()

    if winner != '':
        print('Game Over !! ' + winner + ' Is The Winner')
    elif count == 9:
        print('Game Over !! It\'s a Tie')

playGame()