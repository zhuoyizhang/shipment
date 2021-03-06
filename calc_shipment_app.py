#consummer only
import urllib.request, urllib.parse, urllib.error
import csv
import sqlite3


def calc_shipment_app(app_name,current_cycle):
    print('calc_shipment app starts:', app_name)

    ## read csv raw file

    conn = sqlite3.connect('shipment.sqlite')
    cur = conn.cursor()
    cur.execute('select max(s.fisc_yr),max(s.fisc_mth) FROM shipment s ')
    result = cur.fetchone()

    fisc_yr = result[0]
    fisc_mth = result[1]
    ##The version number is not clean, we just filter on platform
    ##2c17, DT
    cur.execute(("""
    		select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='2c17'  
    		and i.platform_type='dt'
           and s.cycle='2C 17'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?

        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    dt2c17 = cur.fetchone()[0]
    if dt2c17 is None: dt2c17 = 0

    print('dt2c17:', dt2c17)

    ##2c17, nb
    cur.execute(("""
      		select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='2c17'  
    		and i.platform_type='nb'
           and s.cycle='2C 17'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?

        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    nb2c17 = cur.fetchone()[0]
    if nb2c17 is None: nb2c17 = 0

    print('nb2c17:', nb2c17)



    ##The version number is not clean, we just filter on platform
    ##1c17, DT
    cur.execute(("""
     		select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='1c17'  
    		and i.platform_type='dt'
           and s.cycle='1C 17'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?
           
        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    dt1c17 = cur.fetchone()[0]
    if dt1c17 is None: dt1c17=0

    print('dt1c17:',dt1c17)

    ##1c17, nb
    cur.execute(("""
        	select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='1c17'  
    		and i.platform_type='nb'
           and s.cycle='1C 17'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?

        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    nb1c17 = cur.fetchone()[0]
    if nb1c17 is None: nb1c17=0

    print('nb1c17:', nb1c17)

    #2c16, NB, DT
    cur.execute(("""
     	select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='2c16'  
    		and i.platform_type='dt'
           and s.cycle='2C 16'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?
    
        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    dt2c16 = cur.fetchone()[0]
    if dt2c16 is None: dt2c16=0

    print('dt2c16:', dt2c16)

    # 2c16, NB, DT
    cur.execute(("""
         	select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='2c16'  
    		and i.platform_type='nb'
           and s.cycle='2C 16'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?

        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    nb2c16 = cur.fetchone()[0]
    if nb2c16 is None: nb2c16=0

    print('nb2c16:', nb2c16)

    #3c16, NB, DT

    cur.execute(("""
    	select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='3c16'  
    		and i.platform_type='dt'
           and s.cycle='3C 16'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?

        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    dt3c16 = cur.fetchone()[0]
    if dt3c16 is None: dt3c16=0

    print('dt3c16:', dt3c16)

    # 3c16, NB, DT

    cur.execute(("""
      	select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='3c16'  
    		and i.platform_type='nb'
           and s.cycle='3C 16'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?

        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    nb3c16 = cur.fetchone()[0]
    if nb3c16 is None: nb3c16=0

    print('nb3c16:', nb3c16)

    #3c15, NB, DT

    cur.execute(("""
    
    
      	select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='3c15'  
    		and i.platform_type='dt'
           and s.cycle='3C 15'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?
        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    dt3c15 = cur.fetchone()[0]
    if dt3c15 is None: dt3c15=0

    print('dt3c15:', dt3c15)

    # 3c15, NB, DT

    cur.execute(("""


       	select sum(s.qty)
            FROM shipment s, install i, apps a, OptionCodes o
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
			and o.app_id = i.app_id
			and o.type = i.platform_type
			and o.cycle = ?
    		and o.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
    		and i.cycle='3c15'  
    		and i.platform_type='nb'
           and s.cycle='3C 15'
    	   and s.fisc_yr=?
    	   and s.fisc_mth = ?
        """), (current_cycle,app_name,fisc_yr,fisc_mth))
    nb3c15 = cur.fetchone()[0]
    if nb3c15 is None: nb3c15=0
    print('nb3c15:', nb3c15)


    #Consumer Win10 Jumpstart NPI (2C17) Unit in K, excl. CGK

    s2c17 = nb2c17 + dt2c17
    print('all2c17:',s2c17 )


    #Consumer Win10 Jumpstart NPI (1C17) Unit in K, excl. CGK

    s1c17 = nb1c17 + dt1c17
    print('all1c17:',s1c17 )

    #Consumer Win10 Jumpstart NPI (3C16) Unit in K, excl. CGK

    s3c16 = nb3c16 + dt3c16
    print('all3c16:', s3c16)

    #Softroll Win10 Jumpstart 3C15-2C16 Unit in K, excl. CGK

    s3c152c16 = nb2c16 + dt2c16 + nb3c15 + dt3c15
    print('allrest:', s3c152c16)

    print('all shipped', s2c17+s1c17+s3c16+s3c152c16)


    cur.close()

    conn.close()

    print('calc_shipment app ends')

    return