#!/bin/bash
# Setup script for Raspberry Pi deployment
sudo apt update
sudo apt install -y python3-pip python3-venv chromium-browser
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
