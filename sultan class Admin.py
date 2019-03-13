### sultan Aljabri
# admin login Story
# 02/25/2019

class Admin:
      
      print ("Welcome to Login Program")
      loop = 'true'
      while(loop=='true'):
            adminName= input("Enter Admin name: ")
            password= input("Enter Password: ")

            if(adminName == "sultan" and password == "sultan123456"):
                print ("Welcome "+ adminName)
            loop ='false'
            loop1 ='True'
            while(loop1 == 'True'):
                command = input(adminName+ "{} >>")
                if(command == "exit" or command == "Exit"):
                    break
                else:
                    print ("'")+command + " is not a valid username!"
            else:
                print('wrong username!')


                



Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:/Users/aljabris/Desktop/sultan class Admin.py ==========
Welcome to Login Program
Enter Admin name: sultan
Enter Password: sultan123456
Welcome sultan
sultan{} >>
