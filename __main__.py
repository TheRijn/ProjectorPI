#! /usr/bin/env python3
from argparse import ArgumentParser
from projector import ProjectorSerial
from extron import ExtronSerial

verbose = False


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

    proj = ProjectorSerial()
    extr = ExtronSerial()

    if args.input:
        proj.power_on()
        extr.wake()
        extr.change_input(args.input)

    elif args.sleep:
        proj.power_off()
        extr.sleep()
