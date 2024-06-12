table = [1,2,3,4,5,6,7,8,9]
def display_table():
    print(f" {table[0]} | {table[1]} | {table[2]} ")
    print("___|___|___")
    print(f" {table[3]} | {table[4]} | {table[5]} ")
    print("___|___|___")
    print(f" {table[6]} | {table[7]} | {table[8]} ")
    print("   |   |   ")

display_table()

entry = input("Please enter a nuber that is available : ")
i=0
while i < len(table):
    if table[i] == int(entry):
        table[i] = "X"
    i = i+1
display_table()
