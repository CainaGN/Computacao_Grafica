import cv2
import numpy as np

image = cv2.imread('input.jpg')

pixels = image.reshape((-1, 3))

unique_colors = set()

for pixel in pixels:
 
    unique_colors.add(tuple(pixel))

num_unique_colors = len(unique_colors)
print(f"Number of unique colors: {num_unique_colors}")

