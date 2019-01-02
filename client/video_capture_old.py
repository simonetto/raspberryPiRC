import cv2


class VideoCapture_old:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)

        #https://raspberrypi.stackexchange.com/questions/23182/how-to-stream-video-from-raspberry-pi-camera-and-watch-it-live
        #https://raspberrypi.stackexchange.com/questions/79513/rpi-camera-stream-to-opencv-in-python
        #pipeStr = "gst-launch-1.0 tcpclientsrc host=192.168.0.6 port=5600  ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink  sync=false"
        #self.vid = cv2.VideoCapture(pipeStr)


        if not self.vid.isOpened():
            raise ValueError('Unable to open video source', video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None
        return None

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
