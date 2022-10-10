import socket 


c = socket.socket()
c.connect(('10.202.5.26',65432))


while True:
    c.send(bytes('0','utf-8'))
    
    out = c.recv(1024).decode()
    A = out.split(",") 
    print(A)
    
    