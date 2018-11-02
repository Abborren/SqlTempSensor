import datetime
import os
import glob
import time

from dBConnetion import open_connection, close_connection


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def loop():
    while True:
        if datetime.datetime.now().minute % 5 == 0:
            print ("getting data...")
            get_request()
            time.sleep(60)


def add_to_database(arr):
    my_db = open_connection()
    my_cursor = my_db.cursor()

    sql = "INSERT INTO inside (date, time, temp) VALUES (%s,%s,%s)"
    my_cursor.execute(sql, arr)
    my_db.commit()
    print("sql sent : " + sql)
    close_connection(my_db)


def get_request():
    request = 0
    for x in range(5):

        temp_reading = get_reading()
        if x == 0:
            request = temp_reading
        else:
            request = (request + temp_reading) / 2
        time.sleep(1)

    arr = [time.strftime("%Y-%m-%d"), time.strftime("%H:%M"), request]
    add_to_database(arr)
    print arr
    print ("#########################newline#######################")


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def get_reading():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


time.sleep(2)
loop()
