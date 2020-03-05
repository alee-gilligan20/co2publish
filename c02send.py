import time, zmq, random
import RoboPiLib as RPL

RPL.RoboPiInit("/dev/ttyAMA0",115200)
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    sdata = RPL.analogRead(4)
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(.5)

    #  Send reply back to client
    socket.send(b"%d"%sdata)

