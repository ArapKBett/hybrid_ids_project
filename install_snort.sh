sudo apt-get update
sudo apt-get install -y snort
sudo snort -T -i eth0 -c /etc/snort/snort.conf
