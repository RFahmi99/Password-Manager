from Functions.key import *
from Functions.commands import *


keyCheck()
print("Welcome. This is your password manager. What would you like to do today? For viewing all the commands, type 'help'.")

while True:
    inp = input("Type your command: ")
    
    if inp == "quit":
        break
    
    action = commands.get(inp)
    if action:
        action()
    else:
        print("Invalid command. Type 'help' for list of commands.")