import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import save_img, img_to_array, load_img # type: ignore
import matplotlib.pyplot as plt
import sys
import os
import GenerateImagesPrototype # type: ignore
from scipy.ndimage import convolve
from scipy.ndimage import zoom

def smooth_image(image_array, threshold=4, swap=False): #re implemnted method from VASTSmoothing.py
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    image_array = img_to_array(image_array) / 255.0
    binary_img = (image_array < 0.99).astype(int)  # col "black" if < 0.99
    neighbor_counts = convolve(binary_img.squeeze(), kernel, mode='constant', cval=0)
    smoothed_image = binary_img.squeeze() * (neighbor_counts >= threshold)
    if(swap): smoothed_image = 1 - smoothed_image
    return np.expand_dims(smoothed_image, axis=-1)

def generateSmooth(seed, output_dir):
    image = GenerateImagesPrototype.generate_New_Image(seed)
    image_array = img_to_array(image) / 255.0
    
    os.makedirs(output_dir, exist_ok=True)
    
    temp_image_dir = os.path.join(output_dir, "temp")
    os.makedirs(temp_image_dir, exist_ok=True)
    
    temp_image_path = os.path.join(temp_image_dir, "temp_image.png")
    save_img(temp_image_path, image_array)
    reloaded_image = load_img(temp_image_path, color_mode="grayscale")
    # reloaded_image_array = img_to_array(reloaded_image) / 255.0
    
    smoothed_image = smooth_image(reloaded_image)
    
    smoothed_image_path = os.path.join(output_dir, f"generated_image_smooth_{seed}.png")
    save_img(smoothed_image_path, smoothed_image)
    print(f"Saved smoothed image: {smoothed_image_path}")
    return smoothed_image

def generateDoubleSmooth(seed, output_dir):
    image = GenerateImagesPrototype.generate_New_Image(seed)
    image_array = img_to_array(image) / 255.0

    os.makedirs(output_dir, exist_ok=True)
    
    temp_image_dir = os.path.join(output_dir, "temp")
    os.makedirs(temp_image_dir, exist_ok=True)

    temp_image_path = os.path.join(temp_image_dir, "temp_image.png")
    save_img(temp_image_path, image_array)
    
    # First round: load, then smooth, then make path, then save
    reloaded_image = load_img(temp_image_path, color_mode="grayscale")
    smoothed_once = smooth_image(reloaded_image, threshold=4)
    temp_image_path = os.path.join(output_dir, f"generated_image_smooth1_{seed}.png")
    save_img(temp_image_path, smoothed_once)

    # 2nd round: load, then smooth, then make path, then save
    reloaded_image = load_img(temp_image_path, color_mode="grayscale")
    smoothed_twice = smooth_image(reloaded_image, threshold=4, swap=True)
    smoothed_image_path = os.path.join(output_dir, f"generated_image_smooth2_{seed}.png")
    save_img(smoothed_image_path, smoothed_twice)
    
    print(f"Saved double-smoothed image: {smoothed_image_path}")
    return smoothed_twice


def generateQuality(seed, output_dir, n=4):
    smoothed_image_path = os.path.join(output_dir, f"generated_image_smooth2_{seed}.png")

    if not os.path.exists(smoothed_image_path): generateDoubleSmooth(seed, output_dir)

    # load our 2x smoothed image
    smoothed_image = load_img(smoothed_image_path, color_mode="grayscale"); smoothed_array = img_to_array(smoothed_image) / 255.0

    # first we upscale our image
    upscaled_image = zoom(smoothed_array, (n, n, 1), order=5)  # k nearest neighbor inspired upscale

    # apply curve smoothing by modifying white pixels based on neighbors
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    neighbor_counts = convolve(upscaled_image.squeeze(), kernel, mode='constant', cval=0)
    smoothed_upscaled = (neighbor_counts >= 4).astype(float)  # threshold for curves = 4

    # save time
    enhanced_image_path = os.path.join(output_dir, f"generated_image_quality_{seed}.png")
    save_img(enhanced_image_path, np.expand_dims(smoothed_upscaled, axis=-1))
    
    print(f"Saved quality-enhanced image: {enhanced_image_path}")
    return smoothed_upscaled

#print("Example Usage: pass a seed (int) & a directory to save the image (dir)")
#generateSmooth(100, "data/generated_images")


# generateSmooth(100, "data/temp")
# generateDoubleSmooth(43, "data/temp")

# generateQuality(100, "data/temp", n=72)

# new app images:

# script_dir = os.path.dirname(os.path.abspath(__file__))
# target_dir = os.path.join(script_dir, "..", "public", "data", "temp")

# for i in range(12):
#     generateQuality(((i+1)*100), target_dir, n=72)

# generateQuality(100, "data/temp", n=72)
# C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\public