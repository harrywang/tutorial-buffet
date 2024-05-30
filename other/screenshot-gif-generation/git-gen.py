# # Generate Screenshots and Gifs via Python
# 
# Code is revised based on:
# - https://blog.csdn.net/qq_38161040/article/details/91040640
# - https://medium.com/swlh/python-animated-images-6a85b9b68f86
# pip install the following three packages: imageio, pillow, pygifsicle

# %%
from PIL import ImageGrab
from PIL import Image
import time


# %%
# take a screenshot every 0.1 second, 10 jpg saved
total_images = 10 # total screenshots
interval = 0.1 # the interval to take a screenshot
resize_ratio = 0.3 # the resize ratio to keep the screenshot smaller

for i in range(total_images):
    time.sleep(interval)
    img = ImageGrab.grab()
    width = img.size[0]
    height = img.size[1]

    img = img.resize(
        (int(width*resize_ratio), int(height*resize_ratio)), 
        Image.ANTIALIAS)
    
    img = img.convert('RGB') # if save to jpg
    img.save(f'./screenshots/screenshot{str(i+1)}.jpg')


# %%
import imageio

gif_images = []
for i in range(total_images):
    gif_images.append(imageio.imread(f'./screenshots/screenshot{str(i+1)}.jpg'))

imageio.mimsave("./screenshots/screenshot.gif", gif_images, fps=5)


# %%
from pygifsicle import optimize

gif_orginal = './screenshots/screenshot.gif'

# create a new onegit 
optimize(gif_orginal, './screenshots/screenshot_optimized.gif')

# overwrite the original one if needed
# optimize(gif_orginal)


