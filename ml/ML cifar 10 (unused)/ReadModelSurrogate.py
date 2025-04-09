import csv
import pickle
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore


# import CIFAR-10 images (as before)
def load_cifar_batch(filename):
    with open(filename, 'rb') as f:
        batch = pickle.load(f, encoding='latin1')
        images = batch['data']
        labels = batch['labels']
    return images, labels


def reshape_images(images):
    images = images.reshape(-1, 3, 32, 32)
    images = np.transpose(images, (0, 2, 3, 1))  # Reorder dimensions
    return images

# load model
images, labels = load_cifar_batch(
    'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1'
)
images = reshape_images(images) / 255.0  # normalize

# read from CSV
csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv'
image_ratings = {}

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip title
    for row in reader:
        image_id = int(row[0])
        ratings = list(map(float, row[1:]))  # read all ratings - color, contrast, & shape; && overall
        image_ratings[image_id] = ratings


rated_images = []; rated_labels = []

for img_id, rating in image_ratings.items():
    rated_images.append(images[img_id]); rated_labels.append(rating)
test_images = np.array(rated_images); test_labels = np.array(rated_labels)




# paths
model_paths = {
    "Color": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Color_Model.h5',
    "Contrast": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Contrast_Model.h5',
    "Shape": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Shape_Model.h5',
    "Overall": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Overall_Model.h5',
}

# for each model
    # load
    # eval
    # predict
for i, (rating_type, model_path) in enumerate(model_paths.items()):
    print(f"\nProcessing model: {rating_type}")

    # load the model
    model = load_model(model_path)
    print(f"\n\n{rating_type} model loaded from disk.")

    # evaluate the model
    test_loss, test_mae = model.evaluate(test_images, test_labels, verbose=2)
    print(f"Test MAE ({rating_type} model): {test_mae}")

    # predict with the model (example: first test image)
    predicted_rating = model.predict(np.expand_dims(test_images[0], axis=0))
    print(f"Predicted {rating_type} rating for the first image: {predicted_rating[0][0]}")
