========================
Django Coding Club Site
========================
An amazing site for amazing people (and maybe some django users.)

=============================================
Setting up your local vagrant dev environment
=============================================

### 1

Download and Install (1) [vagrant](http://www.vagrantup.com) and (2) [virtualbox](https://www.virtualbox.org/).

### 2

Stand in the main directory (the same directory as the Vagrantfile) and run in your shell

    vagrant up
    vagrant ssh
    cd /vagrant
    sh vagrant/setup.sh

This will install and setup python and the database. In the future it is possible that we will want to use Fabric instead of SSHing into the vagrant.


### 3

(still inside vagrant machine) Start the server with

    python ny-py/manage.py runserver 0.0.0.0:8000

The site should now be running and accessible from your (host) machines browser

    localhost:8080
