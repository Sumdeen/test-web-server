import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5555
s.bind((host, port))
s.listen(5)
c, addr = s.accept()
while True: c,


print('Got connection from', addr)
c.send(b'Thank you for connecting')
c.close()


filename = input(str("Please enter a filename for the incoming file : "))
file = open (filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")


