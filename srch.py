import sqlite3 as sl

con = sl.connect('databases/local.db')
cursor = con.cursor()


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
        cursor.execute("SELECT * FROM pokemon WHERE name LIKE (?)", ['%' + searchNameInput + '%'])
        print(cursor.fetchall())


def user_delete_entry():
    try:
        userDefinedDeletionID = input('What is the ID (first number in the data entry) of the entry you would like to '
                                      'delete?: ')
        cursor.execute("DELETE FROM pokemon WHERE id=(?)", userDefinedDeletionID)
        con.commit()
        print('Entry deleted')
    except:
        print("Failed to delete, your input needs to be an integer (for example 1).")


def user_search_type():
    userDefinedType = input('What is the type you would like to search for?: ').upper()
    cursor.execute("SELECT * FROM pokemon WHERE type=(?)", [userDefinedType])
    print(cursor.fetchall())


def user_search_rarity():
    userDefinedRarity = input('What is the rarity you would like to search for?: ').upper()
    cursor.execute("SELECT * FROM pokemon WHERE rarity=(?)", [userDefinedRarity])
    print(cursor.fetchall())


def user_search_cardset():
    userDefinedCardset = input('What is the set you would like to search for?: ').upper()
    cursor.execute("SELECT * FROM pokemon WHERE cardset=(?)", [userDefinedCardset])
    print(cursor.fetchall())
