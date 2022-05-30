""" Process and improve image quality of a number of images quickly """
import os
import sys
from time import time
from PIL import Image, ImageFilter


try:
    image_folder = sys.argv[1]
    result_folder = sys.argv[2]

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    t_1 = time()
    for filename in os.listdir(image_folder):
        name_of_file = os.path.splitext(filename)[0]
        image = Image.open(f'{image_folder}/{filename}')
        image.thumbnail((700, 700))
        img = image.filter(ImageFilter.DETAIL())
        img.filter(ImageFilter.EDGE_ENHANCE())
        img.filter(ImageFilter.EDGE_ENHANCE_MORE())
        img.filter(ImageFilter.SMOOTH())
        img.filter(ImageFilter.SMOOTH_MORE())
        img.filter(ImageFilter.EMBOSS())
        img.filter(ImageFilter.FIND_EDGES())
        img.save(f'{result_folder}/{name_of_file}.png', 'png')
    t_2 = time()
    print(f'Finished in {t_2-t_1}ms')
except FileNotFoundError:
    print("File not Found")
