# Machine Learning Module for Aesthetic Rating Prediction

This folder contains the machine learning module for predicting aesthetic ratings of sample images using convolutional neural networks (henceforth CNNs). The directory includes scripts for training, evaluating, and saving models, as well as surrogate models that assess multiple aesthetic dimensions we can hopefully use for insight in our milestone 2 experiment.

## Requirements

To run this project, install the required dependencies using:

```bash
py -m pip install tensorflow
```

### Major Dependencies
the project is programmed in [![Py][Py]][PyUrl] using
- [![TF][TF]][TFURL]: For building and training CNN models
- [![Numpy][Numpy]][Numpy-url] & [![Pandas][Pandas]][Pandas-url]: For data processing
- [![Matplotlib][Matplotlib]][Matplotlib-url]: For visualizing results (optional)


[Pandas]: https://img.shields.io/badge/Pandas%20-%20%23150458?logo=pandas&logoColor=%23FFFFFF&logoSize=auto
[Pandas-url]: https://pandas.pydata.org/

[TF]: https://img.shields.io/badge/TensorFlow%20-%20%23FF6F00?logo=tensorflow&logoColor=%23FFFFFF&logoSize=auto
[TFURL]: https://www.tensorflow.org
[Py]: https://img.shields.io/badge/Python%20-%20%233e50b5?logo=python&logoColor=%23FFDE57&logoSize=auto
[PyUrl]: https://www.python.org

[Numpy]: https://img.shields.io/badge/NumPy-%20%23013243?logo=numpy&logoColor=%23FFFFFF&logoSize=auto
[Numpy-url]: https://numpy.org/
[Matplotlib]: https://img.shields.io/badge/MatPlotLib-%20%2345ca9a?logo=python&logoColor=%23FFFFFF&logoSize=auto
[Matplotlib-url]: https://matplotlib.org/

---

## Files and Functionality

### 1. `CNNMain.py`

**Purpose**: Train and evaluate a CNN model to predict overall aesthetic ratings. This is the primary CNN I have worked on during my time here

**Features**:
- **Data Preprocessing**: Loads CIFAR-10 images and normalizes them. Filters images based on ratings stored in a CSV file.
- **Model Architecture**:
  - Three convolutional layers (ReLU activation, MaxPooling, & Dropout)
  - A fully connected dense layer with Dropout for regularization
  - A final dense layer with a single output for predicting aesthetic ratings
- **Training and Evaluation**:
  - Train test split (90% for training, 10% for testing)
  - Trains for 5 epochs with MAE as the evaluation metric
  - Saves the trained model
- **Output**: 
  - Test Mean Absolute Error (MAE)
  - Predicted rating for a single test image
  - Optionally plots training/validation MAE over epochs

Run the script:
```bash
python CNNMain.py
```

---

### 2. `CNNSurrogate.py`

**Purpose**: Train surrogate models for different aesthetic dimensions (e.g., color, contrast, shape, and overall ratings). The goal with this one is finding insights on what different demographics enjoy

**Features**:
- **Data Preprocessing**: Similar to `CNNMain.py` but processes ratings for specific categories stored in `prototype_image_ratings_detailed.csv`.
- **Model Training**: 
  - Separate models for each aesthetic dimension
  - Saves models for `color`, `contrast`, `shape`, and `overall` ratings
- **Output**:
  - MAE for each surrogate model
  - Saves each trained model with a descriptive filename (e.g., `CNN_Color_Model.h5`)

Run the script:
```bash
python CNNSurrogate.py
```

---

### 3. `ReadModelMain.py`

**Purpose**: Loads the trained main model from `CNNMain.py` (`CNN_Main_Model.h5`) for use in the overall product later on

**Features**:
- Loads test images and labels from the dataset
- Evaluates the model on the test set
- Predicts the aesthetic rating for a sample test image

Run the script:
```bash
python ReadModelMain.py
```

---

### 4. `ReadSurrogate.py`

**Purpose**: Load trained surrogate models (`CNN_Color_Model.h5`, `CNN_Contrast_Model.h5`, etc.) for use in later experiments 

**Features**:
- Loads and evaluates each surrogate model
- Predicts ratings for specific aesthetic dimensions (e.g., color, contrast, shape)

Run the script:
```bash
python ReadSurrogate.py
```

---

## Dataset

### CIFAR-10 Images
- Path: `C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/cifar-10-batches-py/data_batch_1`
- Images are normalized to [0, 1] and reshaped to 32x32x3 format.

### Ratings
- **Overall Ratings**: `prototype_image_ratings.csv`
  - Columns: `image_id`, `rating`
- **Detailed Ratings**: `prototype_image_ratings_detailed.csv`
  - Columns: `image_id`, `color`, `contrast`, `shape`, `overall`

---

## Results

1. **Main Model** (`CNNMain.py`):
   - Test MAE and predicted ratings for the overall aesthetic score.

2. **Surrogate Models** (`CNNSurrogate.py`):
   - Test MAE and predicted ratings for individual dimensions: color, contrast, shape, and overall.

3. **Visualization**:
   - Optional training/validation MAE plots.

---

## Usage Notes

- **Paths**: Update file paths in scripts to match your local setup.
- **Training**: Use `CNNMain.py` for overall aesthetic ratings and `CNNSurrogate.py` for specific dimensions.
- **Evaluation**: Use `ReadModelMain.py` and `ReadSurrogate.py` for testing and predictions on saved models.

---

## Future Enhancements

- Add support for training on additional datasets.
- Optimize hyperparameters to improve MAE.
- Explore advanced architectures like ResNet or EfficientNet for better accuracy.

--- 

This README aligns with your scripts and includes clear usage instructions for users. Let me know if further refinements are needed!
