import os
import sys

os.system("git status")

add_user_response = input("would you like to add? Y/N ('-f')to force:  ")
if add_user_response == "y":
    os.system("git add -A")
elif add_user_response == "n":
     sys.exit()
elif add_user_response == "-f":
     os.system("git add -A")
     os.system("git commit -m force")
     os.system("git push")
     sys.exit()
    

else:
     print("Error")
     sys.exit()


commit_user_response = input("would you like to commit? Y/N:  ")
message = input("Enter your commit message (Use dashes (-) as spaces): ")
        
if commit_user_response == "y":
    os.system("git commit -m" + message)
elif commit_user_response == "n":
     sys.exit()
else:
     print("Error")
     sys.exit()

push_user_response = input("Would you like to push these changes? Y/N: ")
if commit_user_response == "y":
    os.system("git push")
elif commit_user_response == "n":
     sys.exit()
else:
     print("Error")
     sys.exit()

      
