import os
import csv
import matplotlib.pyplot as plt
from PIL import Image

def get_next_uid(csv_file):
    if not os.path.exists(csv_file): return 0 #0 if no file

    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        uids = [int(row['UID']) for row in reader if row['UID'].isdigit()]  # get UID s
        return max(uids, default=0) + 1  # max U ID + 1

def get_next_rating_id(csv_file):
    if not os.path.exists(csv_file): return 0 

    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        rating_ids = [int(row['Rating ID']) for row in reader if row['Rating ID'].isdigit()]
        return max(rating_ids, default=0) + 1


# load images
def load_vast_images(directory, num_images=None):
    image_files = [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    if num_images: image_files = image_files[:num_images]
    images = [Image.open(os.path.join(directory, file)) for file in image_files]
    return images, image_files

# get last rated image pair ID
def get_last_rated_pair_id(csv_file):
    if not os.path.exists(csv_file): return -1  # no file exists
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        last_id = -1
        for row in reader:
            if row: last_id = int(row[0])
        return last_id

# display two images side by side and get user's choice
def show_images_and_get_choice(img_left, img_right, img_id_left, img_id_right):
    plt.figure(figsize=(8, 4))
    
    #   L
    plt.subplot(1, 2, 1); plt.imshow(img_left); plt.title(f"Left (ID: {img_id_left})"); plt.axis('off')

    #   R
    plt.subplot(1, 2, 2); plt.imshow(img_right); plt.title(f"Right (ID: {img_id_right})"); plt.axis('off')

    plt.tight_layout(); plt.show()

    # get input
    while True:
        choice = input("Choose 'L' for Left or 'R' for Right (or 'ctrl'+'c' then 'S' to Skip): ").strip().upper()
        if choice in ['L', 'R', 'S']: return choice
        print("Invalid. Please choose 'L', 'R', or 'S'.")

# save the choice to CSV
def save_rating_to_csv(writer, UID, pair_id, choice, img_id_left, img_id_right):
    if choice == 'L':
        # left image rated 1 (good), right image rated 0 (bad)
        writer.writerow([UID, pair_id, img_id_left, 1])
        writer.writerow([UID, pair_id + 1, img_id_right, 0])
        print(  f"Saved: Entry {pair_id} (UID {UID}, ID {img_id_left}, Rating 1), "
                f"Entry {pair_id + 1} (UID {UID}, ID {img_id_right}, Rating 0)")
    elif choice == 'R':
        # right image rated 1 (good), left image rated 0 (bad)
        writer.writerow([UID, pair_id, img_id_left, 0])
        writer.writerow([UID, pair_id + 1, img_id_right, 1])
        print(  f"Saved: Entry {pair_id} (UID {UID}, ID {img_id_left}, Rating 0), "
                f"Entry {pair_id + 1} (UID {UID}, ID {img_id_right}, Rating 1)")
    else:
        print(f"Skipped: Pair {pair_id}")

# Main
def rate_vast_images(vast_images_dir, csv_file):
    images, filenames = load_vast_images(vast_images_dir)
    last_rated_pair_id = get_last_rated_pair_id(csv_file)
    file_exists = os.path.exists(csv_file)
    UID = get_next_uid(csv_file)

    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)

        # header
        if not file_exists:
            writer.writerow(['UID', 'Rating ID', 'Image ID', 'Rating'])

        # rate  pairs
        pair_id = get_next_rating_id(csv_file)
        print(pair_id)
        for i in range(0, len(images), 2):
            if i + 1 >= len(images):  # skip last image if odd number of images
                print("Odd number of images, skipping the last image.")
                break
            
            img_left = images[i]; img_right = images[i + 1]
            img_id_left = filenames[i]; img_id_right = filenames[i + 1]

            choice = show_images_and_get_choice(img_left, img_right, img_id_left, img_id_right)
            if choice == 'S':  #  skip pair
                continue
            save_rating_to_csv(writer, UID, pair_id, choice, img_id_left, img_id_right)
            f.flush(); pair_id = get_next_rating_id(csv_file) # comit to file

            # if we continue
            continue_rating = input("Rate another pair? (y/n): ").strip().lower()
            if continue_rating != 'y':
                print("Exiting rating application.")
                break

vast_images_dir = r'C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\data\VAST Images'
csv_file = r'C:\Users\samia\OneDrive\Desktop\cosc 499\capstone-project-team-9-Order-Of-Aesthetics\data\vast_image_ratings.csv'

# run app
rate_vast_images(vast_images_dir, csv_file)
