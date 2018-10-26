import time
import datetime
import serial


from dBConnetion import open_connection,close_connection




def loop():
    while True:
        if datetime.datetime.now().minute % 5 == 0:
            print ("getting data...")
            serial_io()
            time.sleep(60)


def add_to_database(arr):
    my_db = open_connection()
    
    my_cursor = my_db.cursor()

    sql = "INSERT INTO outside (date_outside, time_outside, temp_outside) VALUES (%s,%s,%s)"
    my_cursor.execute(sql, arr)
    my_db.commit()
    print("sql sent : " + sql)
    close_connection(my_db)


def get_request(serial):
    print ("serial reading....")

    request = serial.readline()
    print ("serial reading is complete.")
    request = request.rstrip("\n")
    today = datetime.date.min
    arr = [time.strftime("%Y-%m-%d"),time.strftime("%H:%M"),request]
    print (time.strftime("%Y-%m-%d")+" "+time.strftime("%H:%M"))
    add_to_database(arr)
    print ("#########################newline#######################")


def send_request(serial):

    serial.write('1')
    get_request(serial)


def serial_io():
    send_request(ser)


ser = serial.Serial(
    'COM3', 9600
)
# print ser.is_open

time.sleep(2)
loop()
