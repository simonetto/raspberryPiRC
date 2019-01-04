import cv2
import numpy as np
import threading
import zmq

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
            self.current_frame = self.string_to_image(frame)
            cv2.imshow('Stream', self.current_frame)
            cv2.waitKey(1)

    @staticmethod
    def string_to_image(string):
        import numpy as np
        import cv2
        import base64
        img = base64.b64decode(string)
        npimg = np.fromstring(img, dtype=np.uint8)
        return cv2.imdecode(npimg, 1)

    def stop(self):
        self.keep_running = False
        self.footage_socket.close()
        print('Video socket stopped')

