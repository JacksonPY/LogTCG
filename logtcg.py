# imports!
import sqlite3 as sl
from plgth.hlp import *
from plgth.logi import *
from plgth.srch import *

# establishing connection
con = sl.connect('databases/local.db')
cursor = con.cursor()
print('')
print("Database Opened Success")

tableExists(customTableCreate)
con.commit()


# dictionary to return a function based on users input. seems to be faster than massive elif block.
tree = {'VIEW ALL':Query.user_view_all,
        'DELETE':Entry.user_delete_entry,
        'HELP':user_help_me,
        'CREATE TABLE':customTableCreate,
        'SEARCH':Query.custom_basic_search,
        'COLUMN NAMES':Query.getColumnNames,
        'ENTRY':Entry.custom_entry}

print('')
print('Need help? Just type "help"!')

main(tree)
