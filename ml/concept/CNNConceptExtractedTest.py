import unittest
import os
import numpy as np
import pickle
import csv
from tensorflow.keras import models, layers
import tensorflow as tf

class TestImageModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.images, cls.labels = cls.load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
        cls.images = cls.reshape_images(cls.images) / 255.0
        
        cls.image_ratings = cls.load_csv_ratings('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv')
        cls.rated_images, cls.rated_labels = cls.filter_rated_images(cls.images, cls.image_ratings)
        
        cls.train_images = np.delete(cls.rated_images, np.arange(0, cls.rated_images.shape[0], 10), axis=0)
        cls.train_labels = np.delete(cls.rated_labels, np.arange(0, cls.rated_labels.shape[0], 10), axis=0)
        cls.test_images = cls.rated_images[::10]
        cls.test_labels = cls.rated_labels[::10]
        
        cls.model = cls.build_model()

    @staticmethod
    def load_cifar_batch(filename):
        with open(filename, 'rb') as f:
            batch = pickle.load(f, encoding='latin1')
            images = batch['data']
            labels = batch['labels']
        return images, labels

    @staticmethod
    def reshape_images(images):
        images = images.reshape(-1, 3, 32, 32)
        images = np.transpose(images, (0, 2, 3, 1))  # order: batch_size, height, width, channels
        return images

    @staticmethod
    def load_csv_ratings(csv_file):
        image_ratings = {}
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # omit first line
            for row in reader:
                image_id, rating = int(row[0]), int(row[1])
                image_ratings[image_id] = rating
        return image_ratings

    @staticmethod
    def filter_rated_images(images, image_ratings):
        rated_images = []
        rated_labels = []
        for img_id, rating in image_ratings.items():
            rated_images.append(images[img_id])
            rated_labels.append(rating)
        return np.array(rated_images), np.array(rated_labels)

    # @staticmethod
    # def load_images():
    #     images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1') # type: ignore
    #     images = reshape_images(images) / 255.0  # type: ignore # normalize
        
    #     rated_images = []
    #     rated_labels = []
    #     for img_id, rating in image_ratings.items(): # type: ignore
    #         rated_images.append(images[img_id])
    #         rated_labels.append(rating)
    #     rated_images = np.array(rated_images)
    #     rated_labels = np.array(rated_labels)
        
    #     return rated_images, rated_labels

    @staticmethod
    def build_model():
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
        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])  # avg abs error
        return model

        # training line
        # rated_images, rated_labels = load_images() # type: ignore
        # history = model.fit(rated_images, rated_labels, epochs=10, validation_split=0.2)
        # return model

    def test_model_training(self):
        history = self.model.fit(self.train_images, self.train_labels, epochs=10, validation_split=0.2)

        # confirm that the model history contains training and validation MAE
        self.assertIn('mae', history.history)
        self.assertIn('val_mae', history.history)
        
        self.assertLess(history.history['mae'][-1], history.history['mae'][0]) ## error above 0
        # self.assertLess(history.history['val_mae'][-1], history.history['val_mae'][0])

    def test_model_prediction(self):
        # predict rating for our first image
        predicted_rating = self.model.predict(np.expand_dims(self.test_images[0], axis=0))

        # check if the predicted rating is within a reasonable range (+/- 1)
        self.assertGreaterEqual(predicted_rating[0][0], -1)
        self.assertLessEqual(predicted_rating[0][0], 1)

    def test_model_evaluation(self):
        # evaluate
        test_loss, test_mae = self.model.evaluate(self.test_images, self.test_labels, verbose=0)
        
        # make sure average absolute error is legit
        self.assertLessEqual(test_mae, 5)

    def test_split_lengths(self):
        # the lengths of train n test should be 90% and 10%
        expected_train_len = int(0.9 * len(self.rated_images))
        expected_test_len = int(0.1 * len(self.rated_images))
        
        self.assertLessEqual(len(self.train_images) - expected_train_len, 1)
        self.assertLessEqual(len(self.test_images) - expected_test_len, 1) # asserts the difference is less then 1

    def test_prediction_shape(self):
        predicted_rating = self.model.predict(np.expand_dims(self.test_images[0], axis=0))
        
        # assert prediction shape is (1, 1) (such that single output for all img's)
        self.assertEqual(predicted_rating.shape, (1, 1))


if __name__ == '__main__':
    unittest.main()
