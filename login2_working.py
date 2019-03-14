###################################
#Author:          Hamdan Alshammari
#Project_Name:    UserLogin
#Date:            03/08/2019
###################################

users = {}
status = ""
 
def displayMenu():
    status = input("Are you registered user? y/n?: " )
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
        createLogin = input("Create login name: ")
     
        if createLogin in users:
            print("\nLogin name already exist!\n")
        else:
            createPWord = input("Create password: ")
            users[createLogin] = createPWord
            print("\nUser created\n")
     
def oldUser():
    login = input("Enter login name: ")
    pWord = input("Enter password: ")
 
    if login in users and users[login] == pWord:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")
 
while status != "q":
    displayMenu()

def main():
    User
    displayMenu()
    newUser()
    oldUser()

main()
