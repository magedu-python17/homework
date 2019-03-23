# import hashlib
#
#
# md5_obj = hashlib.md5()
# while has_sent < file_size:
#     data = file_obj.read(1024)
#     self.sock.sendall(data)
#     has_sent += len(data)
#     md5_obj.update(data)
#     self.progress_percent(has_sent, file_size)
#
# else:
#     print('post sucess!')
#     md5_val = md5_obj.hexdigest()
#     self.sock.recv(1024)
#     self.sock.send(md5_val.encode('utf-8'))
#     response = self.sock.recv(1024).decode('utf-8')
#     print('response', response)

