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



# #original - Test MAE: 1.6905971765518188 1.8740997314453125 1.7286865711212158
# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.Flatten())
# model.add(layers.Dense(64, activation='relu'))
# model.add(layers.Dense(1))  # our output is a param of 1 int

# #deeper - Test MAE: 1.8830822706222534 1.9497720003128052 1.8288532495498657
# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.Conv2D(32, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Flatten())
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dense(1))

# #wider - Test MAE: 1.7672028541564941 1.7378004789352417 1.74454927444458
# model = models.Sequential()
# model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Dropout(0.25))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Dropout(0.25))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Flatten())
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(1))


# #pool instead of flattening - Test MAE: 1.9808818101882935 2.155207395553589 1.9429112672805786
# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.GlobalAveragePooling2D())
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dense(1))


# #deepwise - Test MAE: 2.4067673683166504 2.2836754322052 2.6195974349975586
# model = models.Sequential()
# model.add(layers.SeparableConv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.SeparableConv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.SeparableConv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Flatten())
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dense(1))

### the original & wider had the best numbers, but wider was the most stable, so lets experiment more there

# #original - Test MAE: 2.1775565147399902 1.9907641410827637 1.8713759183883667 1.813438892364502 2.0066592693328857 1.9775497913360596 2.0425102710723877
# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.Flatten())
# model.add(layers.Dense(64, activation='relu'))
# model.add(layers.Dense(1))  # our output is a param of 1 int

# #wider - Test MAE: 1.7348178625106812 1.7924838066101074 1.7346808910369873 1.8982186317443848 1.8729251623153687 1.6898002624511719 1.737528681755066
# model = models.Sequential()
# model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Dropout(0.25))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Dropout(0.25))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Flatten())
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(1))

### looks like we're going to use wider as that provided stability & accuracy
### both consistently stabilized after 2-4 epochs, see issue #60, #61, #62, & #63 for progress on fighting over-fit 

# # # model = models.Sequential()
# # # model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# # # model.add(layers.MaxPooling2D((2, 2)))
# # # model.add(layers.Dropout(0.25))
# # # model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# # # model.add(layers.MaxPooling2D((2, 2)))
# # # model.add(layers.Dropout(0.25))
# # # model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# # # model.add(layers.MaxPooling2D((2, 2)))
# # # model.add(layers.Flatten())
# # # model.add(layers.Dense(128, activation='relu'))
# # # model.add(layers.Dropout(0.5))
# # # model.add(layers.Dense(1))


# #deepwide - Test MAE: 5.632107734680176 6.425512313842773 4.6033549308776855
# # worked in my head, but in practice is worse then guessing
# model = models.Sequential()
# model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(32, 32, 3)))
# model.add(layers.BatchNormalization())
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Dropout(0.25))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.BatchNormalization())
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Dropout(0.25))
# model.add(layers.Conv2D(256, (3, 3), activation='relu'))
# model.add(layers.BatchNormalization())
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Dropout(0.5))
# model.add(layers.Flatten())
# model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(1))


# # inception - Test MAE: 1.8733185529708862 2.0098676681518555 1.7741690874099731
# # not bad, but very complicated & unstable - if this has potential this is definetly beyond my skill level
# model = models.Sequential()
# def inception_module(x, filters):
#     path1 = layers.Conv2D(filters, (1, 1), padding='same', activation='relu')(x)
#     path2 = layers.Conv2D(filters, (3, 3), padding='same', activation='relu')(x)
#     path3 = layers.Conv2D(filters, (5, 5), padding='same', activation='relu')(x)
#     return layers.concatenate([path1, path2, path3], axis=-1)
# inputs = tf.keras.Input(shape=(32, 32, 3))
# x = inception_module(inputs, 64)
# x = layers.MaxPooling2D((2, 2))(x)
# x = layers.Dropout(0.25)(x)
# x = inception_module(x, 128)
# x = layers.MaxPooling2D((2, 2))(x)
# x = layers.Dropout(0.5)(x)
# x = layers.Flatten()(x)
# x = layers.Dense(128, activation='relu')(x)
# x = layers.Dropout(0.5)(x)
# outputs = layers.Dense(1)(x)
# model = models.Model(inputs, outputs)

# # residual mark 2 - disregard, couldnt get this to work either
# input_shape = (32, 32, 3)
# inputs = tf.keras.Input(shape=input_shape)
# # block 1
# x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(inputs)
# x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
# x = layers.MaxPooling2D((2, 2))(x)
# x = layers.Dropout(0.25)(x)
# # block 2 w/ residual connection
# y = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
# y = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(y)
# x = layers.add([x, y])
# x = layers.MaxPooling2D((2, 2))(x)
# x = layers.Dropout(0.25)(x)
# # flatten n dense
# x = layers.Flatten()(x)
# x = layers.Dense(128, activation='relu')(x)
# x = layers.Dropout(0.5)(x)
# outputs = layers.Dense(1)(x)
# model = models.Model(inputs, outputs)


# final product:

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
model.add(layers.Dense(1))

# compile time
model.compile(optimizer='adam', 
              loss='mean_squared_error',
              metrics=['mae'])  # avg abs error



# training line
history = model.fit(train_images, train_labels, epochs=10, validation_split=0.2)

# evaluate
test_loss, test_mae = model.evaluate(test_images, test_labels, verbose=2)
print(f'Test MAE: {test_mae}')



# predict time
predicted_rating = model.predict(np.expand_dims(test_images[0], axis=0))
print(f"Predicted rating for the image: {predicted_rating[0][0]}")



import matplotlib.pyplot as plt

plt.plot(history.history['mae'], label='train MAE'); plt.plot(history.history['val_mae'], label='test MAE')
plt.xlabel('num epochs'); plt.ylabel('avg AE'); plt.legend(); plt.show()