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
