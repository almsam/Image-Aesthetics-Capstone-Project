import csv
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os
from collections import defaultdict

model_path = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/VAST_CNN_Main_Model.h5'
image_dir = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/VAST Images'
csv_file = r'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/vast_image_ratings.csv'


# read from CSV
image_ratings = defaultdict(list)
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  #no headr
    for row in reader:
        try:
            image_id = row[0]
            rating = int(row[2])  # to int
            image_ratings[image_id].append(rating)
        except ValueError:
            print(f"Skipping invalid row: {row}")

average_ratings = {image_id: np.mean(ratings) for image_id, ratings in image_ratings.items()}
# print(f"Loaded ratings: {average_ratings}")

# import CIFAR-10 images (as before)
rated_images = []
rated_labels = []
for filename in os.listdir(image_dir):
    if filename.endswith('.png'):
        img_id = os.path.splitext(filename)[0]
        normalized_id = img_id.split()[1][:-1]  # normalyze
        normalized_id = str(int(normalized_id))  # no leading zeroes

        if normalized_id in average_ratings:
            img_path = os.path.join(image_dir, filename)
            img = load_img(img_path, target_size=(32, 32))  # resize
            img_array = img_to_array(img) / 255.0  # normalyze
            rated_images.append(img_array); rated_labels.append(average_ratings[normalized_id])

test_images = np.array(rated_images); test_labels = np.array(rated_labels)







# load the saved model
model = load_model(model_path)
print("model loaded from disk")

# evaluate the loaded model
test_loss, test_mae = model.evaluate(test_images, test_labels, verbose=2)
print(f'test MAE (loaded model): {test_mae}')

# predict with the loaded model
sample_img = test_images[0]  # get first test image
predicted_rating = model.predict(np.expand_dims(sample_img, axis=0))
print(f"predicted rating for the image (loaded model): {predicted_rating[0][0]}")











def evaluate_L_R_predictions(model, image_dir, average_ratings):

    pair_predictions = {}

    # predict for all rated images
    for filename in os.listdir(image_dir):
        if filename.endswith('.png'):
            img_id = os.path.splitext(filename)[0]  # e.g., 'img 01L'
            normalized_id = img_id.split()[1][:-1]  # e.g., '01' from 'img 01L'
            normalized_id = str(int(normalized_id)) # convert '01' to '1', '02' to '2', etc.
            
            if normalized_id in average_ratings:
                img_path = os.path.join(image_dir, filename)
                img = load_img(img_path, target_size=(32, 32))
                img_array = img_to_array(img) / 255.0  # normalize
                
                predicted_rating = model.predict(np.expand_dims(img_array, axis=0))[0][0]
                pair_predictions[img_id] = predicted_rating

    # compare predictions for L R
    correct = 0; total = 0

    for img_id, pred_rating in pair_predictions.items():
        base_id = img_id[:-1]  # e.g., 'img 01'
        side = img_id[-1]  # e.g., 'L' or 'R'
        # Find the paired side ('L' -> 'R' or 'R' -> 'L')
        paired_id = base_id + ('R' if side == 'L' else 'L')
        
        if paired_id in pair_predictions:
            total += 1
            # Compare predictions
            if (side == 'L' and pred_rating > pair_predictions[paired_id]) or (side == 'R' and pred_rating < pair_predictions[paired_id]):
                correct += 1

    # accuracy
    return (correct / total if total > 0 else 0) * 100

# # check predictions for all test images
# predictions = model.predict(test_images)
# for i, pred in enumerate(predictions[:10]):  # 1st 10 predictions
#     print(f"Image {i}: True Rating = {test_labels[i]:.2f}, Predicted Rating = {pred[0]:.2f}")


accuracy = evaluate_L_R_predictions(model, image_dir, average_ratings)
print(f"L/R Prediction Accuracy: {accuracy:.2f}%")