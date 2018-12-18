import time
from socket_server import SocketServer
from video_streamer import VideoStreamer


def main():
    socket_thread = SocketServer()
    video_thread = VideoStreamer()
    try:
        socket_thread.start()
        video_thread.start()

        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        socket_thread.stop()
        video_thread.join()
        socket_thread.join()


if __name__ == '__main__':
    main()
