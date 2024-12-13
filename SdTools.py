import os
from machine import Pin,SPI
from sdc import SDCard


import machine
#print(sd)

#sd = sdcard.SDCard(SPI(2,sck=Pin(41), mosi=Pin(40), miso=Pin(42), Pin(39)))


def Init():
    s = SPI(1)
    s.init(miso=Pin(42),mosi=Pin(40),sck=Pin(41))
    sd= SDCard(s,Pin(39))

    os.VfsFat(sd)
    os.mount(sd,'/sd')
    

if __name__ == '__main__':
    Init()


    