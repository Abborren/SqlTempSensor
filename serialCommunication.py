import time
import datetime
import serial


# import dBConnetion




def loop():
    while True:
        if datetime.datetime.now().minute % 1 == 0:
            print ("getting data...")
            serial_io()
            time.sleep(59)


# def add_to_database(request):
#   my_db = dBConnetion.my_db
#  my_cursor = my_db.cursor()

#  sql = "INSERT INTO weather_outside (date, time,temp,humidity) VALUES (%s, %s,%s,%s)"

# my_cursor.execute(sql, request)

# my_db.commit()


def get_request(serial):
    print ("serial reading after this")

    request = serial.readline()
    print ("serial reading is done")
    print (request)
    # request_split = request.split(',')
    # request.array([datetime.datetime.date(), time.time.utcnow(), request_split[0], request_split[1]])
    # add_to_database(request)
   # print (request.array([datetime.datetime.date(), time.time.utcnow(), request]))


def send_request(serial):

    serial.write('1')
    get_request(serial)


def serial_io():
    send_request(ser)


ser = serial.Serial(
    'COM3', 9600
)
print ser.is_open


time.sleep(2)
loop()
