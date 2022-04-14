import time
import paramiko 
import datetime

now = datetime.datetime.now()
# mention username and password 
user = "cisco" 
password = "cisco"
enable_password = "cisco"
# mention username and password 
port=22
f0 = open('/root/Cisco_switch_Backups/cisco_devices.txt')
for ip in f0.readlines():
      ip = ip.strip()
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(ip,port, user, password, look_for_keys=False)
      chan = ssh.invoke_shell()
      time.sleep(2)
      chan.send('enable\n')
      chan.send(enable_password +'\n')
      time.sleep(1)
      chan.send('term len 0\n')
      time.sleep(1)
      chan.send('sh run\n')
      time.sleep(20)
      output = chan.recv(999999)
      filename = "/root/Cisco_switch_Backups/Backup-"+str(ip)+"_"+str(now.month)+"_"+str(now.day)+"_"+str(now.year)+"_"+str(now.hour)+":"+str(now.minute)+".txt"
      f1 = open(filename, 'a')
      f1.write(output.decode("utf-8") )
      f1.close()
      ssh.close() 
      f0.close()
