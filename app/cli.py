#!/usr/bin/python3
# -*- utf-8 -*-

import click
import json
import serial


@click.command()
@click.option("--run", is_flag=True, help="Run app with config file and connected device")
@click.argument("configfile", type=click.File("r"), required=True)

def cli(run, configfile):
    if run:
        serialPort = serial.Serial(port = "COM4", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        print(serialPort.readline())