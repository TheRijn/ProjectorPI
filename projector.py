from serial import Serial

STX = chr(0x02)
ETX = chr(0x03)

if __name__ == "__main__":
    with Serial("/dev/ttyAMA0", 9600, timeout=1) as ser:
        ser.write((STX + "ADZZ" + ";" + "PON" + ETX).encode())
        while not (response := ser.readline()):
            pass
        print(response)
                
