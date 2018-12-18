import threading
import socket
import pickle
from robot_controller import RobotController

PORT = 10000
IP = '127.0.0.1'


class SocketServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (IP, PORT)
        print('starting up on {} port {}'.format(*self.server_address))
        self.socket.bind(self.server_address)
        self.socket.listen(1)
        self.is_listening = True
        self.robot_controller = RobotController()

    def run(self):
        try:
            while self.is_listening:
                print('waiting for a connection')
                connection, client_address = self.socket.accept()
                try:
                    print('client connected:', client_address)
                    while True:
                        data = connection.recv(200)
                        packet = pickle.loads(data)
                        message = packet['message']
                        token = packet['token']

                        if token == 'client_token':
                            self.robot_controller.move(message[0])
                            if message:
                                connection.sendall(message)
                            else:
                                break
                        else:
                            connection.close()
                finally:
                    connection.close()
        except OSError:
            print('Socket server stopped')

    def stop(self):
        self.is_listening = False
        self.socket.close()

    def __del__(self):
        self.stop()
