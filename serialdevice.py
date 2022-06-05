from doctest import REPORT_CDIFF
from serial import Serial


class SerialDevice:
    def __init__(
        self, serial_port: str, baudrate: int = 9600, verbose: bool = False
    ) -> None:
        self.serial_port: str = serial_port
        self.baudrate = baudrate
        self.verbose = verbose
        self.prefix = ""

    def send_command(self, command: str) -> str:

        with Serial(self.serial_port, self.baudrate, timeout=1) as s:
            if self.verbose:
                print(self.prefix, "send:", command)

            s.write(command.encode())

            response_raw = None

            count = 0
            while count < 10 and not (response_raw := s.readline()):
                pass

            if response_raw:
                response = response_raw.decode().strip()
            else:
                response = ""

            if self.verbose:
                print(self.prefix, "resp:", response)
            if not response:
                print(self.prefix, "No response")

            return response
