import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img # type: ignore
from scipy.ndimage import convolve

def process_and_display_images(data_dir, image_seeds, threshold=4):

    image_files = [f"generated_image_{seed}.png" for seed in image_seeds]
    kernel = np.array([[1, 1, 1],   [1, 0, 1],   [1, 1, 1]])

    def process_image(image_path):
        img = load_img(image_path, color_mode="grayscale")  # ro grayscale
        img_array = img_to_array(img) / 255.0  # map to [0, 1]
        binary_img = (img_array < 0.99).astype(int)  # Consider pixels "black" if < 0.99
        neighbor_counts = convolve(binary_img.squeeze(), kernel, mode='constant', cval=0)
        return binary_img.squeeze() * (neighbor_counts >= threshold)

    fig, axes = plt.subplots(1, len(image_files), figsize=(12, 4))
    for i, file_name in enumerate(image_files):
        image_path = os.path.join(data_dir, file_name)
        processed_image = process_image(image_path)
        
        axes[i].imshow(processed_image, cmap='gray'); axes[i].axis('off'); axes[i].set_title(f"Processed {file_name}")

    plt.tight_layout(); plt.show()

def process_image(image_path, threshold=4):
    kernel = np.array([[1, 1, 1],   [1, 0, 1],   [1, 1, 1]])
    
    img = load_img(image_path, color_mode="grayscale")  # ro grayscale
    img_array = img_to_array(img) / 255.0  # map to [0, 1]
    binary_img = (img_array < 0.99).astype(int)  # Consider pixels "black" if < 0.99
    neighbor_counts = convolve(binary_img.squeeze(), kernel, mode='constant', cval=0)
    return binary_img.squeeze() * (neighbor_counts >= threshold)


def main():
    data_dir = r"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images/"
    output_dir = r"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images/"
    os.makedirs(output_dir, exist_ok=True)

    seeds = [100, 300, 500]

    process_and_display_images(data_dir, seeds)

    # save three smoothed images per seed
    for seed in seeds:
        # for i in range(1, 4):  # ceating three smoothed variations for each seed
        image_path = os.path.join(data_dir, f"generated_image_{seed}.png")
        processed_image = process_image(image_path)
        processed_image = np.expand_dims(processed_image, axis=-1)  # add a channel dimension to make save_img happy
        smoothed_image_path = os.path.join(output_dir, f"smoothed_image_{seed}.png")
        save_img(smoothed_image_path, processed_image)
        print(f"Saved: {smoothed_image_path}")

# main()