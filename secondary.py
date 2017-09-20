#!/usr/bin/env python

import socket
import os
import subprocess
import filecmp

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

cl, addr = s.accept()
toSend=''.join([random.choice(string.lowercase) for i in range(n)])
cl.send(toSend)	#Send random salt
sums_recd = cl.recv(BUF)	#BUF better be big, complete md5sums "file" received
if os.path(./md5sums).isfile():
	os.rename('md5sums', 'md5sums.old')
	new_sums = open("md5sums","w")
	new_sums.writelines(sums_recd.split('\n'))
	new_sums.close()
	filecmp.cmp("md5sums.old","md5sums")	#compares md5sums with md5sums.old
	delete old
else:
	new_sums = open("md5sums","w")
	new_sums.writelines(sums_recd.split('\n'))
	new_sums.close()

cl.close()