#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install unattended-upgrades -y
sudo apt-get install ufw -y
sudo ufw allow ssh
sudo dpkg-reconfigure --priority=low unattended-upgrades
sudo ufw enable