# latchwake
Turn on the multiple remote computers with Latch.
No need to open ports on the router
No need to open ports on the firewall
Easy and cheap

INSTALATION MANUAL
We will install the download manager wget to get the plugin and also python 3.0: 
apt-get install wget 
apt-get install python3 

We will enter the installation directory “/usr/local/src” and download our plugin: 
cd /usr/local/src 
wget https://github.com/maxssestepa/Latchwake/archive/master.zip  

We will unzip the downloaded file and rename the directory as "latchwake". Remember that the files in this directory have to belong to the user "root" to ensure the safety of the plugin: 
unzip master.zip 
rename Latchwake-master latchwake 

We adapt the appropriate user and permissions: 
cd latchwake 
chown root.root * 
chmod 550 latchwake latchwakeon.py install.py 

We will enter the latchwake plugin directory and execute the plugin “install” command: 
./install 
Configure the plugin with the pair code and mac-ddress.
