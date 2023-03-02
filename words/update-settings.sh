#!/env/bin/bash

sudo sed -i "s/DEBUG = True/DEBUG = False/" settings.py # Change DEBUG to False with Sed in settings.py
testp=$(curl http://checkip.amazonaws.com) # Curl server public IP and save to testp variable
sed -i "28s/\[\]/\['$testp']/" settings.py # Add server public IP to ALLOWED_HOSTS in settings.py
