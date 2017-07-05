#consummer only
import urllib.request, urllib.parse, urllib.error
import csv
import sqlite3


def calc_shipment_app(app_name):
    print('calc_shipment app starts:', app_name)

    ## read csv raw file

    conn = sqlite3.connect('shipment.sqlite')
    cur = conn.cursor()


    ##The version number is not clean, we just filter on platform
    ##1c17, DT
    cur.execute(("""
    select sum(s.qty)
        FROM shipment s, install i, apps a
        WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
        AND s.OPERATING_SYSTEM LIKE ('%10%')
		AND upper(s.platform) = upper(i.platform)
		and i.option_cd = s.prod_opt_cd
		and a.id = i.app_id
		and a.name=?
		and i.cycle='1c17'  
		and i.platform_type='dt'
       and s.cycle='1C 17'
	   and s.fisc_yr=2017
	   and s.fisc_mth = 5
           
    """),(app_name,))
    dt1c17 = cur.fetchone()[0]
    print('dt1c17:',dt1c17)

    ##1c17, nb
    cur.execute(("""
        select sum(s.qty)
            FROM shipment s, install i, apps a
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
    		and i.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
		    and i.cycle='1c17'  
    		and i.platform_type='nb'
           and s.cycle='1C 17'
    	   and s.fisc_yr=2017
    	   and s.fisc_mth = 5

        """),(app_name,))
    nb1c17 = cur.fetchone()[0]
    print('nb1c17:', nb1c17)

    #2c16, NB, DT
    cur.execute(("""
     select sum(s.qty)
        FROM shipment s, install i, apps a
        WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
        AND s.OPERATING_SYSTEM LIKE ('%10%')
		AND upper(s.platform) = upper(i.platform)
		and i.option_cd = s.prod_opt_cd
		and a.id = i.app_id
		and a.name=?
		and i.cycle='2c16'  
		and i.platform_type='dt'
       and s.cycle='2C 16'
	   and s.fisc_yr=2017
	   and s.fisc_mth = 5
    
    """),(app_name,))
    dt2c16 = cur.fetchone()[0]
    if dt2c16 is None: dt2c16=0

    print('dt2c16:', dt2c16)

    # 2c16, NB, DT
    cur.execute(("""
         select sum(s.qty)
            FROM shipment s, install i, apps a
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
    		and i.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
		    and i.cycle='2c16'  
    		and i.platform_type='nb'
           and s.cycle='2C 16'
    	   and s.fisc_yr=2017
    	   and s.fisc_mth = 5

        """),(app_name,))
    nb2c16 = cur.fetchone()[0]
    if nb2c16 is None: nb2c16=0

    print('nb2c16:', nb2c16)

    #3c16, NB, DT

    cur.execute(("""
    select sum(s.qty)
            FROM shipment s, install i, apps a
            WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
            AND s.OPERATING_SYSTEM LIKE ('%10%')
    		AND upper(s.platform) = upper(i.platform)
    		and i.option_cd = s.prod_opt_cd
    		and a.id = i.app_id
    		and a.name=?
		    and i.cycle='3c16'  
    		and i.platform_type='dt'
           and s.cycle='3C 16'
    	   and s.fisc_yr=2017
    	   and s.fisc_mth = 5

    """),(app_name,))
    dt3c16 = cur.fetchone()[0]
    print('dt3c16:', dt3c16)

    # 3c16, NB, DT

    cur.execute(("""
      select sum(s.qty)
              FROM shipment s, install i, apps a
              WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
              AND s.OPERATING_SYSTEM LIKE ('%10%')
      		AND upper(s.platform) = upper(i.platform)
      		and i.option_cd = s.prod_opt_cd
      		and a.id = i.app_id
      		and a.name=?
		    and i.cycle='3c16'  
      		and i.platform_type='nb'
             and s.cycle ='3C 16'
      	   and s.fisc_yr=2017
      	   and s.fisc_mth = 5

      """),(app_name,))
    nb3c16 = cur.fetchone()[0]
    print('nb3c16:', nb3c16)

    #3c15, NB, DT

    cur.execute(("""
    
    
      select sum(s.qty)
              FROM shipment s, install i, apps a
              WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
              AND s.OPERATING_SYSTEM LIKE ('%10%')
      		AND upper(s.platform) = upper(i.platform)
      		and i.option_cd = s.prod_opt_cd
      		and a.id = i.app_id
      		and a.name=?
		    and i.cycle='3c15'  
      		and i.platform_type='dt'
             and s.cycle='3C 15'
      	   and s.fisc_yr=2017
      	   and s.fisc_mth = 5
    
    """),(app_name,))
    dt3c15 = cur.fetchone()[0]
    if dt3c15 is None: dt3c15=0

    print('dt3c15:', dt3c15)

    # 3c15, NB, DT

    cur.execute(("""


       select sum(s.qty)
               FROM shipment s, install i, apps a
               WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
               AND s.OPERATING_SYSTEM LIKE ('%10%')
       		AND upper(s.platform) = upper(i.platform)
       		and i.option_cd = s.prod_opt_cd
       		and a.id = i.app_id
       		and a.name=?
		    and i.cycle='3c15'  
       		and i.platform_type='nb'
              and s.cycle='3C 15'
       	   and s.fisc_yr=2017
       	   and s.fisc_mth = 5

     """),(app_name,))
    nb3c15 = cur.fetchone()[0]
    if nb3c15 is None: nb3c15=0
    print('nb3c15:', nb3c15)

    #Consumer Win10 Jumpstart NPI (1C17) Unit in K, excl. CGK

    s1c17 = nb1c17 + dt1c17
    print('all1c17:',s1c17 )

    #Consumer Win10 Jumpstart NPI (3C16) Unit in K, excl. CGK

    s3c16 = nb3c16 + dt3c16
    print('all3c16:', s3c16)

    #Softroll Win10 Jumpstart 3C15-2C16 Unit in K, excl. CGK

    s3c152c16 = nb2c16 + dt2c16 + nb3c15 + dt3c15
    print('s3c152c16:', s3c152c16)



    cur.close()

    conn.close()

    print('calc_shipment app ends')

    return