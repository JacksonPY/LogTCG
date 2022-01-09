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

print('')
print('Need help? Just type "help"!')
mainWhileLooper = True
while mainWhileLooper:
    # first response
    print('')
    startProgUser = input("Welcome, what would you like to do?\n").upper()

    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Data entry, 4 parameters.
    if startProgUser == 'ENTRY':
        cardName = input("Input the card name: ").upper()
        cardRarity = input("Input the card rarity: ").upper()
        cardSet = input("Input the set name (Fusion Strike, Sword & Shield, etc.: ").upper()
        cardType = input("What is the cards type: ").upper()

        # executing the SQL insert statement into the 'pokemon' table. '?' denotes a placeholder for the variables
        # from the user.
        cursor.execute("INSERT INTO pokemon (name, rarity, cardset, type) VALUES (?,?,?,?)",
                       (cardName, cardRarity, cardSet, cardType))
        con.commit()
        print("Entry successful")

    elif startProgUser == 'VIEW ALL':
        user_view_all()

    elif startProgUser == 'DELETE':
        user_delete_entry()

    elif startProgUser == 'HELP':
        user_help_me()

    elif startProgUser == 'EXIT':
        break

    elif startProgUser == 'SNAME':
        user_search_name_params()

    elif startProgUser == 'STYPE':
        user_search_type()

    elif startProgUser == 'SRARITY':
        user_search_rarity()

    elif startProgUser == 'SCARDSET':
        user_search_cardset()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Not a valid command. Please try again. If you need more help please type "help"')
