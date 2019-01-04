import time
from control_server import ControlServer
from video_server import VideoServer


def main():
    video_thread = VideoServer()
    control_thread = ControlServer(video_thread)

    try:
        video_thread.start()
        control_thread.start()
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        control_thread.stop()
        video_thread.stop()
        video_thread.join()
        control_thread.join()


if __name__ == '__main__':
    main()
