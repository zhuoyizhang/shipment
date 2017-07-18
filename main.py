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



# if first time, load create table script

create_tables.create_tables()

cycle2load=['3c16','1c17','2c17']
max_cycle='2c17'
#cycle2load=['3c16']

for cycle in cycle2load:
    #only pick the selected sections by cycle and their child sections.
    config = util.loadConfig('swpor_0617.conf')
    subtree= util.getConfigTree(cycle,config)
    children = util.getConfigChildren(subtree)
    parent = util.getConfigParent(subtree)

    for child in children:
        gen_swpor.gen_swpor(children[child],parent)




    output_path = r'./swpor_output/'
    print(output_path)
    #nb
    load_swpor.load_swpor(output_path + cycle+'_'+'nb_loc.csv'
                          ,'nb'
                          ,output_path + cycle+'_'+'nb.csv',cycle)
    #dt
    load_swpor.load_swpor(output_path + cycle+'_'+'dt_loc.csv'
                          ,'dt'
                          ,output_path + cycle+'_'+'dt.csv',cycle)

calc_shipment.calc_shipment(config[max_cycle])

#all apps
#calc_shipment_app.calc_shipment_app('HP JumpStart',max_cycle)
#calc_shipment_app.calc_shipment_app('OMEN Command Center',max_cycle)
calc_shipment_app.calc_shipment_app('HP Audio Switch',max_cycle)



print('main ends')
