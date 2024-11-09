from machine import Pin, SPI
import sdcard, os

# Initialize SPI and SD card
spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(5, Pin.OUT)

try:
    sd = sdcard.SDCard(spi, cs)
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/sd")
    print("SD card mounted successfully.")

    # Write to a file on the SD card
    with open("/sd/test.txt", "w") as file:
        file.write("Hello from MicroPython! This is a test write operation.")
        print("Data written to /sd/test.txt.")

    # Read from the file
    with open("/sd/test.txt", "r") as file:
        content = file.read()
        print("Content of /sd/test.txt:", content)
        
    # Create a directory and write a file to it
    #os.mkdir("/sd/mydir")
    #with open("/sd/mydir/another_test.txt", "w") as file:
        #file.write("This is a file inside a folder!")
    
    # Append data to the file
    with open("/sd/test.txt", "a") as file:
        file.write("\nAppending some new data!")

    
    # Delete the file
    #os.remove("/sd/test.txt")
    #os.rmdir("/sd/...) to remove an empty directory 
    
    #list the files on the /sd
    print(os.listdir("/sd"))

    # Get filesystem statistics for the SD card
    stat = os.statvfs("/sd")
    # Calculate total capacity and available space
    total_space = stat[0] * stat[2]  # block size * total number of blocks
    free_space = stat[0] * stat[3]   # block size * number of free blocks

    # Print total and free space in bytes
    print("SD Card Capacity: {:.2f} MB".format(total_space / (1024 * 1024)))
    print("Available Space: {:.2f} MB".format(free_space / (1024 * 1024)))

    

except Exception as e:
    print("SD card initialization error:", e)
