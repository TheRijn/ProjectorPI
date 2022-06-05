#! /usr/bin/env python3
from serial import Serial
from argparse import ArgumentParser
from time import sleep


# w == escape
# | == carriage return
POWER_SAVE_ON = "w1PSAV|"
POWER_SAVE_OFF = "w0PSAV|"
POWER_SAVE = "wpsav|"
INPUT = lambda x: f"{x}!"

EDIDS = {
    "automatic": 0,
    "1280x800": 14,
    "720p60": 34,
    "1080p60": 45,
}

ERRORS = {
    "E01": "Invalid input number",
    "E06": "Invalid switch attempt in this mode",
    "E10": "Invalid command",
    "E11": "Invalid preset number",
    "E12": "Invalid port number",
    "E13": "Invalid parameter",
    "E14": "Not valid for this configuration",
    "E17": "Invalid command for signal type",
    "E22": "Busy",
}

verbose = False


def send_command(command: str) -> str:
    with Serial("/dev/serial/by-id/usb-Extron_Product-if00", 9600, timeout=1) as ser:
        if verbose:
            print("Send:", command)

        ser.write(command.encode())
        # response = ser.readline().decode().strip()
        response = None

        while not (response := ser.readline()):
            pass
        response = response.decode().strip()

        if verbose:
            print("Resp:", response)
        if not response:
            print("no reponse")
            exit(1)
        if response[0] == "E":
            print(response, ERRORS.get(response, "Unknown"))
            exit(1)

    return response


def send_command_projector(command: str) -> str:
    with Serial("/dev/serial0", 9600, timeout=1) as ser:
        ser.write(command.encode())
        response = ser.readline()

        if response:
            print(response.decode())


def check_power_save():
    resp = send_command(POWER_SAVE)

    return int(resp)


def sleep_extron():
    send_command(POWER_SAVE_ON)


def wake():
    send_command(POWER_SAVE_OFF)


def change_input(input: int):
    send_command(INPUT(input))


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="increase output verbosity"
    )

    sleep_or_wake = parser.add_mutually_exclusive_group()
    sleep_or_wake.add_argument(
        "input",
        nargs="?",
        type=int,
        choices=[1, 2, 3, 4],
        help="wake and select input",
    )
    sleep_or_wake.add_argument("--sleep", action="store_true", help="put in sleep mode")
    args = parser.parse_args()

    verbose = args.verbose

    if args.input:
        send_command_projector("\x02ADZZ;PON\x03")
        wake()
        change_input(args.input)

        if verbose:
            print("Waking projector")
        #send_command_projector("\x02ADZZ;PON\x03")

    elif args.sleep:
        send_command_projector("\x02ADZZ;POF\x03")

        sleep_extron()
