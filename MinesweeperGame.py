"""
Minesweeper
By: Javier Ruiz-Arduengo
Begin Date: 05/06/2014
End Date: 14/06/2014
"""
#raymond_ho@durham.edu.on.ca

import random

#global variable
grid = []
   

def createboard (row,col,dispBoard):

    #CREATE EMPTY NUMBER BOARD
    for r in range (0,row):
        grid.append ([])
        for c in range (0,col):
                grid[r]. append (0)

     #INITIALIZE EMPTY DISPLAY BOARD
    for r in range (0,row):
        dispBoard.append ([])
        for c in range (0,col):      #IF board is empty, initialize
            dispBoard[r]. append ('X')
    return 

def assignbombs (row,col,numMines):
    minesPlaced = 0
    #INSERT MINES AT RANDOM LOCATIONS            
    while minesPlaced != numMines:
        #Generate x and y coordinates for Bombs
        minePlaceCol = random.randint (0, col-1)
        minePlaceRow = random.randint (0,row-1)
        
        if grid [minePlaceRow][minePlaceCol] != -1:
            grid [minePlaceRow][minePlaceCol] = -1
            minesPlaced = minesPlaced + 1        #Update number of bombs placed
    return

def mineindicator (row,col):
    for r in range (0,row):
        for c in range (0,col):
            minecount = 0           #SET/RESET MINECOUNT BACK TO 0
            if c > 0:
                if (grid [r][c-1] == -1):       #Check Left
                    minecount = minecount + 1
                if r > 0:
                    if (grid [r-1][c-1] == -1): #Check Top left
                        minecount = minecount + 1
            if r > 0:                           
                if (grid[r-1][c] == -1):        #Check Up
                    minecount = minecount + 1
                if c < col-1:                                   #(col-1 b/c it does 0-4 if col is 5.
                    if (grid[r-1][c+1] == -1): #Check Top Right
                        minecount = minecount + 1
            if c < col-1:
                if (grid[r][c+1] == -1):        #Check Right
                    minecount = minecount + 1
                if r < row-1:
                    if (grid[r+1][c+1] == -1):  #Check Bottom Right
                        minecount = minecount + 1
            if r < row-1:
                if (grid[r+1][c] == -1):        #Check Down
                    minecount = minecount + 1
                if c > 0:
                    if (grid[r+1][c-1] == -1):  #Check Bottom Left
                        minecount = minecount + 1
            if grid[r][c] != -1:        #If it isnt a bomb,determine mines around
                grid[r][c] = minecount
    return

    
#Display Board
def displayBoard(row,col,dispBoard):
    numString = ' '
    s = ''
    
    #Display x - range
    for i in range (0,col):
        numString = numString + ' ' + str(i)
    print (numString)
    
    #Display Board
    for r in range (0,row):
        s = str (r)
        for c in range (0,col):
            s  = s + ' ' + dispBoard[r][c]
        print(s)    
    return 


def uncoversquares(xcoord,ycoord,row,col,bomb,dispBoard):
    #grid[row][column]
    #dispBoard[row][column]
    #IF THERE IS A MINE INDICATOR, DISPLAY IT
    if dispBoard[ycoord][xcoord] == 'F':
        return
    
    # If the square is already revealed then dont go over it again
    elif dispBoard[ycoord][xcoord] != 'X':
        return 
        
    elif grid[ycoord][xcoord] > 0:
        dispBoard[ycoord][xcoord] = str(grid[ycoord][xcoord])
        return
    elif grid[ycoord][xcoord] == 0:
        dispBoard[ycoord][xcoord] = '-'
        #RECURSION
        if (xcoord > 0):
            if (grid[ycoord][xcoord-1] >= 0):       #Check Left
                uncoversquares(xcoord-1,ycoord,row,col,bomb,dispBoard)
            if (ycoord>0):
                if (grid[ycoord-1][xcoord-1] >= 0): #Check Top Left
                    uncoversquares (xcoord-1,ycoord-1,row,col,bomb,dispBoard)
        if (ycoord > 0):
            if (grid[ycoord-1][xcoord] >= 0):       #Check UP
                uncoversquares(xcoord,ycoord-1,row,col,bomb,dispBoard)
                if (xcoord < col - 1):
                    if grid[ycoord-1][xcoord +1] >= 0:  #Check Top Right
                        uncoversquares(xcoord+1,ycoord-1,row,col,bomb,dispBoard)     
        if (xcoord < col-1):
            if (grid[ycoord][xcoord+1] >= 0):       #Check Right
                uncoversquares(xcoord + 1,ycoord,row,col,bomb,dispBoard)
            if (ycoord <row-1):
                if grid[ycoord+1][xcoord+1] >= 0:   #Check Bottom Right
                    uncoversquares(xcoord+1,ycoord+1,row,col,bomb,dispBoard)
                        
        if (ycoord < row-1):
            if (grid[ycoord+1][xcoord] >= 0):       #Check Down
                uncoversquares(xcoord, ycoord+1,row,col,bomb,dispBoard)
            if (xcoord > 0):
                if (grid[ycoord+1][xcoord-1] >= 0): #Check Bottom Left
                   uncoversquares(xcoord-1,ycoord+1,row,col,bomb,dispBoard)
        return
                
    elif grid[ycoord][xcoord] == -1:        #IF Location picked is a bomb
        dispBoard[ycoord][xcoord] = '*'
        return
            
         
def pcol ():
    pcol =  int(input('Enter the column: '))
    return pcol

def prow():
    prow =  int(input('Enter the row: '))
    return prow
     
def gameoptions(row,col,bomb,dispBoard):
    
    decision = input('Would you like to flag or reveal a square?(F-Flag,R-Reveal): ')
    if (decision == 'F'):
        xcoord = pcol()
        ycoord = prow()
        dispBoard[ycoord][xcoord] = 'F'
    elif (decision =='R'):
        xcoord = pcol()
        ycoord = prow()
        bomb = uncoversquares (xcoord,ycoord,row,col,bomb,dispBoard)   
    return

def winorlose (numMines,row,col,bomb,dispBoard):
    uncovered = 0
    gameend = False
    for i in range (row):
        for u in range(col):
            if dispBoard[i][u] != 'X' and dispBoard[i][u] != 'F' and dispBoard[i][u] !='*':
                uncovered = uncovered + 1
            if dispBoard[i][u] == '*':  #IF YOU CLICKED ON BOMB
                gameend = True
                print ('YOU LOSE')
                return gameend
            
    #If the number of empty spots without mines is equal to the number of spots uncovered, YOU WIN
    if (row * col) - numMines == uncovered:
        wingame = True
        gameend = True
        print ()
        print ('YOU WIN!')
    return gameend



#---------MAIN PROGRAM--------

#Ask for Board Properties
row = int(input('Enter the number of rows: '))
col = int(input('Enter the number of columns: '))

dispBoard =[]
bomb = False
gameend = False
numMines = int (input('Enter the number of bombs: '))

#CREATE BOARD WITH MINES
createboard (row,col,dispBoard)
assignbombs(row,col,numMines)
mineindicator (row,col)

while gameend != True:      #REPEAT WHILE PLAYER HASNT WON OR LOST, Keep Playing
    print ('Current Board')
    displayBoard (row,col,dispBoard)
    gameoptions(row,col,bomb,dispBoard)
    gameend = winorlose(numMines,row,col,bomb,dispBoard)
    
#SHOW FINAL BOARD
print()
print('FINAL BOARD')
displayBoard (row,col,dispBoard)
        
    





    
