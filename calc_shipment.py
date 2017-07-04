#consummer only
#save SWPOR to csv - manual
import urllib.request, urllib.parse, urllib.error
import csv
import sqlite3

def calc_shipment():
    print('calc_shipment starts')


    ## read csv raw file

    conn = sqlite3.connect('shipment.sqlite')
    cur = conn.cursor()

    #load shipment into shipment table
    cur.executescript('''
    
    DROP TABLE IF EXISTS Shipment;
    
    CREATE TABLE IF NOT EXISTS Shipment (
        FISC_YR INTEGER,
        FISC_MTH INTEGER,
        QTY   INTEGER,
        PRFT_CTR_LVL_5_NM  TEXT,
        OPERATING_SYSTEM TEXT,
        PLATFORM TEXT,
        CYCLE TEXT,
        PROD_OPT_CD TEXT
    )
    ''')


    exp = ['STOLI','MAYA','KOWALSKI','ZONDA','PASHA','SANGRIA','KAILI','NOKA','CINDERELLA','PUCCINI','PAVLOVA','PANINI','BABA','GODIVA','VALRHONA','PAVLOVA','VANILLA','GUMMI','PITA','DASANI','JOSHUA','FAJITA']

    with open('Units_Final_2017_04_06_raw.csv', newline='') as rawfile:
        reader = csv.reader(rawfile, delimiter=',')
        rawfile.readline()
        for row in reader:
            fisc_year = int(row[0].split('-')[0][2:])
            fisc_month= int(row[0].split('-')[1])
            qty = row[32]
            country= row[10]
            os= row[35]
            platform = row[33].split(' ')[0]
            if platform.upper() not in exp:
                    if platform.upper().endswith('A') or platform.upper().endswith('I'):
                        platform=platform[:-1]
            #found exceptions in data. corrected
            if platform.upper().startswith('SPHINX2'):
                platform = platform[:-1]
                        #print(platform)
            cycle=row[36]
            option_cd=row[38]
            #print(qty)

            cur.execute('''INSERT OR IGNORE INTO Shipment (FISC_YR, FISC_MTH, QTY,PRFT_CTR_LVL_5_NM,OPERATING_SYSTEM,PLATFORM,CYCLE,PROD_OPT_CD)
                 VALUES ( ?,?,?,?,?,?,?,? )''', (fisc_year,fisc_month, qty,country,os,platform,cycle,option_cd ) )

    conn.commit()


    ## Consumer shipment units in K
    cur.execute('select SUM(s.QTY) FROM shipment s where s.fisc_yr=2017 and s.fisc_mth = 5')
    consumerShipmentUnits = cur.fetchone()[0]
    print('consumerShipmentUnits:',consumerShipmentUnits)

    #cur.close()


    ## Consumer shipment units in K excl. CKG

    cur.execute("""
    select SUM(QTY)
    FROM
    shipment
    WHERE
    PRFT_CTR_LVL_5_NM not in ('China Local Sales', 'Germany Sales', 'Korea Local Sales')
    and fisc_yr=2017
    and fisc_mth = 5
    
    """)
    consumerShipmentUnitsCKG = cur.fetchone()[0]
    print('consumerShipmentUnitsCKG:',consumerShipmentUnitsCKG)




    ## Consumer Win10 units in K
    cur.execute("""select SUM(QTY)
            FROM shipment
            WHERE OPERATING_SYSTEM LIKE ('%10%')
            and fisc_yr=2017
           and fisc_mth = 5
    """)
    consumerWin10 = cur.fetchone()[0]
    print('consumerWin10:',consumerWin10)


    ## Consumer Win10 units in K excl. CGK

    cur.execute("""select SUM(QTY)
            FROM shipment
            WHERE PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND OPERATING_SYSTEM LIKE ('%10%')
            and fisc_yr=2017
           and fisc_mth = 5
    """)
    consumerWin10CGK = cur.fetchone()[0]
    print('consumerWin10CGK:',consumerWin10CGK)


    cur.close()

    conn.close()


    #
    # ##The version number is not clean, we just filter on platform
    # ##1c17, DT
    # cur.execute("""
    # select SUM(s.QTY)
    #         FROM shipment s
    #         WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
    #         AND s.OPERATING_SYSTEM LIKE ('%10%')
    # 		AND upper(s.platform) in (	select distinct upper(i.platform)
    # 		from install i, apps a
    # 		where a.id = i.app_id
    # 		and a.name='JumpStart'
    # 		and type='new')
    #        and s.cycle='1C 17'
    #        and s.fisc_yr=2017
    # 	   and s.fisc_mth = 5
    #
    # """)
    # dt1c17 = cur.fetchone()[0]
    # print('dt1c17:',dt1c17)
    #
    #
    #
    # #2c16, NB, DT
    # cur.execute("""
    # select SUM(s.QTY)
    #         FROM shipment s
    #         WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
    #         AND s.OPERATING_SYSTEM LIKE ('%10%')
    # 		AND upper(s.platform) in (	select distinct upper(i.platform)
    # 		from install i, apps a
    # 		where a.id = i.app_id
    # 		and a.name='JumpStart'
    # 		and type='refresh')
    #        and s.cycle='2C 16'
    #        and s.fisc_yr=2017
    # 	   and s.fisc_mth = 5
    #
    # """)
    # dt2c16 = cur.fetchone()[0]
    # print('dt2c16:', dt2c16)
    #
    #
    #
    #
    # #3c16, NB, DT
    #
    # cur.execute("""
    # select SUM(s.QTY)
    #         FROM shipment s
    #         WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
    #         AND s.OPERATING_SYSTEM LIKE ('%10%')
    # 		AND upper(s.platform) in (	select distinct upper(i.platform)
    # 		from install i, apps a
    # 		where a.id = i.app_id
    # 		and a.name='JumpStart'
    # 		and type='refresh')
    #        and s.cycle='3C 16'
    #        and s.fisc_yr=2017
    # 	   and s.fisc_mth = 5
    #
    # """)
    # dt3c16 = cur.fetchone()[0]
    # print('dt3c16:', dt3c16)
    #
    #
    # #3c15, NB, DT
    #
    # cur.execute("""
    #
    #
    # select SUM(s.QTY)
    #         FROM shipment s
    #         WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
    #         AND s.OPERATING_SYSTEM LIKE ('%10%')
    # 		AND upper(s.platform) in (	select distinct upper(i.platform)
    # 		from install i, apps a
    # 		where a.id = i.app_id
    # 		and a.name='JumpStart'
    # 		and type='refresh')
    #        and s.cycle='3C 15'
    #        and s.fisc_yr=2017
    # 	   and s.fisc_mth = 5
    #
    # """)
    # dt3c15 = cur.fetchone()[0]
    # print('dt3c15:', dt3c15)
    #
    #
    # #Consumer Win10 Jumpstart NPI (1C17) Unit in K, excl. CGK
    #
    # #Number1c17=`r Number1c17`
    #
    #
    # #Consumer Win10 Jumpstart NPI (3C16) Unit in K, excl. CGK
    #
    # #Number3c16=`r Number3c16`
    #
    #
    # #Softroll Win10 Jumpstart 3C15-2C16 Unit in K, excl. CGK
    #
    # #Numbers3c152c16=`r format(Numbers3c152c16, digits=10, big.mark=",")`
    #
    #
    print('calc_shipment ends')

    return