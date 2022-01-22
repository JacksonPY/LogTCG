import os

def user_help_me():
    file = open('commands.txt', 'r')
    contents = file.read()
    print(contents)
    file.close()
