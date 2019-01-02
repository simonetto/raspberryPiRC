import cv2
import numpy as np
import zmq
from utils import string_to_image

PORT = '5555'


class VideoCapture:
    def __init__(self):
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.SUB)
        self.footage_socket.bind('tcp://*:' + PORT)
        self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

    def get_frame(self):
        frame = self.footage_socket.recv_string()
        parsed_frame = string_to_image(frame)
        return cv2.cvtColor(parsed_frame, cv2.COLOR_BGR2RGB)

    # Release the video source when the object is destroyed
    def __del__(self):
        print('close video socket')
