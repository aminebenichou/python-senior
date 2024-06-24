table = ["1","2","3","4","5","6","7","8","9"]
def display_table():
    print(f" {table[0]} | {table[1]} | {table[2]} ")
    print("___|___|___")
    print(f" {table[3]} | {table[4]} | {table[5]} ")
    print("___|___|___")
    print(f" {table[6]} | {table[7]} | {table[8]} ")
    print("   |   |   ")

display_table()

def getTheWinner(firstcell, secondcell, thirdcell, player):
    
    if firstcell == secondcell and secondcell == thirdcell :
        print(f"{player} is the winner")
        return True
    else:
        i = 0
        draw = 1
        while i < len(table):
            if table[i] != str(i+1):
                
                i += 1
            else:
                draw -= 1
                break
        if draw == 1 :
            print("it is a draw")
            return True

turn = 1
while 1>0:
    entry = input("Please enter a number that is available : ")
    if not (entry>="1" and entry<="9"):
        print("Invalid entry")
        entry = input("Please enter a number that is available : ")
    player = ""
    if turn%2 == 0:
        player = "O"
    else:
        player = "X"
    # player = input("Please enter a X or O : ") 
    i=0
    while i < len(table):
        if table[i] == entry:
            table[i] = player
        i = i+1
    display_table()
    turn = turn + 1
    if getTheWinner(table[0], table[1], table[2], player) or getTheWinner(table[3], table[4], table[5], player) or getTheWinner(table[6], table[7], table[8], player) or getTheWinner(table[0], table[3], table[6], player) or getTheWinner(table[1], table[4], table[7], player) or getTheWinner(table[2], table[5], table[8], player) or getTheWinner(table[0], table[4], table[8], player) or getTheWinner(table[2], table[4], table[6], player):
        break
