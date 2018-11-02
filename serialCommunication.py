import time
import datetime
import serial

from dBConnetion import open_connection, close_connection


def loop():
    while True:
        if datetime.datetime.now().minute % 5 == 0:
            print ("getting data...")
            request_reading(ser)
            time.sleep(60)


def add_to_database(arr):
    my_db = open_connection()

    my_cursor = my_db.cursor()

    sql = "INSERT INTO outside (date, time, temp) VALUES (%s,%s,%s)"
    my_cursor.execute(sql, arr)
    my_db.commit()
    print("sql sent : " + sql)
    close_connection(my_db)


def get_reading(serial):
    # print ("serial reading....")

    request = serial.readline()
    # print ("serial reading is complete.")
    request = request.rstrip("\n")

    return request


def request_reading(serial):
    request = 0
    for x in range(5):

        serial.write('1')
        temp_reading = get_reading(serial)
        if x == 0:
            request = temp_reading
        else:
            request = (float(request) + float(temp_reading)) / 2
        time.sleep(1)

    arr = [time.strftime("%Y-%m-%d"), time.strftime("%H:%M"), request]
    add_to_database(arr)
    print arr
    print ("#########################newline#######################")


ser = serial.Serial(
    'COM3', 9600
)
# print ser.is_open

time.sleep(2)
loop()
