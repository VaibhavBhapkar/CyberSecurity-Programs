import base64

def encrypted(key,message):
	cipher=[]
	for i in range(len(message)):
		keycurr=key[(i%len(key))]		
		ciphercurr=chr(ord(message[i])+ord(keycurr))
		cipher.append(ciphercurr)
	CipherText="".join(cipher)
	return CipherText
def decrypted(key,converted):
	plain=[]
	for i in range(len(converted)):
		keycurr=key[(i%len(key))]		
		plaincurr=chr(ord(converted[i])-ord(keycurr))
		plain.append(plaincurr)
	PlainText="".join(plain)
	return PlainText
def overloadtest(text1,text2,flag):
	if flag==True:
		val=encrypted(text1,text2)
		return val
	else:
		res=decrypted(text1,text2)
		return res	

key=raw_input("Enter Key:")
message=raw_input("Enter Message:")
cipher=overloadtest(key,message,True)
print "Cipher text of give text is :"+base64.urlsafe_b64encode(cipher)
result=overloadtest(key,cipher,False)
print "Plain text of cipher text is :"+result
