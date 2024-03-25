from .access import *


commands = {
    "help": lambda: print("The list of commands:\nGet saved password - 1\nSet new password - 2\nTo exit - quit"),
    "1": lambda: print(showPass(input("Enter the name of the password: "))),
    "2": lambda: writePass(input("Enter the name of the password: "), input("Enter the password: "))
}