import socket
import pickle
import time


class SocketClient:
    def __init__(self, host, port, status_callback, retry_attempts=10):
        self.server_address = (host, port)
        self.retry_attempts = retry_attempts
        self.socket = None
        self.is_connected = False
        self.status_callback = status_callback
        self.is_running = True

    def connect(self, attempt=0):
        try:
            if attempt < self.retry_attempts:
                try:
                    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.socket.connect(self.server_address)
                    self.is_connected = True
                    self.status_callback('Connected')
                except ConnectionRefusedError:
                    self.status_callback('Connecting to {}:{}. Attempts: {}'.format(*self.server_address, attempt + 1))
                    self.connect(attempt + 1)
            else:
                self.status_callback('{}:{} - Failed'.format(*self.server_address))
        except OSError:
            print('Socket client stopped')

    def send(self, message, callback):
        packet = {'token': 'client_token', 'message': message}
        self.socket.sendall(pickle.dumps(packet))

        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected and self.is_running:
            data = self.socket.recv(200)
            amount_received += len(data)

            response = pickle.loads(data)
            current = int(round(time.time() * 1000))
            self.status_callback('Latency {}ms'.format(current - response[1]))
            callback(response[0])

    def disconnect(self):
        self.is_running = False
        self.socket.close()

    def __del__(self):
        self.disconnect()
