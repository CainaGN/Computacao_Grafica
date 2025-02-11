import cv2
import numpy as np

def is_warm_color(hue):
    return (hue < 60) or (hue >= 300)

def categorize_image(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    warm_pixels = 0
    cold_pixels = 0
    

    for row in hsv_image:
        for pixel in row:
            hue = pixel[0]  
            if is_warm_color(hue):
                warm_pixels += 1
            else:
                cold_pixels += 1
    
    total_pixels = warm_pixels + cold_pixels
    print(f"Warm Pixels: {warm_pixels}, Cold Pixels: {cold_pixels}")
    
    if warm_pixels > cold_pixels:
        print("The image is predominantly warm.")
    else:
        print("The image is predominantly cold.")


categorize_image('input.jpg')

