import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing.image import save_img # type: ignore
import matplotlib.pyplot as plt
import sys
import os
ml_path = r"C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\ml"; sys.path.append(ml_path)
import GenerateImagesPrototype # type: ignore

save = True

seeds = [100, 300, 500]; generated_images = {}

for seed in seeds:
    print(f"Generating image for seed {seed}...")
    generated_images[seed] = GenerateImagesPrototype.generate_New_Image(seed)

# save images
output_dir = r"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/generated_images/"
os.makedirs(output_dir, exist_ok=True)

# display generated images
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for i, seed in enumerate(seeds):
    # save:
    if(save):
        save_path = os.path.join(output_dir, f"generated_image_{seed}.png")
        save_img(save_path, generated_images[seed]);  print(f"Saved: {save_path}")

    # display
    axes[i].imshow(generated_images[seed]); axes[i].axis('off'); axes[i].set_title(f"Seed {seed}")

plt.tight_layout(); plt.show()