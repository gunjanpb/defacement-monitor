#!/usr/bin/env python
import subprocess
import socket

BUF = 1024
port = 12345 #Change to anything
ip = localhost #Change to secondary's ip

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
except socket.error as err:
	print "socket creation failed with error %s" %(err)
	return
except socket.gaierror:
	print "There was an error resolving the host"
	return
while True:
	salt = sock.recv(BUF)
	#Use salt during hashing
	sums = subprocess.check_output('find -type f -exec md5sum '{}' \;'.split(), shell=True)
	sock.send(sums)	#md5sums sent
	if cl broken:
		break
