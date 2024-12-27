import serial
import time
import requests
arduinoSerialData = serial.Serial('COM7',115200)


t = time.localtime()
current_time = time.strftime("%H", t)
p =int ((current_time))
print(p)


def sms1():
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS & message= your child entered bus and departed to school & language=english & route=p & numbers=9740671620"
    headers = {
        'authorization': "4x3CrQ8w8qX4ak577JiULwXK1ke1IhmE8oTjejcvGV74vg4yxacfL7GtM1jF",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

def sms2():
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS & message= your child entered bus and departed to home  & language=english & route=p & numbers=9740671620"
    headers = {
        'authorization': "4x3CrQ8w8qX4ak577JiULwXK1ke1IhmE8oTjejcvGV74vg4yxacfL7GtM1jF",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def sms3():
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS & message= Your child left the school & language=english & route=p & numbers=9740671620"
    headers = {
        'authorization': "4x3CrQ8w8qX4ak577JiULwXK1ke1IhmE8oTjejcvGV74vg4yxacfL7GtM1jF",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

def sms():
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS & message= Your child Entered school & language=english & route=p & numbers=9740671620"
    headers = {
        'authorization': "4x3CrQ8w8qX4ak577JiULwXK1ke1IhmE8oTjejcvGV74vg4yxacfL7GtM1jF",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

while (1 == 1):
    if (arduinoSerialData.in_waiting>0):
        mydata = arduinoSerialData.readline()
        print(mydata)
        #h = mydata.decode()
        #print(h)
        if (p > 9 and p < 10):
            #print("hii")
            #if (mydata == b'B6706AF3\r\n'):
                #sms()
            if (mydata == b'84C64883\r\n'):
                sms1()

        if (p>10 and p<11):
            if (mydata == b'B6706AF3\r\n'):
                sms()

        if ( p > 16 and p < 17 ):
            if (mydata == b'B6706AF3\r\n'):
                sms3()

        if (p > 17 and p < 18 ):
            if (mydata == b'84C64883\r\n'):
                sms2()
