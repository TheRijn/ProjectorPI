[![Build Status](https://drone.marijndoeve.nl/api/badges/Marijn/ProjectorPi/status.svg)](https://drone.marijndoeve.nl/Marijn/ProjectorPi)

# ProjectorPi

Projector is a personal tool I user to control my _Panasonic PT-RW330_ projector and _Extron IN1604 DTP_ scalar over serial using a Raspberry Pi.

## Build wheels

Building the project can be done using poetry. 

```shell
$ poetry build
```

## Install locally

```shell
$ pip install .
```

## Usage

Make sure the user is a member of the `dialout` group.

Wake projector and scaler and select input 2:

```shell
$ projectorpi 2
```

Put projector and scalar in sleep mode:

```shell
$ projectorpi --sleep
```