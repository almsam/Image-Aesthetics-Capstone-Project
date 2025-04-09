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

# Import images
images, labels = load_cifar_batch('C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1')
images = reshape_images(images)

# CIFAR-10 labels
class_labels = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]

# CSV file path
csv_file = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings_detailed.csv'
file_exists = os.path.exists(csv_file)

# Open CSV for appending
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)

    # Write header (if first run)
    if not file_exists:
        writer.writerow(['Image ID', 'Color Rating', 'Contrast Rating', 'Shape Rating', 'Overall Rating'])

    # Display image and collect ratings
    def show_image_and_rate_terminal(n):
        plt.imshow(images[n])
        plt.title(f"Label: {class_labels[labels[n]]} (ID: {n})")
        plt.axis('off')
        plt.show()  # Show image

        # Helper function to get a valid rating
        def get_rating(prompt):
            while True:
                try:
                    rating = int(input(prompt))
                    if 1 <= rating <= 10:
                        return rating
                    else:
                        print("Rating must be between 1 and 10. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 10.")

        # Get ratings for each category
        color_rating = get_rating(f"Rate the color of image {n} (1-10): ")
        contrast_rating = get_rating(f"Rate the contrast of image {n} (1-10): ")
        shape_rating = get_rating(f"Rate the shape of image {n} (1-10): ")
        overall_rating = get_rating(f"Rate the overall aesthetics of image {n} (1-10): ")

        # Append ratings to the CSV file
        writer.writerow([n, color_rating, contrast_rating, shape_rating, overall_rating])
        print(f"Image {n} rated: Color={color_rating}, Contrast={contrast_rating}, Shape={shape_rating}, Overall={overall_rating}")
        f.flush()  # Save changes to file immediately

    # Rate all images
    def rate_all_images():
        for n in range(len(images)):
            show_image_and_rate_terminal(n)
            continue_rating = input("Rate another? (y/n): ").lower()
            if continue_rating != 'y':
                print("Exiting rating process.")
                break

    rate_all_images()
