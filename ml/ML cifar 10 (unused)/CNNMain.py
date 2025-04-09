import pickle
import numpy as np
import csv
import os
from tensorflow.keras import datasets, models, layers
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
    images = np.transpose(images, (0, 2, 3, 1))  # order on batch_size, height, width, channels
    return images

images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
images = reshape_images(images) / 255.0  # normalize



# read from CSV
csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv'
image_ratings = {}

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip 1st line
    for row in reader:
        image_id, rating = int(row[0]), int(row[1])
        image_ratings[image_id] = rating



# filter images based on available ratings
rated_images = []
rated_labels = []
for img_id, rating in image_ratings.items():
    rated_images.append(images[img_id])
    rated_labels.append(rating)

rated_images = np.array(rated_images)
rated_labels = np.array(rated_labels)



# 90% for train case, 10% for test (every 10th img goes test set)
train_images = np.delete(rated_images, np.arange(0, rated_images.shape[0], 10), axis=0)
train_labels = np.delete(rated_labels, np.arange(0, rated_labels.shape[0], 10), axis=0)
test_images = rated_images[::10]
test_labels = rated_labels[::10]


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
model.compile(optimizer='adam', 
              loss='mean_squared_error',
              metrics=['mae'])  # avg abs error



# training line
history = model.fit(train_images, train_labels, epochs=5, validation_split=0.2)
# evaluate
test_loss, test_mae = model.evaluate(test_images, test_labels, verbose=2)
print(f'Test MAE: {test_mae}')
# predict time
predicted_rating = model.predict(np.expand_dims(test_images[0], axis=0))
print(f"Predicted rating for the image: {predicted_rating[0][0]}")


# save the model
model.save('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Main_Model.h5')
print("model saved to disk.")


# # if you want to plot
# import matplotlib.pyplot as plt
# plt.plot(history.history['mae'], label='train MAE'); plt.plot(history.history['val_mae'], label='test MAE')
# plt.xlabel('num epochs'); plt.ylabel('avg AE'); plt.legend(); plt.show()