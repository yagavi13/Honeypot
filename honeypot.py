import socket
import atexit
LHOST='0.0.0.0'
LPORT=21
RHOST=socket.gethostbyname("localhost")
RPORT=35393
BANNER='Ubuntu 14.04 LTS\nlogin: '
TIMEOUT=10
def main():
print ('[*] Honeypot starting on ' + LHOST + ':' + str(LPORT))
atexit.register(exit_handler)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listener.bind((LHOST,LPORT))
listener.listen(5)
while True:
(insock,address) = listener.accept()
insock.settimeout(TIMEOUT)
print ('[*] Honeypot connection from '+address[0] + ':' +str(address[1])+'on port'+
str(LPORT))sss
try:
insock.send(BANNER.encode('utf-8'))
data=insock.recv(4096)
except(socket.error):
32
sendlog(address[0],'Error:')
else:
sendlog(address[0],data)
finally:
insock.close()
def sendlog(fromip, message):
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((RHOST,RPORT))
s.send(f"'IP:' + fromip + 'Port:' +str(LPORT)+'|'+message.replace('\r\n','')".encode())
s.close()
def exit_handler():
print('\n[*] Honeypot is shutting down!')
listener.close()
listener=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if name == 'main':
try:
main()
except KeyboardInterrupt:
pass
