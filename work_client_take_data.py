import socket
import pickle

sock = socket.socket()
sock.connect(('26.41.8.62', 9090))

BUFFER_SIZE = 10240

all_data = bytearray()
while True:
    data = sock.recv(BUFFER_SIZE)
    print('a')
    if not data:
        break
    #print('Recv: {}: {}'.format(len(data), data))
    all_data += data
obj = pickle.loads(all_data)
print('Obj:', obj)

obj.pop(0)
data = pickle.dumps(obj)
print(len(obj))
#sock.sendall(data)

print('Close')
sock.close()
