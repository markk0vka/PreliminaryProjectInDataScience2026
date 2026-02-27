import os
from os.path import join

from img_util import ImageDataLoader, saveImageFile
from inpaint_util import removeHair


# Ruta ABSOLUTA (más seguro ahora mismo)
input_dir = r"C:\Users\ruben\Desktop\Data Science\2nd YEAR\2nd SEMESTER\Projects in Data Science\data\lesion"
output_dir = r"C:\Users\ruben\Desktop\Data Science\2nd YEAR\2nd SEMESTER\Projects in Data Science\Preliminary Assignment\PreliminaryProjectInDataScience2026\result\hair_removed"

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