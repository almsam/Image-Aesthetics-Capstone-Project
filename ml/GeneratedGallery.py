import os
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore
from GenerateImage import *

# seaborn theme for nicer plots goes here
sns.set_theme(style="darkgrid")

def display_image_pipeline(seeds, output_dir, save_path):
    
    n = len(seeds)
    fig, axes = plt.subplots(nrows=n, ncols=4, figsize=(16, 3 * n))
    if n == 1: axes = [axes]
    
    for row_idx, seed in enumerate(seeds):
        print(f"Rendering seed {seed}...")
        stages = [
            ("Raw Image", os.path.join(output_dir, "temp", "temp_image.png")),
            ("Smoothed Once", os.path.join(output_dir, f"generated_image_smooth1_{seed}.png")),
            ("Smoothed Twice", os.path.join(output_dir, f"generated_image_smooth2_{seed}.png")),
            ("HD Quality", os.path.join(output_dir, f"generated_image_quality_{seed}.png"))
        ]
        # fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(16, 4))

        # axes = axes.flatten()
        for col_idx, (title, path) in enumerate(stages):
            ax = axes[row_idx][col_idx] if n > 1 else axes[col_idx]
            if not os.path.exists(path):
                print(f"Warning: Missing file {path}, add it to missing seeds")
                ax.axis('off')
                continue
            image = load_img(path, color_mode="grayscale")
            ax.imshow(img_to_array(image).squeeze(), cmap='gray')
            ax.set_title(title, fontsize=10)
            ax.axis('off')

    plt.tight_layout(); plt.savefig(save_path, dpi=600); plt.show()

if __name__ == "__main__":
    
    # fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(16, 4))
    # n=1; fig, axes = plt.subplots(nrows=n, ncols=4, figsize=(16, 3 * n))
    
    # seed = [800, 1000, 600, x] #    seed = [1100, 800, 1000, 600] # 1900
    seed = [800, 1000, 600, 1900]
    missingSeeds = [] # [800, 1000, 600, 1900]
    
    output_dir = os.path.join(os.path.dirname(__file__), "public", "data", "temp")
    for seeds in missingSeeds: generateQuality(seeds, output_dir, n=72)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "public", "data", "temp")
    
    save_path = os.path.join(script_dir, "gallery_4seeds.png")

    display_image_pipeline(seed, output_dir, save_path=save_path)
    
    
