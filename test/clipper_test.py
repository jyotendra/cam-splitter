from utils.clip_img import image_util
import cv2
import os
import glob


img_input_directory = os.path.join(os.getcwd(), "images", "input")
glob_pattern = "*.jpeg"

def run_test():
    for file in glob.glob(os.path.join(img_input_directory, glob_pattern)):
        img = cv2.imread(file)
        img_util_obj = image_util(img)

        img_util_obj\
            .clipper()\
            .square_splitter()\
            .get_squared_images()\
            .display_all_img()