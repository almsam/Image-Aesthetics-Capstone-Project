# Doccumentation for the ML

This directory focuses on generating and optimizing images using CNN models. We use a convolutional neural network (CNN henceforth) trained to predict the aesthetic score (IE how likely it is an image will be chosen), and uses gradient ascent to refine generated images for maximum aesthetic appeal.










# Requirements:

### Python 3.x with the following:
- Math packages:
   - NumPy
   - Matplotlib

- ML packages:
   - TensorFlow
   - TensorFlow with Keras
   - SciPy.ndimage

- Data & System packages:
   - sys
   - os
   - csv
   - collections
   - pickle (formerly)

### Installation:

To install, use:

``` sh
   pip install numpy matplotlib tensorflow scipy
   # Since sys, os, csv, collections, & pickle are built in to Py3, no need to install them
```

Then verify the installation was successful using:

```Py
   import numpy as np
   import matplotlib.pyplot as plt

   import tensorflow as tf
   from tensorflow.keras.models import load_model
   from tensorflow.keras.preprocessing.image import save_img, img_to_array, load_img
   from scipy.ndimage import convolve, zoom

   import sys
   import os
   import csv
   from collections import defaultdict
   import pickle
```

---


# Main Files:

---

## GenerateImage.py:
#### Info:
   - Generates new images based on a given seed
   - Applies nearest neighbor, or hex smoothing techniques followed by interpolation to enhance image quality
   - Saves processed images to a specified output directory
   - Depends on:
      - `GenerateImagesPrototype.py` to generate base images.

#### Example usage:
   ``` Py
   import os
   from GenerateImage import *

   # First we define our output directory
   script_dir = os.path.dirname(os.path.abspath(__file__))
   output_dir = os.path.join(script_dir, "public", "data", "temp")
   os.makedirs(output_dir, exist_ok=True)

   # then we generate an image with a specific seed
   seed = 12345
   generated_image = generateQuality(seed, output_dir, n=72)

   print(f"Generated and saved image for seed {seed} in {output_dir}")

   ```

   Where seed is the seed, output_dir is where the image is saved, & n is the quality coefficient

   n is in units of 32 pixels - so to generate a 2304x2304 image, you will need (32x72 pixels)x(32x72 pixels)

   This code will save an image to the designated location

---

## GenerateImagesPrototype.py

#### Info:
   - Loads a trained CNN model (`VAST_CNN_Main_Model.h5`) to assess and improve image aesthetics
   - Implements gradient ascent to optimize images & uses color quantization to simplify images into B&W
   - Generates an aesthetically optimized image based on a seed value

#### Example usage:
   ``` Py
   import os
   from GenerateImagePrototype import *


   image = GenerateImagesPrototype.generate_New_Image(seed)
   ```

   Where seed is the seed to ensure the image is deterministic

   This code will return a `numpy.ndarray` representation of a 32x32x[Black/White/Grey] image you can play with

---


## VASTCNNMain.py

#### Info:
   - Loads and processes images from the VAST dataset
   - Reads images from `data/VAST Images/*`
   - Reads sample aesthetic ratings for those images from `data/vast_image_ratings.csv`
   - Prepares images and ratings for training and testing our CNN
   - Implements color quantization to B/W/G to reduce complexity in image representation

   It works by running a regression to train our model to predict the aesthetic score

   It then saves the model as `ml/models/VAST_CNN_Main_Model.h5`

---

# Smaller Files:


## VASTReadModelMain.py
#### Info:
   This is simply a file to confirm the .h5 exists & can be used to do cool things



## GeneratedGallery.py & OutputGallery.py
#### Info:
   These 2 files generate the images: `generate gallery_4seeds.png` & `hd_gallery_20seeds.png`, which can be seen below 



## gallery_4seeds.png & hd_gallery_20seeds.png
| ![gallery_4seeds](gallery_4seeds.png)      | ![hd_gallery_20seeds](hd_gallery_20seeds.png)   |
|-------------------------|-------------------------|



## GeneratedGalleryTest.py & OutputGalleryTest.py
#### Info:
   Test cases for `GeneratedGallery.py` & `OutputGallery.py`



## ExperimentM3.md
#### Info:
   Summarizes an experiment we did for M3 - cool stuff id recommend checking out



## GenerateImagesPrototypeTest.py
#### Info:
   Test case for `GenerateImagesPrototype.py`



## GenerateImageTest.md & GenerateImageTest.py
#### Info:
   Test cases for `GenerateImage.py`
   The Py version runs automated tests, the md runs a snapshot test


## ExampleUsage.py & ExampleUsageTest.py
#### Info:
   Verifies sample cases from this file


## VASTCNNMainTest.py
#### Info:
   Test case for `VASTCNNMain.py`


## VASTCNNTestPixelate.py
#### Info:
   Test case to verify a pixelation script worked when this was in progress
   It will be kept around as this test would fail in the case of a new source of error in 1 half of the stream


## VASTReadModelMainTest.py
#### Info:
   Test cases for `VASTReadModelMain.py`

---

# Directories:

## `concept/`
#### Info:
   Previous repo on the *CIFAR-10* dataset (as oppose to the current *VAST* dataset)
   Acted as proof of concept & kept around as I still rip lines of code from there

   This section focuses on the Prototype of the CNN model

## `data/`
#### Info:
   A convenient place to save generated images during rapid prototyping

## `ML cifar 10 (unused)/`
#### Info:
   Previous repo on the *CIFAR-10* dataset (as oppose to the current *VAST* dataset)
   Acted as proof of concept & kept around as I still rip lines of code from there

   This section focuses on the specifics of our CNN model

## `models/`
#### Info:
   A convenient place to save AI models












Developed for the **Order of Aesthetics Capstone Project** by Samira







