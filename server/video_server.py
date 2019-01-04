import cv2
import zmq
import threading
from camera import Camera
from constants import PORT, SERVER_ADDRESS
from utils import image_to_string


class VideoServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.PUB)
        self.footage_socket.connect('tcp://' + SERVER_ADDRESS + ':' + PORT)
        self.keep_running = True
        self.camera = Camera()

    def run(self):
        print('Streaming Started...')
        self.camera.start_capture()
        self.keep_running = True

        while self.footage_socket and self.keep_running:
            try:
                frame = self.camera.current_frame.read()
                image_as_string = image_to_string(frame)
                self.footage_socket.send(image_as_string)
            except zmq.error.ZMQError:
                self.stop()

        cv2.destroyAllWindows()

    def stop(self):
        self.keep_running = False
        self.footage_socket.close()
        print('Video socket stopped')
