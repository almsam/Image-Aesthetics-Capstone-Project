import os
import matplotlib.pyplot as plt
from PIL import Image

def load_vast_images(directory, num_images=None):
    image_files = [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    if num_images: image_files = image_files[:num_images]
    
    images = [Image.open(os.path.join(directory, file)) for file in image_files]
    return images, image_files

vast_images_dir = r'C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\data\VAST Images'

images, filenames = load_vast_images(vast_images_dir, num_images=6) #run meth

# pre view time
plt.figure(figsize=(8, 6))

# mpl stuff:
for i in range(0, len(images), 2):  # group into pairs
    row = i // 2 
    plt.subplot(len(images) // 2, 2, 2 * row + 1)  # Lef
    plt.imshow(images[i]); plt.title(f"Img {row + 1}L"); plt.axis('off')

    plt.subplot(len(images) // 2, 2, 2 * row + 2)  # Right
    plt.imshow(images[i + 1]); plt.title(f"Img {row + 1}R"); plt.axis('off')

plt.tight_layout(); plt.show()
