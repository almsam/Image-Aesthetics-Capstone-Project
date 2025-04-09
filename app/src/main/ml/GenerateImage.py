import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import save_img, img_to_array, load_img # type: ignore
import matplotlib.pyplot as plt
import sys
import os
from ml import GenerateImagesPrototype # type: ignore
from scipy.ndimage import convolve

def smooth_image(image_array, threshold=4): #re implemnted method from VASTSmoothing.py
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    image_array = img_to_array(image_array) / 255.0
    binary_img = (image_array < 0.99).astype(int)  # col "black" if < 0.99
    neighbor_counts = convolve(binary_img.squeeze(), kernel, mode='constant', cval=0)
    smoothed_image = binary_img.squeeze() * (neighbor_counts >= threshold)
    return np.expand_dims(smoothed_image, axis=-1) 

def generateSmooth(seed, output_dir):
    image = GenerateImagesPrototype.generate_New_Image(seed)
    image_array = img_to_array(image) / 255.0
    
    os.makedirs(output_dir, exist_ok=True)
    
    temp_image_path = os.path.join(output_dir, f"temp/temp_image.png")
    save_img(temp_image_path, image_array)
    reloaded_image = load_img(temp_image_path, color_mode="grayscale")
    # reloaded_image_array = img_to_array(reloaded_image) / 255.0
    
    smoothed_image = smooth_image(reloaded_image)
    
    smoothed_image_path = os.path.join(output_dir, f"generated_image_smooth_{seed}.png")
    save_img(smoothed_image_path, smoothed_image)
    print(f"Saved smoothed image: {smoothed_image_path}")
    return smoothed_image

#print("Example Usage: pass a seed (int) & a directory to save the image (dir)")
#generateSmooth(100, "C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images")