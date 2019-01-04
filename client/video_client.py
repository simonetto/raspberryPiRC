import cv2
import numpy as np
import threading
import zmq
from utils import string_to_image

PORT = '5555'


class VideoClient(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.SUB)
        self.footage_socket.bind('tcp://*:' + PORT)
        self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        self.current_frame = None
        self.keep_running = True

    def run(self):
        self.keep_running = True
        while self.footage_socket and self.keep_running:
            frame = self.footage_socket.recv_string()
            self.current_frame = string_to_image(frame)
            cv2.imshow('Stream', self.current_frame)
            cv2.waitKey(1)

    def stop(self):
        self.keep_running = False
        self.footage_socket.close()
        print('Video socket stopped')

