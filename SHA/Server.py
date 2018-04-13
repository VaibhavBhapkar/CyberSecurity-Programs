import hashlib
import socket
if __name__=="__main__":
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host="127.0.0.1"
	port=12345
	print "Starting Server.."
	s.bind((host,port))
	s.listen(1)
	print "Waiting for connection.."
	conn,add=s.accept()
	try:
		print "Got connection from",add
		rcvdata=conn.recv(1024)		
		print "Recieved Message: "+rcvdata
		rcvhash=conn.recv(1024)
		print "Recieved Hash: "+rcvhash
	finally:
		digest=hashlib.sha1(rcvdata).hexdigest()
		if rcvhash==str(digest):
			print "Unaltered Message.."
		else:
			print "Message is altered.."
		print "Stopping Server ..."
		s.close()


	
