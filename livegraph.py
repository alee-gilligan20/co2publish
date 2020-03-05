import matplotlib.pyplot as plt
import time
import random
import zmq

context = zmq.Context()

#  Socket to talk to server
print('Connecting to CO2 server')
socket = context.socket(zmq.REQ)
socket.connect('tcp://192.168.21.38:5555')
#CHANGE THE IP TO THE IP OF THE PI AND MAKE SURE THAT THE PORT NUMBER MATCHES
plt.axis([0, 100, 0, 1000])

for i in range(100):
    print('Sending request %s ' % i)
    socket.send(b'Hello')

    #  Get the reply.
    message = socket.recv()
    print('Received reply %s [ %s ] %s' % (i, message,""))
    plt.scatter(i, message)
    plt.pause(0.05)

plt.show()
