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

    #load 1c17_nb_loc.csv
    with open(loc_file_name, newline='') as loc_file:
        reader = csv.reader(loc_file, delimiter=',')
        first_line = loc_file.readline()
        print(first_line)
        newappname = None
        for row in reader:
            option_code = row[1]
            appname = row[0]
            if newappname is None or newappname !=appname:
                newappname=appname
                cur.execute('''INSERT OR IGNORE INTO Apps (name)
                                                VALUES ( ? )''', (appname,))
            cur.execute('SELECT id FROM Apps WHERE name = ? ', (appname,))
            appid = cur.fetchone()[0]

            type = type2load
            #dict.items() return tuple, tuple does not have key, use[i]
            #item(col_index, app_id)

            cur.execute('''INSERT OR IGNORE INTO OptionCodes (app_id, option_cd, type)
                     VALUES ( ? ,?,?)''', ( appid, option_code, type) )


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
            cycle = row[1]
            category = re.search(r'\(.*\)',row[2]).group(0)[1:-1]
            #print(platform, version, category)
            cur.execute('''INSERT OR IGNORE INTO Platforms (platform, version, category)
                    VALUES ( ?, ?, ?)''', ( platform, version, category) )
            #insert into install table
            #loop by app and loc code

            result = cur.execute('select app_id, option_cd from OptionCodes where type=?',(type2load,))
            data = result.fetchall()
            for item in data:
                cur.execute('''INSERT OR IGNORE INTO Install (app_id, option_cd, platform, version, platform_type,cycle)
                                VALUES ( ?, ?,?,?,?,?)''', (item[0], item[1],platform, version, type2load,cycle))

    cur.close()

    conn.commit()






    #load new version of SWPOR





    #deal with new cycle SWPOR



    #cycle ???
    #platform change time-   add or remove a platform in 1c17
    print('load_swpor ends')

    return