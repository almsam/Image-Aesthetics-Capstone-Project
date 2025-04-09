import pickle
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

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
images = reshape_images(images)

class_labels = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck']

csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv'
file_exists = os.path.exists(csv_file)

# meth to find the largest image ID already rated
def get_last_rated_image_id(csv_file):
    if not os.path.exists(csv_file):
        return -1  # If no CSV exists, start from the beginning
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip zero index
        last_id = -1
        for row in reader:
            if row:  # ensure row isn't  empty
                last_id = int(row[0])
        return last_id

# get final entries ID
last_rated_image_id = get_last_rated_image_id(csv_file)

# append mode in CSV
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)
    
    #header if first run
    if not file_exists:
        writer.writerow(['Image ID', 'Rating'])

    # show_image_and_rate_terminal
    def show_image_and_rate_terminal(n):
        plt.imshow(images[n])
        plt.title(f"label: {class_labels[labels[n]]} (ID: {n})")
        plt.axis('off')
        plt.show()
        
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

        # commit to CSV
        writer.writerow([n, rating])
        print(f"image {n} rated {rating}")
        f.flush()

    # pate all
    def rate_all_images():
        start_index = last_rated_image_id + 1
        for n in range(start_index, len(images)):
            show_image_and_rate_terminal(n)
            continue_rating = input("Rate another? (y/n): ").lower()
            if continue_rating != 'y':
                print("Exiting")
                break

    # run4
    rate_all_images()
