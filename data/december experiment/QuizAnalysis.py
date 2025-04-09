import os
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# list of DataFrames
dfs = []

for i in range(1, 11):  # # each file from ratings1.csv to ratings10.csv
    file_name = f"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/quiz results/ratings{i}.csv"  # general file name
    df = pd.read_csv(file_name); dfs.append(df)

file_name = f"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/quiz results/ratings_Youry.csv"
df = pd.read_csv(file_name); dfs.append(df)
file_name = f"C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/quiz results/ratings_Jerry.csv"
df = pd.read_csv(file_name); dfs.append(df)

# for idx, df in enumerate(dfs, start=1):
#     print(f"DataFrame {idx}:")#     print(df.head())
# data_frames = [pd.DataFrame({'PairId': [1, 2], 'SelectedImageId': [1, 4]}) for _ in range(10)]

# example imagePairs
imagePairs = [
    [{"id": 1},  {"id": 2}],  [{"id": 3}, {"id": 4}],   [{"id": 5}, {"id": 6}],   [{"id": 7}, {"id": 8}],   [{"id": 9}, {"id": 10}],  [{"id": 11}, {"id": 12}], [{"id": 13}, {"id": 14}], [{"id": 15}, {"id": 16}], [{"id": 17}, {"id": 18}], [{"id": 19}, {"id": 20}], [{"id": 21}, {"id": 22}], [{"id": 23}, {"id": 24}], [{"id": 25}, {"id": 26}], [{"id": 27}, {"id": 28}],
    [{"id": 29}, {"id": 30}], [{"id": 31}, {"id": 32}], [{"id": 33}, {"id": 34}], [{"id": 35}, {"id": 36}], [{"id": 37}, {"id": 38}], [{"id": 39}, {"id": 40}], [{"id": 41}, {"id": 42}], [{"id": 43}, {"id": 44}], [{"id": 45}, {"id": 46}], [{"id": 47}, {"id": 48}], [{"id": 49}, {"id": 50}],
    
    [{"id": 1}, {"id": 37}],  [{"id": 2}, {"id": 15}],  [{"id": 3}, {"id": 22}],  [{"id": 4}, {"id": 40}],  [{"id": 5}, {"id": 9}],   [{"id": 6}, {"id": 28}],  [{"id": 7}, {"id": 44}], [{"id": 8}, {"id": 17}],  [{"id": 9}, {"id": 6}],   [{"id": 10}, {"id": 31}], [{"id": 11}, {"id": 48}], [{"id": 12}, {"id": 3}],  [{"id": 13}, {"id": 25}], [{"id": 14}, {"id": 50}],
    [{"id": 15}, {"id": 4}],  [{"id": 16}, {"id": 38}], [{"id": 17}, {"id": 20}], [{"id": 18}, {"id": 11}], [{"id": 19}, {"id": 23}], [{"id": 20}, {"id": 7}],  [{"id": 21}, {"id": 46}], [{"id": 22}, {"id": 12}], [{"id": 23}, {"id": 42}], [{"id": 24}, {"id": 33}], [{"id": 25}, {"id": 1}],
]

# convert imagePairs to a dictionary for easier lookup
pair_lookup = {i + 1: (pair[0]["id"], pair[1]["id"]) for i, pair in enumerate(imagePairs)}

for df in dfs: # add cols
    df["Image1Id"] = df["QuestionNumber"].map(lambda q: pair_lookup[q][0]); df["Image2Id"] = df["QuestionNumber"].map(lambda q: pair_lookup[q][1])

#snapshot test print(dfs[7])
# read each in DF's

print("\n\n\n\n\n **SNAPSHOT TEST 1/5:** \n\n VERIFY 10 DATA FRAMES WITH QUESTION NUMBER, THE 2 IMAGES TO COMPARE, AND THE USER SELECTED ONE \n\n\n\n\n")
for idx, df in enumerate(dfs, start=1):
    print(f"\n\n DataFrame {idx}: \n"); print(df.head())
print("\n\n\n\n\n")





# load CNN model

model_paths = {
    "Color": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Color_Model.h5',
    "Contrast": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Contrast_Model.h5',
    "Shape": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Shape_Model.h5',
    "Overall": 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/ml/models/CNN_Overall_Model.h5',  # overall from 'main' & not 'overall'
}
model_overall = load_model(model_paths["Overall"]); print("Overall model loaded from disk.")
# load pictures
png_folder = 'C:/Users/samia/OneDrive/Desktop/cosc 499/capstone-project-team-9-Order-Of-Aesthetics/data/png'

# read png n preprocess
image_data = []
for i in range(1, 51):  # for the first 50 images
    image_path = os.path.join(png_folder, f'image_{i}.png')
    image = plt.imread(image_path)  # read image
    
    # Ensure the image has 3 channels (RGB), if it has 4 (RGBA), remove the alpha channel
    if image.shape[-1] == 4:  # Check if the image has an alpha channel
        image = image[..., :3]  # Keep only the RGB channels
    
    image = image / 255.0  # normalize img
    image_data.append(image)

# NumPy array for prediction
image_data = np.array(image_data)
predictions = {}

for rating_type in ["Color", "Contrast", "Shape"]: # 3 surrogate models
    model = load_model(model_paths[rating_type]); print(f"{rating_type} model loaded from disk.")
    predicted_ratings = model.predict(image_data) #use CNN to guess rating
    predictions[rating_type] = predicted_ratings.flatten()  # Flatten predictions to 1D array


predicted_overall_ratings = model_overall.predict(image_data)
predictions["Overall"] = predicted_overall_ratings.flatten()  # Flatten predictions to 1D array

