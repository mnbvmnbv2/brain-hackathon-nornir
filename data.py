import serial

ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    s = ser.read(1000)
    print(s)
