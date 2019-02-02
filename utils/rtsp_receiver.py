import sys
import cv2

from utils.np_clipper import np_clipper_util

rtsp_endpoints = {
    "cam_1": "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov"
}


class rtsp_receiver:
    def __init__(self, endpoint=rtsp_endpoints["cam_1"], fps=25):
        self.endpoint = endpoint
        self.vcap = cv2.VideoCapture(self.endpoint)
        if(not self.vcap.isOpened()):
            print("Error opening", rtsp_endpoints["cam_1"])
            raise Exception("Unable to open rtsp: ", self.endpoint)
        self.cam_fps = self.vcap.get(cv2.CAP_PROP_FPS)
        self.desired_fps = fps
        self.vid_height = int(round(self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.vid_width = int(round(self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)))


    def get_frames(self):
        frame_id = int(round(self.vcap.get(cv2.CAP_PROP_POS_FRAMES)))
        ret, frame = self.vcap.read()
        # print(frame_id)
        if (frame_id % self.desired_fps == 0):
            return img_frame(frame, self.vid_height, self.vid_width)


class img_frame:
    def __init__(self, frame, height, width, channel=3):
        self.raw_frame = frame
        self.height = height
        self.width = width
        self.channel = channel




if __name__ == '__main__':
    receiver = rtsp_receiver()
    while(True):
        im_frame = receiver.get_frames()
        if(im_frame is not None):
            cv2.imshow("Frame", im_frame)
            # sys.stdout.buffer.write(im_frame)
        if(cv2.waitKey(25) & 0xFF == ord('q')):
            cv2.destroyAllWindows()
            break