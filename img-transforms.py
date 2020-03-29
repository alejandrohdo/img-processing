"""Tratamuennto de imágenes de tipo CATCHA"""

import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFilter

def prepare_image(img):
    """Transform image to greyscale and blur it"""
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    if 'L' != img.mode:
        img = img.convert('L')
    return img

def remove_noise(img, pass_factor):
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            value = remove_noise_by_pixel(img, column, line, pass_factor)
            img.putpixel((column, line), value)
    return img

def remove_noise_by_pixel(img, column, line, pass_factor):
    if img.getpixel((column, line)) < pass_factor:
        return (0)
    return (255)

# CATCHA tomado de
# https://prodapp2.seace.gob.pe/seacebus-uiwd-pub/buscadorPublico/buscadorPublico.xhtml?fbclid=IwAR1T1aXjVd9LD0IPTz8rhiqOREmoyF1dZOaJzbjJ2RQ5hPYDp7oB4rM4jn8
input_image = 'c2.jpeg'
img = Image.open(input_image)

# plt.imshow(img, cmap='gray')
# plt.show()

img = prepare_image(img)
# plt.imshow(img, cmap='gray')
# plt.show()

#Imagen proesado    
pass_factor = 20
processed_img = remove_noise(img, pass_factor)
processed_img.save('im1.jpeg')
# plt.imshow(processed_img, cmap='gray')
# plt.show()