#consummer only
import urllib.request, urllib.parse, urllib.error
import csv
import sqlite3
import os.path


def create_tables():
   "function_docstring"
   print('create_tables starts')

   # Setup tables
   conn = sqlite3.connect('shipment.sqlite')
   cur = conn.cursor()

   cur.executescript('''


   DROP TABLE IF EXISTS Shipment;

   DROP TABLE IF EXISTS Install;
   DROP TABLE IF EXISTS OptionCodes;
   DROP TABLE IF EXISTS Apps;
   DROP TABLE IF EXISTS Platforms;



   CREATE TABLE IF NOT EXISTS Platforms (
       platform   TEXT,
       version  TEXT,
       category TEXT,
       PRIMARY KEY (platform, version)
   );

   CREATE TABLE IF NOT EXISTS Apps (
       id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
       name  TEXT UNIQUE
   );

   CREATE TABLE IF NOT EXISTS OptionCodes (
       id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
       app_id INTEGER,
       option_cd  TEXT,
       type    TEXT,
       FOREIGN KEY(app_id) REFERENCES Apps(id)
   );

   CREATE TABLE IF NOT EXISTS Install (
       type TEXT,
       app_id INTEGER,
       loc_id INTEGER,
       platform   TEXT,
       version   TEXT,
       platform_type   TEXT,
       cycle TEXT,
       FOREIGN KEY(app_id) REFERENCES Apps(id),
       FOREIGN KEY(loc_id) REFERENCES OptionCodes(id),
       FOREIGN KEY(platform, version) REFERENCES Platforms(platform, version),
       PRIMARY KEY(app_id,platform,loc_id)
   );

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


   cur.close()
   print('create_tables ends')

   return


