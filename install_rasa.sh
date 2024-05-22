#!/bin/bash

# Commandes d'installation de Rasa
echo "Installation de Rasa..."
apt-get update
apt-get install -y python3-pip
pip3 install rasa
