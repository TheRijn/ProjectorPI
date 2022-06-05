from serialdevice import SerialDevice

STX = chr(0x02)
ETX = chr(0x03)


class ProjectorSerial(SerialDevice):
    def __init__(self, verbose: bool = False) -> None:
        serial_port = "/dev/serial0"
        baudrate = 9600

        super().__init__(serial_port, baudrate, verbose)

    def send_command(self, command: str, device_id: str = "ZZ") -> str:
        assert device_id in ["01", "02", "03", "04", "05", "06", "ZZ"]

        full_command = f"\x02AD{device_id};{command}\x03"

        return super().send_command(full_command)

    def power_on(self) -> None:
        self.send_command("PON")

    def power_off(self) -> None:
        self.send_command("POF")
