# shipment

#prepare SWPOR rule file
#all apps in one file
App, Type, Platform

#prepare option code rule file
#all apps in one file

#diff the SWPOR files if they belong to the same cycle

git diff --word-diff=color --word-diff-regex=. 1c17-nb.csv 1c17-nb-test.csv


#run load_swpor.py
1c17-nb-loc.csv and 1c17-dt.csv are mandatory
note that loc files are different between nb and dt platform





July 3rd
#march data misses lots of location code.

install table,  new and refresh,   should I change them to cycle?
