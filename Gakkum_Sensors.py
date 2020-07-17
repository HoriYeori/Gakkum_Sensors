import sqlite3
import serial
import datetime

connect = sqlite3.connect("C:\Gakkum_Project\mysite\db.sqlite3")
cursor = connect.cursor()

Sensors = serial.Serial('COM4', 9600)

idx = 0
while (1):
    temp = Sensors.readline()
    humid = Sensors.readline()
    soil = Sensors.readline()
    dist = Sensors.readline()
    while (chr(temp[0]) == '0' and chr(humid[0]) == '0'):
        temp = Sensors.readline()
        humid = Sensors.readline()
        soil = Sensors.readline()
        dist = Sensors.readline()

    temp = int(temp)
    humid = int(humid)
    soil = int(soil)
    dist = int(dist)

    date = datetime.datetime.now()

    query = "INSERT INTO IITP_sensors (temperature, humidity, distance, soil_moisture, captured_date) VALUES (?, ?, ?, ?, ?)"
    data = (temp, humid, soil, dist, date)

    cursor.execute(query, data)
    connect.commit()