#!/bin/bash

sudo apt update && sudo apt install -y make python3-pip

sudo python3 -m pip install --upgrade pip
sudo pip install -r requirements-dev.txt

