# cisco_backup

Script created to take running config backup of cisco devices provided in inout file

Error: No URLs in mirrorlist
Solution:
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*

To Create Virtual environment:
python3 -m venv .

To activate virtual env:
source bin/activate

To Install paramiko Library:
python -m pip install paramiko

Input file of script:
/root/Cisco_switch_Backups/cisco_devices.txt

Run Script:
/root/Cisco_switch_Backups/bin/python3 /root/Cisco_switch_Backups/Script.py

To See lst of crons:
crontab -l

Edit crons:
crontab -e
