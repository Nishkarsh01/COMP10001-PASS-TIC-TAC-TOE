# TIC TAC TOE game using python
#     0:1:2
# 0: [_,_,_]
# 1: [_,_,_]
# 2: [_,_,_]

# column:2
# row:1
# row:|
# coulmn:->
#     0:1:2
# 0: [X,_,_]
# 1: [_,_,_]
# 2: [_,_,_]


# IF turnTracker is true, the turn is of first player 'X', ELSE second player 'O'
turnTracker=False
gameEnd =False

#CREATE 3 lists 
row0=["", "", ""]
row1=["", "", ""]
row2=["", "", ""]


        
while(gameEnd!=True):
    #ASSUME user input is a valid positive integer value [0,1,2]
    #GET row number
    rowSelection=int(input("Please select row number: "))
    #GET Column Number
    columnSelection=int(input("Please select a column number: "))
    
    if(turnTracker):
        if(rowSelection==0):
                row0[columnSelection]="X"
                print(row0)
                print(row1)
                print(row2)
        elif(rowSelection==1):
            row1[columnSelection]="X"
            print(row0)
            print(row1)
            print(row2)
        elif(rowSelection==2):
            row2[columnSelection]="X"
            print(row0)
            print(row1)
            print(row2)
    else:
        if(rowSelection==0):
            row0[columnSelection]="O"
            print(row0)
            print(row1)
            print(row2)
        elif(rowSelection==1):
            row1[columnSelection]="O"
            print(row0)
            print(row1)
            print(row2)
        elif(rowSelection==2):
            row2[columnSelection]="O"
            print(row0)
            print(row1)
            print(row2)
    
    
# SWITCH BETWEEN USERS
# MODULARIZE CODE
# HANDLE INPUT IN THE SAME LOCATIONS
# MODULARIZE CODE





