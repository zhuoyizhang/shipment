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


print('main starts')
#user input cycle and type
#cycle2load=input('Enter cycle to load [1c17...]')

#type2load=input('Enter type to load [nb/dt]')

#validate 1c17_dt_loc_backup.csv,1c17_dt_backup.csv,1c17_nb_loc.csv,1c17_nb.csv
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

#prepare 4 rule files

#DT

inputfile = '1c17 cDT_SWPOR_Matrix_2017_02_06.xlsx'

cycle2load=inputfile.split()[0]

#config
dtDict1c17=dict()
dtDict1c17['startCol']='O'
dtDict1c17['endCol']='AK'
dtDict1c17['exclude']={'Q','T','AE'}
dtDict1c17['cyclerow']=2
dtDict1c17['platformrow']=3


dtDict1c17['startCol_loc']='AM'
dtDict1c17['endCol_loc']='CN'
dtDict1c17['exclude_loc']={}
dtDict1c17['optioncode_row']=7

dtDict1c17['apps'] = ['HP Orbit', 'HP JumpStart', 'HP JumpStart Apps', 'HP Audio Switch']


gen_swpor.gen_swpor(inputfile,dtDict1c17)


#NB

inputfile2 = '1c17 cNB_SWPOR_Matrix_2016_12_27.xlsx'

#config
nbDict1c17=dict()
nbDict1c17['startCol']='P'
nbDict1c17['endCol']='V'
nbDict1c17['exclude']={}
nbDict1c17['cyclerow']=1
nbDict1c17['platformrow']=2



nbDict1c17['startCol_loc']='X'
nbDict1c17['endCol_loc']='BW'
nbDict1c17['exclude_loc']={}
nbDict1c17['optioncode_row']=6


nbDict1c17['apps'] = ['HP Orbit', 'HP JumpStart', 'HP JumpStart Apps', 'HP Audio Switch']


gen_swpor.gen_swpor(inputfile2, nbDict1c17)

#nb
load_swpor.load_swpor(cycle2load+'_'+'nb_loc.csv','nb',cycle2load+'_'+'nb.csv')
#dt
load_swpor.load_swpor(cycle2load+'_'+'dt_loc.csv','dt',cycle2load+'_'+'dt.csv')

calc_shipment.calc_shipment()


calc_shipment_app.calc_shipment_app('HP JumpStart')

print('main ends')
