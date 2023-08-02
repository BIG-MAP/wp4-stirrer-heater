import time

import serial


class SerialDriver:
    def __init__(self, port: str):
        self.serial = serial.Serial(
            port=port,
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_EVEN,
            xonxoff=False,
            timeout=2,
            exclusive=True,
        )
        time.sleep(1)

    def send_command(self, command: str):
        self.serial.write((command + "\r\n").encode())
        self.serial.flush()

    def read_line(self) -> str:
        return self.serial.readline().decode().strip()

    def read_last_line(self) -> str:
        lines = self.serial.readlines()
        return lines[-1].decode().strip()

    def close(self):
        self.serial.close()
