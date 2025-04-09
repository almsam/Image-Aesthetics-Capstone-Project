import os
import pickle
import matplotlib.pyplot as plt
import numpy as np

def load_cifar_batch(filename):
    with open(filename, 'rb') as f:
        batch = pickle.load(f, encoding='latin1')
        images = batch['data']
        labels = batch['labels']
    return images, labels

def reshape_images(images):
    # CIFAR-10 images are 32x32 pixels, RGB (3 tf layers)
    images = images.reshape(-1, 3, 32, 32)
    images = np.transpose(images, (0, 2, 3, 1))  # reorder to (batch_size, height, width, channels)
    return images

# load and reshape the images
images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
images = reshape_images(images)

# labels for CIFAR-10
class_labels = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# create the 'png' folder if it doesn't exist
output_folder = 'png'
os.makedirs(output_folder, exist_ok=True)

# load and reshape the images
images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
images = reshape_images(images)

# get the directory of this script and create the 'png' folder as a sibling
script_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(script_dir, 'png')
os.makedirs(output_folder, exist_ok=True)

# save the first 50 images as PNG files
for i in range(50):
    plt.imsave(os.path.join(output_folder, f'image_{i + 1}.png'), images[i])

print(f"Saved the first 50 images to the '{output_folder}' folder.")
