import os
import sqlite3 as sl
from inspect import signature

con = sl.connect('databases/local.db')
cursor = con.cursor()


# TODO - this entire file just needs to change its so poorly written

def tableExists(customTableCreate):
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' and name = 'pokemon'")
    if cursor.fetchone()[0]==1:
        print('Table Exists')
    else: 
        while True:
            selectDefault = input("Would you like to use the default table that is created?: ").upper()
            if selectDefault == "NO":
                    customTableCreate()
                    break
            elif selectDefault == "YES":
                    defaultTable(cursor)
                    break
            else:
                print("Please make a decision. 'Yes' to use the default table. 'No' to make your own custom table.")

def customTableCreate():
    columnLoop = True
    while columnLoop == True:
        cursor.execute("""CREATE TABLE IF NOT EXISTS pokemon (
                id INTEGER PRIMARY KEY AUTOINCREMENT
            )""")
        columnCount = int(input("How many columns would you like to create? (categories)\n"))

        # function to increment on the amount of columns and create columns based on user input.
        mk_col_names(columnCount)
            
        columnCorrect = input(f'Amazing! You said {columnCount}. Is that correct?').upper()
        if columnCorrect == "YES":
            columnLoop = False
        if columnCorrect == "NO":
            return

def mk_col_names(columnCount):
    increm = 0
    while increm < columnCount:
        colNameQ = input("Enter column name: ")
        colTypeQ = input("What is this columns type? (text, int, date): ")
        increm += 1
        cursor.execute(f"ALTER TABLE pokemon ADD COLUMN {colNameQ} '{colTypeQ}'")

def defaultTable(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text,
        rarity text,
        cardset text,
        type text
    )""")

        
def clear():
    os.system("cls" if os.name == 'nt' else 'clear')

def main(tree):
    clear()
    file = open("mm.txt", 'r')
    contents = file.read()
    print(contents)
    mainWhileLooper = True
    while mainWhileLooper:
        startProgUser = input("Welcome, what would you like to do?\n").upper()

        clear()
        print('')

        if startProgUser in tree:
            selected_function = tree.get(startProgUser)
            sig = signature(selected_function)
            amt_params = sig.parameters
            if len(amt_params) > 1:
                selected_function(cursor, con)
            else:
                selected_function(cursor)
        elif startProgUser == 'EXIT':
            print("Goodbye!")
            clear()
            break
        else:
            print("That's not a selection. Type 'help' to see the available selections.")

