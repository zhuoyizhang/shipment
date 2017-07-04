#consummer only
import urllib.request, urllib.parse, urllib.error
import csv
import sqlite3
import os.path
import create_tables
import re



def load_swpor(loc_file_name,type2load,file_name):
    print('load_swpor starts')
    print(loc_file_name,type2load,file_name)

    #input file xxxx_xx.csv and xxxx_xx.loc.csv
    #naming convention     1c17_nb.csv and 2c17-dt-loc.csv




    #read csv file into memory

    conn = sqlite3.connect('shipment.sqlite')
    cur = conn.cursor()

    #read csv file into option code table
    #open 1c17_nb_loc.csv
    #load file into dict of lists
    #'orbit' [aba,uum, ...]
    #load dataframe into table

    with open(loc_file_name, newline='') as loc_file:
        reader = csv.reader(loc_file, delimiter=',')
        first_line = loc_file.readline()
        print(first_line)

        #each column is an app
        #key=col_index, value=app_id
        dict_app_id = dict()
        col_index=1
        for name in first_line.split(',')[1:]:
            cur.execute('''INSERT OR IGNORE INTO Apps (name)
                VALUES ( ? )''', (name,))
            cur.execute('SELECT id FROM Apps WHERE name = ? ', (name,))
            dict_app_id[col_index]=cur.fetchone()[0]
            col_index = col_index + 1

        # Option Code, HP Orbit, HP JumpStart, HP JumpStart Apps, HP Audio Switch
        # ABA, n, n, n, n
        # B1F, n, n,, n

        # id, app_id, option_cd, type
        for row in reader:
            option_code = row[0]
            type = type2load
            #dict.items() return tuple, tuple does not have key, use[i]
            #item(col_index, app_id)
            for item in dict_app_id.items():
                #print(row)
                if len(row[item[0]])<1: continue
                cur.execute('''INSERT OR IGNORE INTO OptionCodes (app_id, option_cd, type)
                     VALUES ( ? ,?,?)''', ( item[1], option_code, type) )


    #load 1c17_nb_csv
    with open(file_name, newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=',')
        csvfile.readline()

        #do not repeat inserting platforms
        for row in reader:
            #is it a new platform
            #print(row[2].split())
            platform = row[2].split()[0]
            version = row[2].split()[1]
            type = row[1]
            category = re.search(r'\(.*\)',row[2]).group(0)[1:-1]
            #print(platform, version, category)
            cur.execute('''INSERT OR IGNORE INTO Platforms (platform, version, category)
                    VALUES ( ?, ?, ?)''', ( platform, version, category) )
            #insert into install table
            #loop by app


            result = cur.execute('select app_id, option_cd from OptionCodes')
            data = result.fetchall()
            for item in data:
                cur.execute('''INSERT OR IGNORE INTO Install (app_id, loc_id, platform, version, type, platform_type)
                                VALUES ( ?, ?,?,?,?,?)''', (item[0], item[1],platform, version, type, type2load))

    cur.close()

    conn.commit()






    #load new version of SWPOR





    #deal with new cycle SWPOR



    #cycle ???
    #platform change time-   add or remove a platform in 1c17
    print('load_swpor ends')

    return