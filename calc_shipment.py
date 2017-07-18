#consummer only
#save SWPOR to csv - manual
import urllib.request, urllib.parse, urllib.error
import csv
import sqlite3
import util
def calc_shipment(config1):
    print('calc_shipment starts')
    #config=util.getConfig(config1)


    shipmentfile = r'./units/' + config1.get('shipment')
    print(shipmentfile)
    ## read csv raw file

    conn = sqlite3.connect('shipment.sqlite')
    cur = conn.cursor()



    #ending with A or I
    exp = ['STOLI','MAYA','KOWALSKI','ZONDA','PASHA','SANGRIA',
           'KAILI','NOKA','CINDERELLA','PUCCINI','PAVLOVA','PANINI',
           'BABA','GODIVA','VALRHONA','PAVLOVA','VANILLA',
           'GUMMI','PITA','DASANI','JOSHUA','FAJITA']

    with open(shipmentfile, newline='') as rawfile:
        reader = csv.reader(rawfile, delimiter=',')
        rawfile.readline()
        for row in reader:
            fisc_year = int(row[0].split('-')[0][2:])
            fisc_month= int(row[0].split('-')[1])
            qty = row[33]
            country= row[10]
            os= row[36]
            platform = row[34].split(' ')[0]
            if platform.upper() not in exp:
                    if platform.upper().endswith('A') or platform.upper().endswith('I'):
                        platform=platform[:-1]
            #found exceptions in data. corrected
            if platform.upper().startswith('SPHINX2'):
                platform = platform[:-1]
                        #print(platform)
            cycle=row[37]
            try:
                option_cd=row[18].split("#")[1]
            except:
                option_cd=None
            #print(qty)

            cur.execute('''INSERT OR IGNORE INTO Shipment (FISC_YR, FISC_MTH, QTY,PRFT_CTR_LVL_5_NM,OPERATING_SYSTEM,PLATFORM,CYCLE,PROD_OPT_CD)
                 VALUES ( ?,?,?,?,?,?,?,? )''', (fisc_year,fisc_month, qty,country,os,platform,cycle,option_cd ) )

    conn.commit()

    cur.execute('select max(s.fisc_yr),max(s.fisc_mth) FROM shipment s ')
    result = cur.fetchone()


    fisc_yr=result[0]
    fisc_mth=result[1]


    ## Consumer shipment units in K
    cur.execute('select SUM(s.QTY) FROM shipment s where s.fisc_yr=? and s.fisc_mth = ?',(fisc_yr,fisc_mth))
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
    and fisc_yr=?
    and fisc_mth = ?
    """, (fisc_yr,fisc_mth))
    consumerShipmentUnitsCKG = cur.fetchone()[0]
    print('consumerShipmentUnitsCKG:',consumerShipmentUnitsCKG)




    ## Consumer Win10 units in K
    cur.execute("""select SUM(QTY)
            FROM shipment
            WHERE OPERATING_SYSTEM LIKE ('%10%')
            and fisc_yr=?
            and fisc_mth = ?
    """,(fisc_yr,fisc_mth))
    consumerWin10 = cur.fetchone()[0]
    print('consumerWin10:',consumerWin10)


    ## Consumer Win10 units in K excl. CGK

    cur.execute("""select SUM(QTY)
            FROM shipment
            WHERE PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND OPERATING_SYSTEM LIKE ('%10%')
            and fisc_yr=?
           and fisc_mth = ?
    """,(fisc_yr,fisc_mth))
    consumerWin10CGK = cur.fetchone()[0]
    print('consumerWin10CGK:',consumerWin10CGK)


    cur.close()

    conn.close()



    print('calc_shipment ends')

    return