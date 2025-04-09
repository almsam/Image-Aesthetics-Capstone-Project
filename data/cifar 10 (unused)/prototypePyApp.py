import pickle
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

# load_cifar_batch
def load_cifar_batch(filename):
    with open(filename, 'rb') as f:
        batch = pickle.load(f, encoding='latin1')
        images = batch['data']
        labels = batch['labels']
    return images, labels

# reshape_images
def reshape_images(images):
    images = images.reshape(-1, 3, 32, 32)
    images = np.transpose(images, (0, 2, 3, 1))  # Reorder to (batch_size, height, width, channels)
    return images

# impprt images
images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
images = reshape_images(images)

# CIFAR-10 labels
class_labels = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# run the CSV to store image ratings
csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv'
file_exists = os.path.exists(csv_file)

# append csv
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)
    
    # write header (IFF first run)
    if not file_exists:
        writer.writerow(['Image ID', 'Rating'])

    # show_image_and_rate_terminal
    def show_image_and_rate_terminal(n):
        plt.imshow(images[n]); plt.title(f"label: {class_labels[labels[n]]} (ID: {n})"); plt.axis('off'); plt.show() # matplot lib stuff to display

        # get rating
        while True:
            try:
                rating = int(input(f"rate image {n} (1-10): "))
                if 1 <= rating <= 10:
                    break
                else:
                    print("rating must be between 1 and 10 -- try again:")
            except ValueError:
                print("invalid input; rating must be between 1 and 10 -- try again:")

        # appebnd csv
        writer.writerow([n, rating])
        print(f"image {n} rated {rating}")
        f.flush()  # push

    # O(all images) * rate time
    # rate_all_images
    def rate_all_images():
        for n in range(len(images)):
            show_image_and_rate_terminal(n)
            continue_rating = input("Rate another? (y/n): ").lower()
            if continue_rating != 'y':
                print("Exiting")
                break

    rate_all_images()
