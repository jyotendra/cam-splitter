
from utils.rtsp_receiver import rtsp_receiver


def run_test():
    invoked_stream = rtsp_receiver().get_stream()
    while(1):
        invoked_stream.get_frames_on_console()
