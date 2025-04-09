# Machine Learning Module for Aesthetic Rating Prediction

This folder contains the machine learning module for predicting aesthetic ratings of CIFAR-10 images using a convolutional neural network (CNN). The primary files are:

- `CNNGraph.py`: Script for running multiple training sessions, recording average metrics, and generating error bar plots of Mean Absolute Error (MAE) over multiple runs
- `CNNConcept.py`: Script demonstrating a basic training and evaluation cycle on a CNN model for predicting aesthetic ratings

## Requirements

This project uses TensorFlow and other common Python libraries for deep learning. Install the dependencies by running:

```bash
pip install -r requirements.txt
```

### Major Dependencies

- `tensorflow` for building and training the CNN model
- `numpy` & `pandas` for data manipulation
- `matplotlib` for visualizing model performance

## Files

### 1. `CNNGraph.py`

This script loads CIFAR-10 images and corresponding aesthetic ratings, trains a CNN model, and evaluates it across multiple runs

Overview:
- **Data Preprocessing**: Loads images and normalizes them, with 90% of the rated images allocated to the training set and 10% to the test set
- **Model Architecture**: 
  - Three convolutional layers with ReLU activation, MaxPooling, & Dropout
  - Fully connected dense layer with dropout for regularization
  - Final dense layer with a single output for rating prediction
- **Training with Multiple Runs**: Repeats training across a few EPOCH's, calculates average MAE, and plots the MAE
- **Plotting Performance**: Generates a plot showing average MAE across training runs, with error bands to highlight model stability

### 2. `CNNConcept.py`

This script provides a simple, single-run training example of the CNN model, including training, evaluation, and visualization of the MAE over epochs

Key Features:
- **Data Preprocessing**: Similar to `CNNGraph.py`
- **Model Architecture**: Same CNN architecture as in `CNNGraph.py`
- **Training and Evaluation**: Trains for 5 epochs and evaluates on the test set, displaying the test MAE
- **Single Run Visualization**: Plots MAE for training and validation over epochs

## Dataset

The model is trained on the CIFAR-10 dataset. Specifically, images are loaded from `data_batch_1` located in:

```
C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/
```

Image ratings are loaded from:

```
C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/prototype_image_ratings.csv
```

These ratings are stored in a CSV format with each row containing:
- `image_id`: Index of the image in CIFAR-10
- `rating`: User-assigned aesthetic rating (1-10)

To get this to run locally on your machine you will need to clone the whole repo & update these 2 paths accordingly

## Usage

1. **Run Multiple Training Sessions**: Use `CNNGraph.py` to train the model across multiple runs and generate a performance plot

    ```bash
    python CNNGraph.py
    ```

2. **Single Run Training and Evaluation**: Use `CNNConcept.py` to train and evaluate a single instance of the CNN model

    ```bash
    python CNNConcept.py
    ```

## Results

Both scripts output the MAE on the test set after training, with `CNNGraph.py` providing an averaged performance view over multiple runs, and `CNNConcept.py` offering a single-run MAE plot

---

