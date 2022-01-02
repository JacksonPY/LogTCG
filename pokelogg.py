# imports!
import os
import sqlite3 as sl

# establishing connection
con = sl.connect('local.db')
cursor = con.cursor()
print('')
print("Database Opened Success")


def user_view_all():
    cursor.execute("SELECT * FROM pokemon")
    print(cursor.fetchall())
    print('Query Successful!')


def user_search_name_params():
    searchNameInput = input('Please input the name of the card you are looking up: ').upper()
    searchNameInputIfLike = input(f"Do you want to search for all names like {searchNameInput}?(y/n): ")
    if searchNameInputIfLike == 'n':
        cursor.execute("SELECT * FROM pokemon WHERE name=(?)", [searchNameInput])
        print(cursor.fetchall())
    elif searchNameInputIfLike == 'y':
        cursor.execute("SELECT * FROM pokemon WHERE name LIKE (?)", ['%'+searchNameInput+'%'])
        print(cursor.fetchall())


def user_delete_entry():
    userDefinedDeletionID = input('What is the ID (first number in the data entry) of the entry you would like to '
                                  'delete?: ')
    cursor.execute("DELETE FROM pokemon WHERE id=(?)", userDefinedDeletionID)
    con.commit()
    print('Entry deleted')


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
    keepTheLoopCount = 0
    # first response
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
        print("Commands you can use to iterate upon the database. "
              "\nHelp - Resonds with a help message."
              "\nEntry - Start a card data entry!"
              "\nView All - Views all the entries in the 'pokemon' table."
              "\nSName - Searches the database by name."
              "\nDelete - Start the deletion process of a data entry. \n        You might need to find the specific "
              "entry ID before trying "
              " to delete it."
              "\nExit - Exits the program/main loop.")
    elif startProgUser == 'EXIT':
        break

    elif startProgUser == 'SNAME':
        user_search_name_params()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Not a valid command. Please try again. If you need more help please type "help"')
