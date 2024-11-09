SD Card module provides “micro-SD card socket”, for inserting 
the memory card and then provides SPI interface 
pins (MOSI = GPIO23, MISO = GPIO19, SCLK = GPIO18 and CS = GPIO5),
for connecting it into ESP32 board.

SD Card module converts the +5VDC supply into 3.3VDC using AM1117,

3.3VDC regulator and converts the 5VDC logic Pins into 3.3VDC 
logic pins by using “74ABT125PW, Quad Buffer Tri state logic 
converter”.

The micro-SD card adapter should be powered and operated with 5VDC.
the microSD card needs 3.3v 

This experiment uses an 64GB micro-SD card and it must be formatted 
(FAT32) 

Step 5: Python Program – SD Card Interface Module

 Python Program – SD Card Interface Module
Open the ESP32 as drive, and then copy the library into root directory.

 

MicroPython implements a Unix-like Virtual File System (VFS) layer.
All mounted filesystems are combined into a single virtual filesystem, 
starting at the root /. Filesystems are mounted into directories in this
structure, and at startup the working directory is changed to where
the primary filesystem is mounted.

The main advantage of the FAT filesystem is that it can be accessed 
over USB MSC on supported boards without any additional drivers required
on the host PC.

Download and store the MicroPython “sdcard.py” library into ESP32.

The file open functionality open(), can take following arguments 
for write, read and append a file.

w -- Open a file for writing the ASCII text. 
     If a file is already existing, then it rewrites the file.

r -- Open a file for reading the ASCII text.

a -- Open a file for appending the ASCII text at the end.

wb -- Open a file for writing binary data.

rb -- Open a file for reading binary data.

MicroPython SPl, sdcard and os libraries are used for constructing 
the experiment.



During startup, the SPI bus and SD card is initialized.

Initially a “sample.txt” file is created / opened with FILE_WRITE option.

If file open is success, then the program writes running numbers (0 to19), into “sample.txt”, and then closes.

The program once again opens the “sample.txt” with FILE_APPEND option, and appends a text at the end.

Then the program once again opens the “sample.txt” with FILE_READ option, reads the “sample.txt” and send data to the debug port, which prints text on connected debug terminal.



'''
 # Demonstrates ESP32 interface to MicroSD Card Adapter
 # Create a text file and write running numbers.
 # Open text file, read and print the content on debug port
   
 * The ESP32 pin connections for MicroSD Card Adapter SPI
 
 # MicroSD Card Adapter Power Pins
 * MicroSD VCC pin to ESP32 +5V
 * MicroSD GND pin to ESP32 GND
 
 # MicroSD SPI Pins
 * MicroSD MISO pin to ESP32 GPIO19
 * MicroSD MOSI pin to ESP32 GPIO23
 * MicroSD SCK pin to ESP32 GPIO18
 * MicroSD CS pin to ESP32 GPIO5
 
 Name:- M.Pugazhendi
 Date:-  20thOct2021
 Version:- V0.1
 e-mail:- muthuswamy.pugazhendi@gmail.com
'''
import machine
from machine import Pin, SPI, SoftSPI
import sdcard
import os
 
toggle = 0
 
#Initialize the onboard LED as output
led = machine.Pin(2,machine.Pin.OUT)

# Toggle LED functionality
def BlinkLED(timer_one):
    global toggle
    if toggle == 1:
        led.value(0)
        toggle = 0
    else:
        led.value(1)
        toggle = 1

# Initialize the SD card
spi=SoftSPI(1,sck=Pin(18),mosi=Pin(23),miso=Pin(19))
sd=sdcard.SDCard(spi,Pin(5))

# Create a instance of MicroPython Unix-like Virtual File System (VFS),
vfs=os.VfsFat(sd)
 
# Mount the SD card
os.mount(sd,'/sd')

# Debug print SD card directory and files
print(os.listdir('/sd'))

# Create / Open a file in write mode.
# Write mode creates a new file.
# If  already file exists. Then, it overwrites the file.
file = open("/sd/sample.txt","w")

# Write sample text
for i in range(20):
    file.write("Sample text = %s\r\n" % i)
    
# Close the file
file.close()

# Again, open the file in "append mode" for appending a line
file = open("/sd/sample.txt","a")
file.write("Appended Sample Text at the END \n")
file.close()

# Open the file in "read mode". 
# Read the file and print the text on debug port.
file = open("/sd/sample.txt", "r")
if file != 0:
    print("Reading from SD card")
    read_data = file.read()
    print (read_data)
file.close()

# Initialize timer_one. Used for toggling the on board LED
timer_one = machine.Timer(0)

# Timer one initialization for on board blinking LED at 200mS interval
timer_one.init(freq=5, mode=machine.Timer.PERIODIC, callback=BlinkLED)
Attachments
download {{ file.name }}sdcard.pyDownload
Step 6: Conclusion

 Conclusion
 Conclusion
The experiment is successfully executed with ESP32, SD Card Module, and 8GB micro-SD card

A “sample.txt” file is created, written with running numbers and then readback / printed the text via debug port.

Step 7: Results Video and Links

 Results Video and Links
Please Visit You Tube for the Videos:,

Visit the "VESZLE - The Art Of Electronics" you tube channel for further information and videos. https://www.youtube.com/channel/UCY4mekPLfeFinbQH...

ESP32 -- Micro SD Card Implementation video

https://youtu.be/08MXeM0Qb8Y










https://youtu.be/08MXeM0Qb8Y?si=XZb9iozrt-WRAOat