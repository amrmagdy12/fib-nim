numC=int(input())
print("there is pile of ",numC,"on the table")
while(numC!=0):
    print("player 1 turn: ")
    p1=int(input())
    while(p1<0):
        print("negative numbers not allowed , Enter again :")
        p1=int(input()) 
    if(p1==numC):
        print("you Can't take all of Coins")
        print("Come on again !!")    
        p1=int(input())    
    numC-=p1
    while(numC!=0):
        print("there is a pile of ",numC,"on table")
        print("player 2 turn: ")
        p2=int(input())
        while(p2>numC):
            print("you choose a number more than pile of coins\nplease enter again:")
            p2=int(input())
        while(p2>2*p1):
            print("you can't take more than twice previous move")
            print("player 2's turn:")
            p2=int(input())
        while(p2<0):
            print("positive number onlyy please enter again: ")
            p2=int(input())    
        numC-=p2
        if(numC==0):
            print("player 2 wins!!")
            exit()
        print("there is a pile of ",numC,"on table")         
        print("player 1's turn: ")
        p1=int(input())
        while(p1>numC):
            print("you choose a number more than pile of coins\nplease enter again:")
            p1=int(input())
        while(p1>2*p2):
            print("you cant take more than twice previous move")
            print("player 1's turn:")
            p1=int(input())
        while(p1<0):
            print("positive number onlyy please enter again: ")
            p1=int(input())
        numC-=p1
        if(numC==0):
            print("player 1 wins!!")



