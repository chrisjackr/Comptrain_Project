#WOD_PROJECT

#import requests as re
import requests_html
import sqlite3
from sqlite3 import Error
import os
import datetime

def date_convert(date):
    #converts MM.DD.YYYY to YYYY-MM-DD HH:MM:SS.SSS
    new_date = '{}-{}-{} 00:00:00.000'.format(date[-4:],date[:2],date[3:5])
    return new_date

def scrape_data(url,xpath):
    #loads webpage and scrapes workout
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    session = requests_html.HTMLSession()
    r = session.get(url,headers=headers)
    r.html.render(sleep=5, timeout=10)
    for item in r.html.xpath(xpath):
        items_string = item.text
    items_list = items_string.split('\n')
    print(items_list)

    try:
        weekday = items_list[0].split('//')[0].strip()
        date = items_list[0].split('//')[1].strip()
        #print(weekday,date)
        items_list[0] = date_convert(date)
        items_list.insert(0,weekday)
        con = ' \n '.join(items_list[2:])
        items_list = items_list[0:2] + [con]
        #print(items_list)
        #print(items_list[2])
    except:
        con = ' \n '.join(items_list)
        now = datetime.datetime.today()
        weekday = now.strftime('%A')
        date = now.strftime('%Y-%m-%d')
        items_list = [weekday,date,con]
        print(items_list,'\n')


    return items_list

def create_connection(db_file,items):
    # saves workout in database
    #print((items[0],items[1][:10],items[2]))
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        #print('SQLite3 version: '+sqlite3.version)
        conn.execute('''
          CREATE TABLE IF NOT EXISTS wods_table
          ([Weekday] TEXT, [Date] TEXT, [WOD] TEXT)
          ''')
        conn.execute('''INSERT INTO wods_table (Weekday, Date, WOD) VALUES ("{}","{}","{}")'''.format(items[0],items[1][:10],items[2]))
        conn.commit()
        print('Date and workout added.')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    print('\n=== COMPTRAIN SCRAPE STARTED ===\n')
    items = scrape_data('https://comptrain.co/wod/', '//*[@id="wod"]/div[2]/div[1]')
    database = os.path.normpath(r"C:\Users\cjr19\Python\Projects\Comptrain_Project\comptrain_wods.db")
    create_connection(database,items)
    print('\nProcess Complete.\n')