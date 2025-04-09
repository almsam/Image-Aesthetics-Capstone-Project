import csv
import pickle
import numpy as np
from tensorflow.keras.models import load_model # type: ignore


# import CIFAR-10 images (as before)
def load_cifar_batch(filename):
    with open(filename, 'rb') as f:
        batch = pickle.load(f, encoding='latin1'); images = batch['data']; labels = batch['labels']
    return images, labels
def reshape_images(images):
    images = images.reshape(-1, 3, 32, 32); images = np.transpose(images, (0, 2, 3, 1)); return images # order on batch_size, height, width, channels

images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1'); images = reshape_images(images) / 255.0  # normalize

# read from CSV
csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv'; image_ratings = {}
with open(csv_file, 'r') as f:
    reader = csv.reader(f); next(reader)  # skip 1st line
    for row in reader:
        image_id, rating = int(row[0]), int(row[1]); image_ratings[image_id] = rating

# filter images based on available ratings
rated_images = []; rated_labels = []
for img_id, rating in image_ratings.items():
    rated_images.append(images[img_id]); rated_labels.append(rating)
test_images = np.array(rated_images); test_labels = np.array(rated_labels)




# load the saved model
model = load_model('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Main_Model.h5')
print("model loaded from disk")

# evaluate the loaded model
test_loss, test_mae = model.evaluate(test_images, test_labels, verbose=2)
print(f'test MAE (loaded model): {test_mae}')

# predict with the loaded model
predicted_rating = model.predict(np.expand_dims(test_images[0], axis=0))
print(f"predicted rating for the image (loaded model): {predicted_rating[0][0]}")
