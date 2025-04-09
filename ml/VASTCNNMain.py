import pickle
import numpy as np
import csv
import os
from tensorflow.keras import datasets, models, layers
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf
from collections import defaultdict

image_dir = r'C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\data\VAST Images'
csv_file = r'C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\data\vast_image_ratings.csv'


# import VAST images (as before)
image_ratings = defaultdict(list)


def quantize_colors(img_array, levels=3):
    bins = np.linspace(0, 1, levels); quantized = np.digitize(img_array, bins) - 1; return bins[quantized]

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header
    for row in reader:
        try:
            image_id = row[2]
            rating = int(row[3])  # Convert to integer
            image_ratings[image_id].append(rating)
        except ValueError:
            print(f"Skipping invalid row: {row[1]}")

average_ratings = {image_id: np.mean(ratings) for image_id, ratings in image_ratings.items()}
print(average_ratings)

rated_images = []; rated_labels = []

def normalize_image_id(img_id):
    numeric_part = img_id.split()[1][:-1]  # numeric part (e.g., '01')
    side = img_id.split()[1][-1]  # 'L' or 'R'
    base_number = int(numeric_part) * 2 - 1  # convert '01' to 1, '02' to 3, etc etc
    return base_number + (1 if side == 'R' else 0)

for filename in os.listdir(image_dir):
    if filename.endswith('.png'):
        img_id = os.path.splitext(filename)[0]  # get ID

        # Match idd
        # normalized_id = img_id.split()[1][:-1]  # extract the numeric part (e.g., '01' from 'img 01L') normalized_id = str(int(normalized_id))  # convert '01' to '1', '02' to '2', etc
        # normalized_id = normalize_image_id(img_id)
        normalized_id = f"{img_id}.png"
        print(f"Original ID: {img_id}, Normalized ID: {normalized_id}")
        if normalized_id in average_ratings:
            # load n preprocess img
            img_path = os.path.join(image_dir, filename)
            img = load_img(img_path, target_size=(32, 32))  # resize to match CNN input shape
            img_array = img_to_array(img) / 255.0  # normalize
            img_array = quantize_colors(img_array)
            rated_images.append(img_array)
            rated_labels.append(average_ratings[normalized_id])










# 90% for train case, 10% for test (every 10th img goes test set)
rated_images = np.array(rated_images); rated_labels = np.array(rated_labels) # fixes shape bug
train_images = np.delete(rated_images, np.arange(0, rated_images.shape[0], 10), axis=0)
train_labels = np.delete(rated_labels, np.arange(0, rated_labels.shape[0], 10), axis=0)
test_images = rated_images[::10]
test_labels = rated_labels[::10]

print("Rated Labels & imaegs lengths (expected: 53*2, 53*2 * 32*32*3):", rated_labels.size, rated_images.size)


print('start train:')

model = models.Sequential()

model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Dropout(0.25))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dropout(0.5))


model.add(layers.Dense(1))  # our output is a param of 1 int

# compile time
print('start compile:')
model.compile(optimizer='adam', 
              loss='mean_squared_error',
              metrics=['mae'])  # avg abs error


def evaluate_L_R_predictions(model, image_dir, average_ratings):

    pair_predictions = {}

    # predict for all rated images
    for filename in os.listdir(image_dir):
        if filename.endswith('.png'):
            img_id = os.path.splitext(filename)[0]  # e.g., 'img 01L'
            # normalized_id = img_id.split()[1][:-1]  # e.g., '01' from 'img 01L' # normalized_id = str(int(normalized_id)) # convert '01' to '1', '02' to '2', etc.
            normalized_id = f"{img_id}.png"
            
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


print('start fit:')

# training line
history = model.fit(train_images, train_labels, epochs=5, validation_split=0.2)
# evaluate
test_accuracy  = evaluate_L_R_predictions(model, image_dir, average_ratings)
print(f'Test accuracy: {test_accuracy}')

# # experiment:
# test_accuracies = []
# for i in range(10):
#     print(f"Training run {i + 1}...")
#     history = model.fit(train_images, train_labels, epochs=i, validation_split=0.2, verbose=2)
#     test_accuracy = evaluate_L_R_predictions(model, image_dir, average_ratings)
#     test_accuracies.append(test_accuracy)
#     print(f"Test accuracy for run {i + 1}: {test_accuracy:.2f}%")
# print(f"Test accuracies for all runs: {test_accuracies}")

################# 5 is best
# Test accuracies for all runs: [56.60377358490566, 54.71698113207547, 62.264150943396224, 58.490566037735846, 67.9245283018868,
#                                60.37735849056604, 58.490566037735846, 60.37735849056604, 56.60377358490566, 52.83018867924528]






# # save the model
# model.save('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/VAST_CNN_Main_Model.h5')
# print("model saved to disk.")


# # if you want to plot (old)
# import matplotlib.pyplot as plt
# plt.plot(history.history['mae'], label='train MAE'); plt.plot(history.history['val_mae'], label='test MAE')
# plt.xlabel('num epochs'); plt.ylabel('avg AE'); plt.legend(); plt.show()