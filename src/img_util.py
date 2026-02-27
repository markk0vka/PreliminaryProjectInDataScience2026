import os
import cv2


def readImageFile(file_path):
    img_bgr = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, img_bgr)


class ImageDataLoader:
    def __init__(self, directory):
        self.file_list = sorted([
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ])

    def __iter__(self):
        for file_path in self.file_list:
            yield readImageFile(file_path)