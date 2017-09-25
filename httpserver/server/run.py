# -*- coding: utf-8 -*-
import socket
import os

def parser_user_agent(string):
	unuse,pattern,after_pat=string.partition("User-Agent: ")
	del unuse, pattern
	return after_pat[0:after_pat.find("\n")]


def parser_url(url,client_socket,request_string):
	if url=="/":
		client_socket.send("HTTP/1.1 200 OK\r\n\r\n"+"Hello mister!\nYou are: "+parser_user_agent(request_string)+"\n") 
		return

	if url=="/test/":
		client_socket.send("HTTP/1.1 200 OK\r\n\r\n"+request_string)  #send string to the socket
		return
	if url=="/media/":
		directory="./media"
		files=os.listdir(directory)
		client_socket.send("HTTP/1.1 200 OK\r\n\r\n")
		for name in files:
			client_socket.send(name+"\n")
		return 
	if url.count("/")>2:
		client_socket.send("HTTP/1.1 404 Not Found\r\n\r\n"+"Page not found\n")
		return
	try:
		file=open("."+url,'r')
	except IOError as e:
		client_socket.send("HTTP/1.1 404 Not Found\r\n\r\n"+"File not found\n")
	else:
		client_socket.send("HTTP/1.1 200 OK\r\n\r\n"+file.read())
		


def parser_request_dirs(request):
	unuseble,pattern,after_pat=request.partition("GET ")
	del pattern,unuseble
	way=after_pat[0:after_pat.find("HTTP")-1]
	return way
	




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #linking our socket with definite host and port
server_socket.listen(5)  #turn on listening mode for socket with length of queue = 5

print 'Started'

while 1:
    try:
        (client_socket, adress) = server_socket.accept()
        print 'Got new client', client_socket.getsockname(),adress  #return the socket's own adress (host,port)
        request_string = client_socket.recv(2048)  #Receive data from the socket with 2048 size of buffer
        parser_url(parser_request_dirs(request_string),client_socket,request_string)
        client_socket.close()
    except KeyboardInterrupt:  #if we try to stop prog with using "Ctrl+C", we have this exception
        print 'Stopped'
        server_socket.close()  #Close the socket. All future operations on the socket object will fail
        exit()
