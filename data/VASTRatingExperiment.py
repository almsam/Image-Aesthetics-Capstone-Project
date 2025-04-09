import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# dir
model_path = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/VAST_CNN_Main_Model.h5'
test_image_dir = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/Test images'


categories = {
    "Contrast": ["contrast_high_1.png", "contrast_high_2.png", "contrast_high_3.png",
                 "contrast_low_1.png", "contrast_low_2.png", "contrast_low_3.png"],
    "Shape": ["shape_high_1.png", "shape_high_2.png", "shape_high_3.png",
              "shape_low_1.png", "shape_low_2.png", "shape_low_3.png"],
    "Symmetry": ["symetry_high_1.png", "symetry_high_2.png", "symetry_high_3.png",
                 "symetry_low_1.png", "symetry_low_2.png", "symetry_low_3.png"]
}

model = load_model(model_path); print("ML model loaded successfully.")

predictions = {}

# process n predict time
# Process and predict
for category, images in categories.items():
    for image_name in images:
        img_path = os.path.join(test_image_dir, image_name)
        if os.path.exists(img_path):
            img = load_img(img_path, target_size=(32, 32))  # size to 32^2
            img_array = img_to_array(img) / 255.0  # normalyze
            img_array = np.expand_dims(img_array, axis=0)  # normalize

            predicted_rating = model.predict(img_array)[0][0]; predictions[image_name] = predicted_rating
            print(f"Predicted rating for {image_name}: {predicted_rating:.2f}")
        else:
            print(f"Img not found: {image_name}")


# image_names = list(predictions.keys()); rating_values = list(predictions.values())

# # // sns bar plot bloat goes here
# plt.figure(figsize=(12, 6))
# sns.barplot(x=image_names, y=rating_values, palette="viridis")
# plt.xticks(rotation=45, ha="right")
# plt.xlabel("Image Name")
# plt.ylabel("Predicted Rating")
# plt.title("CNN Predicted Ratings for Test Images")
# plt.show()





# data analysis now:

plot_data = []
for category, images in categories.items():
    for image_name in images:
        if image_name in predictions:
            level = "High" if "high" in image_name else "Low"
            plot_data.append((category, level, predictions[image_name]))




df = pd.DataFrame(plot_data, columns=["Category", "Level", "Rating"])

# plot time again
fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True); categories_list = ["Contrast", "Shape", "Symmetry"]
color_palettes = {"Contrast": ["#d73027", "#f48d63"],       "Shape": ["#2555b4", "#91bfdb"],        "Symmetry": ["#36f255", "#abdda4"]}


for i, category in enumerate(categories_list):
    sub_df = df[df["Category"] == category]
    sns.barplot(x="Level", y="Rating", data=sub_df, ax=axes[i], palette=color_palettes[category])
    axes[i].set_title(f"{category} - High vs Low")
    axes[i].set_xlabel("Level")
    axes[i].set_ylabel("Predicted Rating")

plt.tight_layout()
plt.show()
