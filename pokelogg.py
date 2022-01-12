# imports!
import os
import sqlite3 as sl
from srch import *
from hlp import *



# establishing connection
con = sl.connect('databases/local.db')
cursor = con.cursor()
print('')
print("Database Opened Success")


# initial table creation.
cursor.execute("""CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        rarity text,
        cardset text,
        type text
    )""")

# dictionary to return a function based on users input. seems to be faster than massive elif block.
tree = {'VIEW ALL':user_view_all,
        'DELETE':user_delete_entry,
        'HELP':user_help_me,
        'SNAME':user_search_name_params,
        'STYPE':user_search_type,
        'SRARITY':user_search_rarity,
        'SCARDSET':user_search_cardset,
        'ENTRY':user_make_entry}

print('')
print('Need help? Just type "help"!')
mainWhileLooper = True
while mainWhileLooper:
    startProgUser = input("Welcome, what would you like to do?\n").upper()

    cls()
    print('')

    if startProgUser in tree:
        tree.get(startProgUser)()
    elif startProgUser == 'EXIT':
        print("Goodbye!")
        cls()
        break
    else:
        print("That's not a selection. Type 'help' to see the available selections.")
