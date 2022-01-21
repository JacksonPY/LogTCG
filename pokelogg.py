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
tree = {'VIEW ALL':user_view_all,
        'DELETE':user_delete_entry,
        'HELP':user_help_me,
        #'SNAME':user_search_name_params,
        #'STYPE':user_search_type,
        #'SRARITY':user_search_rarity,
        #'SCARDSET':user_search_cardset,
        'ENTRY':user_make_entry,
        'CREATE TABLE':customTableCreate,
        'SEARCH':custom_basic_search,
        'COLUMN NAMES':getColumnNames,
        'CUSTOM ENTRY':custom_entry}

print('')
print('Need help? Just type "help"!')

main(tree)
