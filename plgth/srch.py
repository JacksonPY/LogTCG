import sqlite3 as sl

con = sl.connect('databases/local.db')
cursor = con.cursor()

def user_view_all():
    cursor.execute("SELECT * FROM pokemon")
    print(cursor.fetchall())
    print('Query Successful!')

def user_delete_entry():
    try:
        userDefinedDeletionID = input('What is the ID (first number in the data entry) of the entry you would like to '
                                      'delete?: ')
        cursor.execute("DELETE FROM pokemon WHERE id=(?)", userDefinedDeletionID)
        con.commit()
        print('Entry deleted')
    except:
        print("Failed to delete, your input needs to be an integer (for example 1).")

def custom_basic_search():
    try:
        customSearchCol = input("Alright, lets do this search. What column are we searching from?: ").upper()
        customSerarchParam = input("Now what is the parameter(s) we are using? (name of the card, type etc.): ").upper()
        cursor.execute(f"SELECT * FROM pokemon where {customSearchCol}=(?)", [customSerarchParam])
        if cursor.fetchall() == []:
            print("------")
            print("There is no entry with those parameters!")
            print("------")
        else:
            print(cursor.fetchall())
    except:
        print("Failed to execute the query! Try again and make sure you have an idea for what you're searching for.")

def getColumnNames():
        exCols = cursor.execute("SELECT * FROM pokemon")
        for cols in exCols.description[1:]:
                print(cols[0])

def custom_entry():
    try:
        v = ""
        q = ""
        kk = []
        exCols = cursor.execute("SELECT * FROM pokemon")
        for e in exCols.description[1:]:
                v += e[0] + ", "
                q += "?, "
                g = input(f"Insert entry data for {e[0]}: ").upper()
                kk.append(g)
        q = q[:-2]
        v = v[:-2]
        cursor.execute(f"INSERT INTO pokemon ({v}) VALUES ({q})", kk)
        con.commit()
        print("Data entry success!")
    except:
        print("Data entry failed! Try again, make sure you follow the prompts correctly.")



# old way of doing things. going to use these to look back on.

# def user_search_type():
#     userDefinedType = input('What is the type you would like to search for?: ').upper()
#     cursor.execute("SELECT * FROM pokemon WHERE type=(?)", [userDefinedType])
#     print(cursor.fetchall())


# def user_search_name_params():
#     searchNameInput = input('Please input the name of the card you are looking up: ').upper()
#     searchNameInputIfLike = input(f"Do you want to search for all names like {searchNameInput}?(y/n): ")
#     if searchNameInputIfLike == 'n':
#         cursor.execute("SELECT * FROM pokemon WHERE name=(?)", [searchNameInput])
#         print(cursor.fetchall())
#     elif searchNameInputIfLike == 'y':
#         cursor.execute("SELECT * FROM pokemon WHERE name LIKE (?)", ['%' + searchNameInput + '%'])
#         print(cursor.fetchall())

# def user_search_rarity():
#     userDefinedRarity = input('What is the rarity you would like to search for?: ').upper()
#     cursor.execute("SELECT * FROM pokemon WHERE rarity=(?)", [userDefinedRarity])
#     print(cursor.fetchall())


# def user_search_cardset():
#     userDefinedCardset = input('What is the set you would like to search for?: ').upper()
#     cursor.execute("SELECT * FROM pokemon WHERE cardset=(?)", [userDefinedCardset])
#     print(cursor.fetchall())

# def user_make_entry():
#     cardName = input("Input the card name: ").upper()
#     cardRarity = input("Input the card rarity: ").upper()
#     cardSet = input("Input the set name (Fusion Strike, Sword & Shield, etc.: ").upper()
#     cardType = input("What is the cards type: ").upper()

#     # executing the SQL insert statement into the 'pokemon' table. '?' denotes a placeholder for the variables
#     # from the user.
#     cursor.execute("INSERT INTO pokemon (name, rarity, cardset, type) VALUES (?,?,?,?)",
#                    (cardName, cardRarity, cardSet, cardType))
#     con.commit()
#     print("Entry successful")


