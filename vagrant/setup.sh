#########
# Grab python and some other fun packages we need
########
sudo apt-get update
sudo apt-get install git libxml2 libxslt1-dev libevent-dev --assume-yes
sudo apt-get install python-pip python-dev libjpeg-dev libfreetype6-dev zlib1g-dev build-essential --assume-yes
sudo apt-get install postgresql-server-dev-9.1 postgresql --assume-yes

#########
# Install Requirements
########
sudo pip install -r requirements/local.txt


#########
# Create DB and Owner
########
sh vagrant/db.setup.sh

#########
# initial syncdb.
########
sudo python ny-py/manage.py syncdb --migrate
