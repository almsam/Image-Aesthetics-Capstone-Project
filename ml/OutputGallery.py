import os
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore
from GenerateImage import *

# seaborn theme for nicer plots goes here
sns.set_theme(style="darkgrid")

def display_image_pipeline(seeds, output_dir, save_path):
    
    # n = len(seeds); n=n/5
    # fig, axes = plt.subplots(nrows=int(n), ncols=5, figsize=(16, 3 * int(n)))
    # if n == 1: axes = [axes]
    rows = 4; cols = 5
    fig, axes = plt.subplots(rows, cols, figsize=(20, 12))
    
    for idx, seed in enumerate(seeds):
        print(f"Rendering seed {seed}...")
        path = os.path.join(output_dir, f"generated_image_quality_{seed}.png")
        ax = axes[idx // cols][idx % cols]
        
        # fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(16, 4))

        if not os.path.exists(path):
            print(f"Missing file {path}")
            ax.axis('off')
            continue
        
        image = load_img(path, color_mode="grayscale")
        ax.imshow(img_to_array(image).squeeze(), cmap='gray')
        ax.set_title(f"Seed {seed}", fontsize=10)
        ax.axis('off')

    plt.tight_layout(); plt.savefig(save_path, dpi=600); plt.show()

if __name__ == "__main__":
    
    missingSeeds = [] # [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
    # [800, 1000, 600, 1900]
    
    
    
    seeds = [101, 102, 103, 104, 800, 
            105, 106, 107, 108, 1000, 
            109, 110, 111, 112, 600, 
            113, 114, 115, 116, 1900]
    
    output_dir = os.path.join(os.path.dirname(__file__), "public", "data", "temp")
    for seeds in missingSeeds: generateQuality(seeds, output_dir, n=72)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "public", "data", "temp")
    
    save_path = os.path.join(script_dir, "hd_gallery_20seeds.png")

    display_image_pipeline(seeds, output_dir, save_path=save_path)