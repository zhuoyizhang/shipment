
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

~~* Rule files:
    * 1c17_nb_loc.csv - app-loc mapping
    * 1c17_nb.csv  - app-platform mapping
    * 1c17_nb_loc.csv
    * 1c17_nb.csv~~




### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
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


~~* In Install table, we may want to replace type (new, refresh) column with cycle column~~

* Add 2c17 rule files

* Add OMEN

* Test numbers in old files

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


