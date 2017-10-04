#!/usr/bin/env python
import subprocess
import socket
import time

BUF = 1024
port = 12345 #Change to anything
ip = "localhost" #Change to secondary's ip
period = 15	#in seconds

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
except socket.error as err:
	print "socket creation failed with error %s" %(err)
	quit()
except socket.gaierror:
	print "There was an error resolving the host"
	quit()
while True:
	salt = sock.recv(BUF)
	#Use salt during hashing
	sums = subprocess.check_output("find -type f -exec md5sum '{}' \;", shell=True)
	print "hh{", sums, "}hh"
	sock.send(sums)	#md5sums sent
	time.sleep(period)
#	if cl broken:
#		break
