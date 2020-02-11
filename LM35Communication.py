import serial
import time
from concurrent import futures
import sys
import io
import datetime
import pandas as pd

def key_interupt(ser):
    while True:
        key = input()
        if key == "q":
            ser.close()
            break
    return True

def get_LM35(ser, sio):
    header_info = ["Year", "Month", "Date", "Hour", "Minute", "Second", "Tempture"]
    accumulate = pd.DataFrame(columns = header_info)
    print(", ".join(header_info))
    cnt = 0
    while True:
        lm35_data = sio.readline()
        now = datetime.datetime.today()
        if cnt == 0:
            lm35_data = ""
            
        elif not now.second == past.second and not lm35_data == "":
            temp = lm35_data.strip("\r\n")
            buf = now.strftime("%Y, %m, %d, %H, %M, %S, ")+temp
            print(buf)
        past = now
        cnt += 1

def main():
    print("Let's read data.")
    ser = serial.Serial("/dev/ttyS3", 9600, timeout = 1)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

    

    print("Open COM Port")
    key_interuption = False
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        key_interuption = executor.submit(key_interupt, ser)
        executor.submit(get_LM35, ser, sio)
        if key_interuption:
            executor.shutdown()


    print("Accomplished")
    

if __name__ == "__main__":
    main()