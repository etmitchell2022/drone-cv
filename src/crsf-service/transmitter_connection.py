import time

import serial

CRSF_ELRS_PORT = "/dev/tty.usbmodem00000000001B1"
ELRS_BAUDERATE = 420000


class TransmitterConnection:
    def __init__(self, port=CRSF_ELRS_PORT, baudrate=ELRS_BAUDERATE):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def __enter__(self):
        self.ser = serial.Serial(self.port, baudrate=self.baudrate, timeout=0.1)
        print("Opened serial port:", self.ser.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ser:
            self.ser.close()
            print("Closed serial port:", self.ser.name)

    def read_data(self, size=64):
        return self.ser.read(size)

    def read_continuously(self, duration=5):
        print(f"Reading data for {duration} seconds...")
        start_time = time.time()

        while time.time() - start_time < duration:
            data = self.ser.read(64)
            if data:
                print(f"Received: {data}")
                print(f"Hex: {data.hex()}")
            else:
                print("No data received")
            time.sleep(0.1)

    def close(self):
        if self.ser:
            self.ser.close()
            print("Closed serial port:", self.ser.name)


if __name__ == "__main__":
    with TransmitterConnection(CRSF_ELRS_PORT, ELRS_BAUDERATE) as tc:
        print("Single read:", tc.read_data())
        print("\nContinuous reading...")
        tc.read_continuously(duration=10)
