#consummer only
import urllib.request, urllib.parse, urllib.error
import csv
import sqlite3
import os.path
import create_tables

import load_swpor
import calc_shipment
import calc_shipment_app
import gen_swpor


import configparser
import util




print('main starts')
#user input cycle and type
#cycle2load=input('Enter cycle to load [1c17...]')

#type2load=input('Enter type to load [nb/dt]')

# file_name_lst = list()
# type2load='dt'
# file_name=cycle2load+'_'+type2load+'.csv'
# file_name_lst.append(file_name)
#
# loc_file_name=cycle2load+'_'+type2load+'_loc'+'.csv'
# file_name_lst.append(loc_file_name)
#
#
# type2load='nb'
# file_name=cycle2load+'_'+type2load+'.csv'
# file_name_lst.append(file_name)
#
# loc_file_name=cycle2load+'_'+type2load+'_loc'+'.csv'
# file_name_lst.append(loc_file_name)
#
# print(file_name_lst)
# #refactor this section into a function later
# from pathlib import Path
#
# for file in file_name_lst:
#     my_file = Path(file)
#     if not my_file.is_file():
#         print(file+' does not exist')
#         quit()


# if first time, load create table script

create_tables.create_tables()

cycle2load='1c17'

#only pick the selected sections by cycle and their child sections.
config = util.loadConfig('swpor.conf')
subtree= util.getConfigTree(cycle2load,config)
children = util.getConfigChildren(subtree)
parent = util.getConfigParent(subtree)

for child in children:
    gen_swpor.gen_swpor(children[child],parent)




#nb
load_swpor.load_swpor(cycle2load+'_'+'nb_loc.csv','nb',cycle2load+'_'+'nb.csv')
#dt
load_swpor.load_swpor(cycle2load+'_'+'dt_loc.csv','dt',cycle2load+'_'+'dt.csv')

calc_shipment.calc_shipment(config[cycle2load])

calc_shipment_app.calc_shipment_app('HP JumpStart')

print('main ends')
