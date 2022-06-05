from doctest import REPORT_CDIFF
from serial import Serial


class SerialDevice:
    def __init__(
        self, serial_port: str, baudrate: int = 9600, verbose: bool = False
    ) -> None:
        self.serial_port: str = serial_port
        self.baudrate = baudrate
        self.verbose = verbose

    def send_command(self, command: str, verbose: bool = False) -> str:
        verbose = verbose or self.verbose

        with Serial(self.serial_port, self.baudrate, timeout=1) as s:
            if verbose:
                print("Send:", command)

            s.write(command.encode())

            response_raw = None

            count = 0
            while count < 10 and not (response_raw := s.readline()):
                pass

            if response_raw:
                response = response_raw.decode().strip()
            else:
                response = ""

            if verbose:
                print("Resp:", response)
            if not response:
                print("No response")

            return response
