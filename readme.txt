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
Open the ESP32 as drive, and then copy the library sdcard.py 
into root directory.

 

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


 # Demonstrates ESP32 interface to MicroSD Card Adapter
 # Create a text file 
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
 

 Conclusion:

The experiment is successfully executed with ESP32, SD Card Module, and 64 GB micro-SD card

A “sample.txt” file is created, written  and then readback / printed the text via debug port.













https://youtu.be/08MXeM0Qb8Y?si=XZb9iozrt-WRAOat