# results df to store the results
results_df = pd.DataFrame({
    'ImageID': [f'image_{i}.png' for i in range(1, 51)],
    'ColorRating': predictions["Color"],
    'ContrastRating': predictions["Contrast"],
    'ShapeRating': predictions["Shape"],
    'OverallRating': predictions["Overall"],  #  CNN_Main_Model
})

# results_df.to_csv(output_csv, index=False) # print(f"Predicted ratings saved to {output_csv}")

print("\n\n\n\n\n **SNAPSHOT TEST 2/5:** \n\n VERIFY EACH IMAGE HAS 3 ATTRIBUTE RATINGS & AN OVERALL RATING - MAKE SURE THESE ROUGHLY MATCH WHAT EACH OTHER SAY & ROUGHLY SUM UP TO OVERALL \n\n\n\n\n")
print(results_df.head())# snapshot test/preview
print("\n\n\n\n\n")







question_numbers = []
best_color = []
best_contrast = []
best_shape = []
best_overall = []

# for all image pairs
for question_number, pair in enumerate(imagePairs, start=1):
    img1_id = pair[0]["id"]
    img2_id = pair[1]["id"]
    
    # get the neural networks ratings for these 2
    img1 = results_df.loc[results_df['ImageID'] == f'image_{img1_id}.png']; img2 = results_df.loc[results_df['ImageID'] == f'image_{img2_id}.png']
    
    # compare & let best image win
    best_color_id = img1_id if img1['ColorRating'].values[0] > img2['ColorRating'].values[0] else img2_id; best_contrast_id = img1_id if img1['ContrastRating'].values[0] > img2['ContrastRating'].values[0] else img2_id
    best_shape_id = img1_id if img1['ShapeRating'].values[0] > img2['ShapeRating'].values[0] else img2_id; best_overall_id = img1_id if img1['OverallRating'].values[0] > img2['OverallRating'].values[0] else img2_id
    
    # append results to respectiv list
    question_numbers.append(question_number)
    best_color.append(best_color_id)
    best_contrast.append(best_contrast_id)
    best_shape.append(best_shape_id)
    best_overall.append(best_overall_id)

# make comparison df with the appropriate columns
comparison_df = pd.DataFrame({'QuestionNumber': question_numbers, 'bestColor': best_color, 'bestContrast': best_contrast, 'bestShape': best_shape, 'Bestoverall': best_overall})

print("\n\n\n\n\n **SNAPSHOT TEST 3/5:** \n\n VERIFY EACH QUESTION COMPARES THE CORRECT PAIR OF 2 IMAGES & CLASSIFIES A BEST OVERALL & IN THE 3 SUB RACES \n\n\n\n\n")
print(comparison_df.head())# another snapshot test
print("\n\n\n\n\n")



# add 4 boolean columns to each data frame in dfs
for df in dfs:
    df['BestColorMatch'] = (df['SelectedImageId'] == (comparison_df['bestColor'])).astype(int); df['BestContrastMatch'] = (df['SelectedImageId'] == (comparison_df['bestContrast'])).astype(int)
    df['BestShapeMatch'] = (df['SelectedImageId'] == (comparison_df['bestShape'])).astype(int); df['BestOverallMatch'] = (df['SelectedImageId'] == (comparison_df['Bestoverall'])).astype(int)

print("\n\n\n\n\n **SNAPSHOT TEST 4/5:** \n\n VERIFY 10 DATA FRAMES WITH QUESTION NUMBER, THE 2 IMAGES TO COMPARE, AND THE USER SELECTED ONE -- AS WELL AS THE BOOLEANS FOR IF THE NEURAL NET GOT THE SAME \n\n\n\n\n")
for idx, df in enumerate(dfs, start=1):
    print(f"\n\n DataFrame {idx}: \n"); print(df.head())
print("\n\n\n\n\n")






final_data = []

# calculate the sum of the boolean columns for each df - 
for df in dfs:
    best_color_sum = df['BestColorMatch'].sum(); best_contrast_sum = df['BestContrastMatch'].sum(); best_shape_sum = df['BestShapeMatch'].sum(); best_overall_sum = df['BestOverallMatch'].sum()
    best_color_sum = best_color_sum/50; best_contrast_sum = best_contrast_sum/50; best_shape_sum = best_shape_sum/50; best_overall_sum = best_overall_sum/50
    final_data.append([best_color_sum, best_contrast_sum, best_shape_sum, best_overall_sum])

final_df = pd.DataFrame(final_data, columns=['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']) # final 4x10 DataFrame


# user demographic data df
user_data = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'user_name': ['jade', 'kaycee', 'terrence', 'Nat', 'Athish', 'emma', 'journey', 'alex foot', 'Benji', 'alex fanat', 'Professor Youry', 'TA'],
    'userAge': [24, 21, 22, 20, 21, 26, 22, 29, 26, 24, 77, 32],
    'userGender': ['F', 'F', 'M', 'X', 'M', 'F', 'X', 'F', 'X', 'M', 'M', 'M'],
    'visualArtsCourse': [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
})

# merge user demographic data with final_df
final_df['user_id'] = user_data['user_id'].values; final_df['user_name'] = user_data['user_name'].values; final_df['userAge'] = user_data['userAge'].values
final_df['userGender'] = user_data['userGender'].values; final_df['visualArtsCourse'] = user_data['visualArtsCourse'].values

#order 
final_df = final_df[['user_id', 'user_name', 'userAge', 'userGender', 'visualArtsCourse', 'BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']]


print("\n\n\n\n\n **SNAPSHOT TEST 5/5:** \n\n VERIFY ALL 10 DATA FRAMES ARE AVERAGED IN ALL 4 PARAMETERS \n\n\n\n\n")
print(final_df)
