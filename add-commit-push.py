import os


os.system("git status")

add_user_response = input("would you like to add? Y/N:  ")
if add_user_response == "y":
    os.system("git add -A")
elif add_user_response == "n":
     os.abort
else:
     print("Error")


commit_user_response = input("would you like to commit? Y/N:  ")
message = input("Enter your commit message: ")
        
if commit_user_response == "y":
    os.system("git commit -m" + message)
elif commit_user_response == "n":
     os.abort
else:
     print("Error")


message = input("Enter your commit message: ")
        
