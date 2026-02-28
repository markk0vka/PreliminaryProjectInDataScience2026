import os
from os.path import join

from img_util import ImageDataLoader, saveImageFile
from inpaint_util import removeHair

#CHANGE THIS PATH TO YOUR OWN PATHS
input_dir = r""
output_dir = r""

os.makedirs(output_dir, exist_ok=True)

loader = ImageDataLoader(input_dir)

for i, (img_rgb, img_gray) in enumerate(loader):

    blackhat, thresh, img_out = removeHair(
        img_rgb,
        img_gray,
        kernel_size=5,
        threshold=10
    )

    save_path = join(output_dir, f"image_{i}.png")
    saveImageFile(img_out, save_path)

print("Hair removal completed.")