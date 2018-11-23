#!/usr/bin/python3
# -*- utf-8 -*-

import click
import json
import serial
from firebase import firebase

firebase_url = "https://parkeli-790b8.firebaseio.com/"
firebase = firebase.FirebaseApplication(firebase_url, None)



@click.command()
@click.option("--run", is_flag=True, help="Run app with config file and connected device")
@click.argument("configfile", type=click.File("r"), required=True)
@click.argument("device", required=True)

def cli(run, configfile, device):
    if run:
        uiid = json.loads(configfile.read())["uiid"]
        serialPort = serial.Serial(port = str(device), baudrate=115200, bytesize=8, stopbits=serial.STOPBITS_ONE)
        click.echo("Connected")
        
        while True:
                message = str(serialPort.readline()).split(">")[1][1:-2]
                click.echo(message)

                if message == "Entry":
                        firebase.patch("/parkings/" + uiid, {"free": firebase.get("/parkings/" + uiid + "/free", None)-1})

                elif message == "Exit":
                        firebase.patch("/parkings/" + uiid, {"free": firebase.get("/parkings/" + uiid + "/free", None)+1})