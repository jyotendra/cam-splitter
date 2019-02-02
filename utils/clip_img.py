import cv2
import os
import math

clipping_pts = {"top_left": (0, 100), "bottom_right": None}


class image_util:

    def __init__(self, img):
        self.img = img
        self.img_height, self.img_width, self.channels = img.shape
        self.img_splits = {}

    def clipper(self):
        crop_img = self.img[clipping_pts["top_left"][1]:self.img_height,
                            clipping_pts["top_left"][0]:self.img_width]
        cv2.imshow("cropped", crop_img)
        cv2.waitKey(0)

        self.img = crop_img

        return self

    def square_splitter(self):
        # top frames
        top_left = self.img[0:math.floor(self.img_height/2),
                            0:math.floor(self.img_width / 2)]

        top_right = self.img[0:math.floor(self.img_height/2),
                             math.floor(self.img_width / 2): self.img_width]

        # bottom frames
        bottom_left = self.img[math.floor(self.img_height/2):self.img_height,
                               0: math.floor(self.img_width / 2)]

        bottom_right = self.img[math.floor(self.img_height/2):self.img_height,
                                math.floor(self.img_width / 2): self.img_width]

        self.img_splits.update({"top_left": top_left, "top_right": top_right,
                                "bottom_left": bottom_left, "bottom_right": bottom_right})

        return self

    def get_squared_images(self):
        if self.img_splits.__contains__("top_left"):
            pass
        else:
            print("Please call square splitter before asking forimages")
        return squared_image(self.img_splits["top_left"], 
                self.img_splits["top_right"], 
                self.img_splits["bottom_left"], 
                self.img_splits["bottom_right"])


class squared_image:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left_img = top_left
        self.top_right_img = top_right
        self.bottom_left_img = bottom_left
        self.bottom_right_img = bottom_right

    def display_all_img(self):
        cv2.imshow("Top Left", self.top_left_img)
        cv2.waitKey(0)

        cv2.imshow("Top Right", self.top_right_img)
        cv2.waitKey(0)

        cv2.imshow("Bottom Left", self.bottom_left_img)
        cv2.waitKey(0)

        cv2.imshow("Bottom Right", self.bottom_right_img)
        cv2.waitKey(0)


# if __name__ == '__main__':
#     functionA()
#     functionB()
# print("after __name__ guard")
