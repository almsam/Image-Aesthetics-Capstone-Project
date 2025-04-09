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
    images = np.transpose(images, (0, 2, 3, 1))  # Reorder to (batch_size, height, width, channels)
    return images

# load n reshape
images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
images = reshape_images(images)

# labels for CIFAR-10
class_labels = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# preview 5
num_images_to_show = 5
plt.figure(figsize=(10, 2))

for i in range(num_images_to_show):
    plt.subplot(1, num_images_to_show, i + 1)
    plt.imshow(images[i])
    plt.title(class_labels[labels[i]])
    plt.axis('off')

plt.show()
