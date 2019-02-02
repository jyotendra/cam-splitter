import cv2
import os
import math

# clipping_pts = {"top_left": (0, 100), "bottom_right": None}
clipping_pts = {"top_left": (0, 10), "bottom_right": None}


class np_clipper_util:

    def __init__(self, img, img_height, img_width):
        self.img = img
        self.img_height = img_height
        self.img_width = img_width
        self.img_splits = {}

    def clip_image(self):
        crop_img = self.img[clipping_pts["top_left"][1]:self.img_height,
                   clipping_pts["top_left"][0]:self.img_width]
        self.img = crop_img
        self.img_height = self.img_height - clipping_pts["top_left"][1]
        self.img_width = self.img_height - clipping_pts["top_left"][0]
        return self

    def split_img(self):
        half_height = math.floor(self.img_height / 2)
        half_width = math.floor(self.img_width / 2)
        # top frames
        top_left = self.img[0:half_height,
                   0:half_width]

        top_right = self.img[0:half_height,
                    half_width: self.img_width]

        # bottom frames
        bottom_left = self.img[half_height:self.img_height,
                      0: half_width]

        bottom_right = self.img[half_height:self.img_height,
                       half_width: self.img_width]

        self.img_splits.update({"top_left": top_left, "top_right": top_right,
                                "bottom_left": bottom_left, "bottom_right": bottom_right})

        return self

    def get_squared_images(self):
        if self.img_splits.__contains__("top_left"):
            return squared_image(self.img_splits["top_left"],
                                 self.img_splits["top_right"],
                                 self.img_splits["bottom_left"],
                                 self.img_splits["bottom_right"])
        else:
            raise ("Please call square splitter before asking forimages")


class squared_image:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left_img = top_left
        self.top_right_img = top_right
        self.bottom_left_img = bottom_left
        self.bottom_right_img = bottom_right

    def show_split_images(self):
        cv2.imshow("Top Left", self.top_left_img)
        cv2.imshow("Top Right", self.top_right_img)
        cv2.imshow("Bottom Left", self.bottom_left_img)
        cv2.imshow("Bottom Right", self.bottom_right_img)
        if (cv2.waitKey(25) & 0xFF == ord('q')):
            cv2.destroyAllWindows()
            return 0

