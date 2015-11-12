
import socket
import sys
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
	print "failed"
	sys.exit()
print "socket create"

host="www.tenshine.org"
port = 80
try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "error"
    sys.exit()


print "ip address is ",host,"is",remote_ip

s.connect((remote_ip,port))

print "socket connect ",host,"on ip ",remote_ip

try:
    data = 'GET / HTTP/1.1\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; rv:39.0) Gecko/20100101 Firefox/39.0\nHost: www.tenshine.org\n\n'
    print data
    s.sendall(data)
except socket.error:
    print "failed"
    sys.exit()

print "message send success"

reply = s.recv(10240)
s.close()
print repr(reply)
