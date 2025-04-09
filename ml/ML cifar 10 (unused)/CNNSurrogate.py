import pickle
import numpy as np
import csv
import os
from tensorflow.keras import models, layers
import tensorflow as tf


# import CIFAR-10 images (as before)
def load_cifar_batch(filename):
    with open(filename, 'rb') as f:
        batch = pickle.load(f, encoding='latin1')
        images = batch['data']
        labels = batch['labels']
    return images, labels

def reshape_images(images):
    images = images.reshape(-1, 3, 32, 32)
    images = np.transpose(images, (0, 2, 3, 1))
    return images

images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
images = reshape_images(images) / 255.0  # normalize

# read from CSV
csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings_detailed.csv'
ratings_data = {'color': [], 'contrast': [], 'shape': [], 'overall': []}

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        image_id = int(row[0])
        ratings_data['color']   .append((image_id, int(row[1])))
        ratings_data['contrast'].append((image_id, int(row[2])))
        ratings_data['shape']   .append((image_id, int(row[3])))
        ratings_data['overall'] .append((image_id, int(row[4])))

# meth to train and save models for each
def train_and_save_model(images, ratings, model_name):
    # filter based on available ratings
    rated_images = []; rated_labels = []
    for img_id, rating in ratings:
        rated_images.append(images[img_id]); rated_labels.append(rating)

    rated_images = np.array(rated_images); rated_labels = np.array(rated_labels)

    # train test split remains
    train_images = np.delete(rated_images, np.arange(0, rated_images.shape[0], 10), axis=0)
    train_labels = np.delete(rated_labels, np.arange(0, rated_labels.shape[0], 10), axis=0)
    test_images = rated_images[::10]; test_labels = rated_labels[::10]

    # pre train time
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

    model.add(layers.Dense(1))  # final node is single float value

    # compile
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    # train the model
    history = model.fit(train_images, train_labels, epochs=5, validation_split=0.2, verbose=2)

    # eval time
    test_loss, test_mae = model.evaluate(test_images, test_labels, verbose=2)
    print(f"{model_name} - Test MAE: {test_mae}")

    # save
    model.save(f'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/{model_name}.h5')
    print(f"{model_name} model saved to disk.")

    return history

    #method ends here

for category in ['color', 'contrast', 'shape', 'overall']:
    print(f"Training model for {category} rating...")
    train_and_save_model(images, ratings_data[category], f"CNN_{category.capitalize()}_Model") #most of the program is the method in here
