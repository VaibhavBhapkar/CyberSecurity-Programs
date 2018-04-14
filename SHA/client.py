import hashlib
import socket
import time
if __name__=="__main__":
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host="127.0.0.1"
	port=12345
	print "Connecting to Server.."
	s.connect((host,port))
	try:
		msg=raw_input("Enter Message: ")
		s.send(str(msg))
		msgdigest=hashlib.sha1(msg).hexdigest()
		print "Sending Digest :"+str(msgdigest)
		time.sleep(2)
		s.send(str(msgdigest))
	finally:
		print "Closing Socket..."
		s.close()
