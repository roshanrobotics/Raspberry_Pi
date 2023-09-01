from smbus import SMBus
addr = 0X8 #bus address
#bus = SMBus(1) #indicate ls /dev/*i2c*  i2d-1
bus = bus.write_byte_data(address,0x30,0x03)
numb = 1

print ('enter 1 for on or 0 for off')

while numb == 1:
    ledstate =input(">>>>   ")
    if ledstate == "1":
        bus.write_byte(addr, 0x1)
    elif ledstate == "0":
        bus.write_byte(addr,0x0)
    else:
        numb = 0
