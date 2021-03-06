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
                message = str(serialPort.readline().replace("\n", ""))
                click.echo(message)

                if message == '["00bee9d50005/zavory/", "Entry"]':
                        firebase.patch("/parkings/" + uiid + "/free/actual/", {"free": firebase.get("/parkings/" + uiid + "/free/actual/free", None)-1})

                elif message == '["00bee9d50005/zavory/", "Exit"]':
                        firebase.patch("/parkings/" + uiid + "/free/actual", {"free": firebase.get("/parkings/" + uiid + "/free/actual/free", None)+1})

                elif message == '["04962d957d42/A0", "full"]':
                        freeplace(uiid, "A0", "full")

                elif message == '["04962d957d42/A0", "free"]':
                        freeplace(uiid, "A0", "free")


                elif message == '["7bd09a0a9156/A1", "full"]':
                        freeplace(uiid, "A1", "full")


                elif message == '["7bd09a0a9156/A1", "free"]':
                        freeplace(uiid, "A1", "free")


                elif message == '["698f65464f40/A2", "full"]':
                        freeplace(uiid, "A2", "full")

                elif message == '["698f65464f40/A2", "full"]':
                        freeplace(uiid, "A2", "free")


def freeplace(uiid, place, state):
        firebase.patch("/parkings/" + uiid + "/free/places", {place: state})