import matplotlib.pyplot as plt
import pandas as pd

import statsmodels.api as sm

import QuizAnalysis

df = QuizAnalysis.final_df

# normalize the data
dfNorm = df; dfNorm['BestColorMatch'] = dfNorm['BestColorMatch'] - 0.5; dfNorm['BestContrastMatch'] = dfNorm['BestContrastMatch'] - 0.5
dfNorm['BestShapeMatch'] = dfNorm['BestShapeMatch'] - 0.5;  dfNorm['BestOverallMatch'] = dfNorm['BestOverallMatch'] - 0.5






gender_groups = dfNorm.groupby('userGender')[['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']].mean()

# 3x4 grid of plots (3 rows, 4 columns)
fig, axes = plt.subplots(3, 4, figsize=(18, 9))

# gender
metrics = ['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']  # column names
for i, metric in enumerate(metrics):
    ax = axes[0, i]  # 1st
    gender_groups[metric].plot(kind='bar', ax=ax, color=['skyblue', 'salmon', 'lightgreen'])
    ax.set_title(f'{metric} by Gender')
    ax.set_ylabel('Average Score Minus 50%')
    ax.set_xlabel('Gender')
    ax.set_xticklabels(['M', 'X', 'F'], rotation=0)

# art
arts_groups = dfNorm.groupby('visualArtsCourse')[['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']].mean()
for i, metric in enumerate(metrics):
    ax = axes[1, i]  # 2nd row
    arts_groups[metric].plot(kind='bar', ax=ax, color=['skyblue', 'salmon'])
    ax.set_title(f'{metric} by Visual Arts Course')
    ax.set_ylabel('Average Score Minus 50%')
    ax.set_xlabel('Visual Arts Course')
    ax.set_xticklabels(['No Course', 'Course'], rotation=0)

# age
for i, metric in enumerate(metrics):
    ax = axes[2, i]  # 3rd row
    ax.scatter(df['userAge'], df[metric], color='blue', alpha=0.7)
    ax.set_title(f'{metric} vs Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Score')

plt.tight_layout(); plt.show()



print("\n\n\n\n\n")
print("\n\n\n\n\n")


# lin reg

metrics = ['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']

age_results = {}
for metric in metrics:
    X = sm.add_constant(df['userAge'])  # independent
    y = df[metric]
    model = sm.OLS(y, X).fit(); age_results[metric] = model.params #train n store result
for metric, result in age_results.items(): print(f"Linear Regression Results for {metric} vs Age:"); print(result); print("\n" + "-"*80 + "\n")

art_results = {}
for metric in metrics:
    X = sm.add_constant(df['visualArtsCourse'])  # independent
    y = df[metric]
    model = sm.OLS(y, X).fit(); art_results[metric] = model.params #train n store result
for metric, result in art_results.items(): print(f"Linear Regression Results for {metric} vs Arts Course:"); print(result); print("\n" + "-"*80 + "\n")

gender_mapping = {'M': 0, 'F': 1, 'X': 0.5}; df['userGenderMapped'] = df['userGender'].map(gender_mapping)

gen_results = {}
for metric in metrics:
    X = sm.add_constant(df['userGenderMapped'])  # independent
    y = df[metric]
    model = sm.OLS(y, X).fit(); gen_results[metric] = model.params #train n store result
for metric, result in gen_results.items(): print(f"Linear Regression Results for {metric} vs Gender:"); print(result); print("\n" + "-"*80 + "\n")

# plot lin reg

fig, axes = plt.subplots(1, 4, figsize=(18, 6))

# colours for the bars
color_age = 'lightblue'; color_arts = 'lightgreen'; color_gender = 'salmon'

# plot for each metric
for i, metric in enumerate(metrics):
    ax = axes[i]

    results = {'Age': age_results[metric].get('userAge', 0), 'Arts Course': art_results[metric].get('visualArtsCourse', 0), 'Gender': gen_results[metric].get('userGenderMapped', 0)} #single list for plot
    ax.bar(results.keys(), results.values(), color=[color_age, color_arts, color_gender])

    ax.set_title(f'{metric} vs Predictors'); ax.set_ylabel('Coefficient Value'); ax.set_xlabel('Predictor')

plt.tight_layout(); plt.show()

# #gender plot

# gender_groups = dfNorm.groupby('userGender')[['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']].mean()
# fig, axes = plt.subplots(1, 4, figsize=(18, 4))
# metrics = ['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch'] #col names

# for ax, metric in zip(axes, metrics): #for each metric
#     gender_groups[metric].plot(kind='bar', ax=ax, color=['skyblue', 'salmon', 'lightgreen'])
#     ax.set_title(metric)
#     ax.set_ylabel('Average Score Minus 50%')
#     ax.set_xlabel('Gender')
#     ax.set_xticklabels(['M', 'X', 'F'], rotation=0)

# plt.tight_layout(); plt.show()






# #arts plot


# arts_groups = dfNorm.groupby('visualArtsCourse')[['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']].mean()
# fig, axes = plt.subplots(1, 4, figsize=(18, 4))
# metrics = ['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch'] #col names

# for ax, metric in zip(axes, metrics): ##for each metric
#     arts_groups[metric].plot(kind='bar', ax=ax, color=['skyblue', 'salmon'])
#     ax.set_title(metric)
#     ax.set_ylabel('Average Score Minus 50%')
#     ax.set_xlabel('Visual Arts Course')
#     ax.set_xticklabels(['No Course', 'Course'], rotation=0)

# plt.tight_layout(); plt.show()








# #age plot

# fig, axes = plt.subplots(1, 4, figsize=(18, 6))
# metrics = ['BestColorMatch', 'BestContrastMatch', 'BestShapeMatch', 'BestOverallMatch']

# for ax, metric in zip(axes, metrics):
#     ax.scatter(df['userAge'], df[metric], color='blue', alpha=0.7)
#     ax.set_title(f'{metric} vs Age')
#     ax.set_xlabel('Age')
#     ax.set_ylabel('Score')
    
# plt.suptitle(''); plt.tight_layout(); plt.show()