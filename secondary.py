#!/usr/bin/env python

import socket
import os
import subprocess
import filecmp
import time
import random
import string

BUF = 1024
port = 12345 #Change to anything
period = 15	#in seconds

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port)) #socket.gethostname()
sock.listen(1)

# def mysend(cl,msg,msglen):
# 	totalsent = 0
# 	while totalsent < msglen:
# 		sent = sock.send(msg[totalsent:])
# 		if sent == 0:
# 			raise RuntimeError("socket connection broken")
# 		totalsent = totalsent + sent
#
# def myreceive(cl,msg):
# 	chunks = []
# 	bytes_recd = 0
# 	while bytes_recd < :
# 		chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
# 		if chunk == '':
# 			raise RuntimeError("socket connection broken")
# 		chunks.append(chunk)
# 		bytes_recd = bytes_recd + len(chunk)
# 	return ''.join(chunks)

cl, addr = sock.accept()
while True:
	toSend=''.join([random.choice(string.lowercase) for i in range(5)])
	cl.send(toSend)	#Send random salt
	sums_recd = cl.recv(BUF)	#BUF better be big, complete md5sums "file" received
	print "[{", sums_recd, "]}"
	if os.path.isfile("./md5sums"):
		os.rename('md5sums', 'md5sums.old')
		new_sums = open("md5sums","w")
		new_sums.writelines([sums_recd])
		new_sums.close()
		if not filecmp.cmp("md5sums.old","md5sums"):
			print "Files modified!!!"
		os.remove("md5sums.old")
	else:
		new_sums = open("md5sums","w")
		new_sums.writelines(sums_recd.split('\n'))
		new_sums.close()
	time.sleep(period)
#	if cl broken:
#		break
cl.close()