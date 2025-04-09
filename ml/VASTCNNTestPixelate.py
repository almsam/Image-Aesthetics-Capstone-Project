import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import numpy as np

image_dir = r'C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\data\VAST Images'

def display_images(image_dir, num_images=5):
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]
    
    for i, filename in enumerate(image_files[:num_images]):
        # original img
        img_path = os.path.join(image_dir, filename)
        original_img = load_img(img_path)
        
        # resize the image
        resized_img = load_img(img_path, target_size=(32, 32))  # to a 32x32
        
        # Convert to arrays
        original_array = img_to_array(original_img) / 255.0  # Normalize
        resized_array = img_to_array(resized_img) / 255.0  # Normalize
        
        def process_pixels(array, grey_tol=0.1):
            processed_array = np.copy(array)
            for i in range(array.shape[0]):  # Iterate over height
                for j in range(array.shape[1]):  #          width
                    for k in range(array.shape[2]):  # over channels (RGB)
                        if array[i, j, k] < grey_tol:
                            processed_array[i, j, k] = 0.0  # black
                        elif array[i, j, k] > (1-grey_tol):
                            processed_array[i, j, k] = 1.0  # white
                        else:
                            processed_array[i, j, k] = 0.5  # gray
            return processed_array

        # apply pixel processing to resized array to make our b&W & grey array
        processed_array = process_pixels(resized_array, 0.25)
        
        # PLOT TIMEEE
        plt.figure(figsize=(12, 4))
        
        #oeiginal
        plt.subplot(1, 3, 1)
        plt.imshow(original_array)
        plt.title("Original Image")
        plt.axis('off')
        
        # resized
        plt.subplot(1, 3, 2)
        plt.imshow(resized_array)
        plt.title("Resized Image (32x32)")
        plt.axis('off')
        
        # B&W & grey
        plt.subplot(1, 3, 3)
        plt.imshow(processed_array)
        plt.title("Processed Image (BW/Grey)")
        plt.axis('off')
        plt.show()

display_images(image_dir, num_images=5)
