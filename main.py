email = "example@gmail.com"
password = "qwerty"

credentials = {
    "email": "example@gmail.com",
    "password": "qwerty",
    "phone": "0666666666"
}

if email == "example@gmail.com":
    print("wait for password verification...")
    if password == "qerty":
        print("welcome")
    else:
        print("password is wrong")
else:
    print("email is wrong")

# the second option :
if email == "example@gmail.com" and password == "qwerty":
    print("welcome")
else:
    print("email or password is wrong")


# the third option :
if credentials["email"]=="examle@gmail.com" and credentials["password"] == "qwerty":
    print("welcome")
elif credentials["phone"]=="0666666666" and credentials["password"] == "qwerty":
    print(f"welcome, {credentials['phone']}")
else:
    print("email/phone or password is wrong")


i = 0
while i < 5:
    print(i) 
    i = i + 1

# exercise
# You can write print only once
# print all elements of list
mylist = ["lorem", "ipsum", "lorem2", "ipsum2"]

# Answer
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1


users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 28},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 34},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 22},
    {"id": 4, "name": "David", "email": "david@example.com", "age": 40},
    {"id": 5, "name": "Eve", "email": "eve@example.com", "age": 30}
]

item = 0
while item < len(users):
    print(users[item]["name"], users[item]["age"])
    item += 1

for element in users:
    print("trying with for", element["name"], element["age"])


