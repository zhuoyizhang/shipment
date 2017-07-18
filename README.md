
# Shipment

This project calculates the monthly shipment data for each CEPS application.

## Getting Started

This project needs Python 3.6, PyCharm and Sqlite browser
### Prerequisites

The following inputs files are needed for the calculation.

* Latest version of the SWPOR file for DT and NB
    
    * Excel 1 for NB
    * Excel 2 for DT, 1c17 cDT_SWPOR_Matrix_2017_02_06.xlsx
* Shipment raw data of that month
    
    * Units_Final_xxxxxx.csv

* Configure swpor.conf




### swpor.conf



```
[1c17]
shipment=Units_Final_2017_04_06_raw.csv
apps=HP Orbit,HP JumpStart,HP JumpStart Apps,HP Audio Switch


[1c17.dt]

filename ='1c17 cDT_SWPOR_Matrix_2017_02_06.xlsx'

#platform
startCol=O
endCol=AK
exclude=Q,T,AE
cyclerow=2
platformrow=3

#option code
startCol_loc=AM
endCol_loc=CN
exclude_loc=
optioncode_row=7
```



## Deployment

Run main.py to start


## Authors

* **Zhuoyi Zhang** - *Initial work* 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Notes

* diff the SWPOR files if they belong to the same cycle

````
git diff --word-diff=color --word-diff-regex=. 1c17-nb.csv 1c17-nb-test.csv
````



## To Do

~~* Load 3c16, 1c17, 2c17 together~~
~~* Add OMEN~~
~~* High: defect - OMEN has 1c17 number*~~
* Test numbers in old files
* How to deal 3c16&1c17 softroll?
~~* Fix getCycle()~~
~~* 3c16 option code file has JumpStart apps~~
* Display result in Juypter Notebook style
~~* refactor fisc_yr and fisc_mth~~
* refactor shipment.py by using column name when loading units

## Assumption

* Use the latest version of SWPOR of a cycle
* Combine the the SWPOR of all cycles, 3c16, 1c17, 2c17 etc.
* Refresh = 1 cycle down
* Softroll does not change cycle


## Known Issues

* March shipment units miss lots of location_code.  The query has to be modified for this exception

```
    select sum(qty)
        FROM shipment s, install i, apps a
        WHERE s.PRFT_CTR_LVL_5_NM not in ('China Local Sales','Germany Sales','Korea Local Sales')
        AND s.OPERATING_SYSTEM LIKE ('%10%')
		AND upper(s.platform) = upper(i.platform)
		--and i.location_cd = s.prod_opt_cd
		and a.id = i.app_id
		and a.name='HP JumpStart'
		and i.cycle='3c16'  
		and i.platform_type='dt'
        and s.cycle='3C 16'
	    and s.fisc_yr=2017
	    and s.fisc_mth = 5

```

```
Lollipop 1.0 (HP x2 Detachable 10) / Intel / eMMC, xxxx
We removed the , from raw data.

```

```
Clean the SWPOR by changing the label of 'Refresh' for 3c15 cycle
It requires to modify the SWPOR before running the program

```

```
Option code ramp up issue
3c16   option code:  a,b,c
1c17   option code:  a,b,c,d
when I calculate 3c16, use a,b,c
when I calculate 1c17,  use a,b,c,d

```