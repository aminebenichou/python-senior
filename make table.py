print("   |   |   ")
print("___|___|___")
print("   |   |   ")
print("___|___|___")
print("   |   |   ")

def initialization():
    return [[" " for _ in range(3)] for _ in range(3)]



def display_table(table):
    for m in table :
        print(" | ".join(m))
        print("-"*10)


print(initialization())
display_table(initialization())
