
# Shipment

This project calculates the monthly shipment data for each CEPS application.

## Getting Started

This project needs Python 3.6, PyCharm and Sqlite browser
### Prerequisites

The following inputs files are needed for the calculation.

* Latest version of the SWPOR file for DT and NB
    
    * Excel 1 for NB
    * Excel 2 for DT
* Shipment raw data of that month
    
    * Units_Final_xxxxxx.csv

* Rule files:
    * 1c17_nb_loc.csv - app-loc mapping
    * 1c17_nb.csv  - app-platform mapping
    * 1c17_nb_loc.csv
    * 1c17_nb.csv




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

* March data misses lots of location code, the numbers would not be correct.


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

