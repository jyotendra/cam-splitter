import threading
from utils.rtsp_receiver import rtsp_receiver
from utils.np_clipper import np_clipper_util
import time
import sys
import cv2

rtsp_endpoints = {
    "cam_1": "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"
}


def single_stream_task(kill_event, stream_key):
    cam_stream = rtsp_receiver(rtsp_endpoints[stream_key])
    while not kill_event.is_set():
        # define repetetive task here
        im_frame = cam_stream.get_frames()
        if (im_frame is not None):
            splitted_img = np_clipper_util(im_frame.raw_frame, im_frame.height, im_frame.width)\
                            .clip_image()\
                            .split_img()\
                            .get_squared_images()

        splitted_img.show_split_images()

    # print("exiting thread")


def thread_gen(killer_evnt, stream_metas):
    thread_list = []
    for meta in stream_metas:
        t = threading.Thread(
            target=meta["stream"], args=(killer_evnt, meta["task"]))
        thread_list.append(t)
    return thread_list


def run_streams():
    process_kill_evnt = threading.Event()
    stream_metas = []

    for key in rtsp_endpoints:
        stream_metas.append({
            "stream": single_stream_task(process_kill_evnt, key),
            "task": "thread_" + key
        })

    threads = thread_gen(process_kill_evnt, stream_metas)

    for thread in threads:
        thread.start()
    time.sleep(5)
    process_kill_evnt.set()
    for thread in threads:
        thread.join()
    print("main thread exiting")


if __name__ == '__main__':
    run_streams()
