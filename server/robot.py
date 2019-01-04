import time
from control_server import ControlServer
from video_server import VideoServer


def main():
    control_thread = ControlServer()
    video_thread = VideoServer()
    try:
        control_thread.start()
        video_thread.start()

        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        control_thread.stop()
        video_thread.join()
        control_thread.join()


if __name__ == '__main__':
    main()
