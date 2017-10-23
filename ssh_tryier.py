#!/usr/bin/env python3

import paramiko

hosts = []
usernames = []
passwords = []
port = 22

for host in hosts:
    for username in usernames:
        for password in passwords:
            try:
                client = paramiko.SSHClient()
                client.load_system_host_keys()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host,port,username,password,timeout=5)
                client.close()
                print("Host: %s / User: %s / Password: %s, it\'s ok." %(host,username,password))
                error = False
                passed = True
                break

            except paramiko.ssh_exception.AuthenticationException as e:
                print("Host: %s / User: %s / Password: %s, invalid." %(host,username,password))
                error = False
                passed = False

            except Exception as e:
                print("Host: %s / %s" %(host,e))
                error = True
                passed = False
                break

        if error == True or passed == True:
            break
