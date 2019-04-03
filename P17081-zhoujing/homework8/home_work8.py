import socket
import wsgiref

sock = socket.socket()
sock.bind(('127.0.0.1',9999))
sock.listen(10)
try:
    while True:
        conn, raddr = sock.accept()
        conn.recv(1024)

        with open('img.jpg','rb') as f_obj:
            data = f_obj.read()
            length = len(data)
        with open('1.jpg', 'rb') as f_obj:
            data1 = f_obj.read()
            #length = len(data)+length

        HEAD = 'HTTP/1.1 200 OK\nContent-Type:image/png\n Content-length:'.encode()
        info = HEAD+str(length).encode()+b'\n\n'+data# +b'\n'+data1
        conn.send(info)

except Exception as e:
    print(e)