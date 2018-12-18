import threading


class VideoStreamer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print('streaming')
