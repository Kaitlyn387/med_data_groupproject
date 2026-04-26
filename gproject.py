import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Step 1: Read in data and look at initial information
df = pd.read_csv("./Data/FraminghamDataset.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isna().sum())

# Step 2: Creating Dataframes for each visualization
# Vis 1: Scatter plot (AGE, SYSBP, DYSBP, GLUCOSE, BMI)
print("\n\n=====Scatter Cleaning=====\n")
df_scat = df.copy(deep=True)

# Dealing with missing values
# BMI: Dropping missing
df_scat = df_scat.dropna(subset = ['BMI'])
# Glucose: Filling with mean value
print(df_scat['GLUCOSE'].head(11))
df_scat['GLUCOSE'] = df_scat['GLUCOSE'].fillna(df_scat['GLUCOSE'].mean())
print(df_scat['GLUCOSE'].head(11))
print(df_scat.isna().sum()) #Checking my work
# At this point, this data should be ready for graphing!

#Vis 2: Density Plot Smoke (AGE between CURSMOKE = 0 and CURSMOKE = 1)
# There's no missing data in these variables, but I'm going to go through CURSMOKE and replace 0 with 'No' and 1 with 'Yes' for easier labels
print("\n\n=====Density Smoke Cleaning=====\n")
df_dense_smoke = df.copy(deep=True)
df_dense_smoke['CURSMOKE'] = df_dense_smoke['CURSMOKE'].replace(0, 'Non-Smoker')
df_dense_smoke['CURSMOKE'] = df_dense_smoke['CURSMOKE'].replace(1, 'Smoker')
print(df_dense_smoke.head(10)) #Checking my work
print(df_dense_smoke.info())

# Now comes the grouping, and I'll stop with the following line
#(hint: I found a way to do the graph by adding stuff to the end of this line. But I'll let you find your own way.)
df_dense_smoke.groupby('CURSMOKE')['AGE']
# There's also a way to make a seaborn plot that actually doesn't need the above line. Basically, if you need help, I know how in plt and sns.



# Vis 3: Boxplot (HEARTRTE separated by AGE)
# We need to separate the two age groups: above and below the NIH cutoff for being an older adult (AKA < 65 and >= 65)
print("\n\n=====Boxplot Cleaning=====\n")
df_box = df.copy(deep=True)
cutoff = 65
# Creating a new column to indicate if the age is above or below the cutoff
df_box['AGE_GROUP'] = np.where(df_box['AGE'] >= cutoff, '65 and Older', 'Below 65')
# I'm leaving HEARTRTE as NaN as instructed
# From here, the .boxplot() function can actually do the rest of the grouping work as long as you put in the right parameters.
# I also know how to do this in seaborn from here, so I can help either way if you want.


# Vis 4: Density Plot BP (TOTCHOL, SYSBP, DIABP)
df_dense_chol = df.copy(deep=True)
# I've been told to leave the NaN TOTCHOL values, so there's no missing data to handle here. Which means there's actually no data to clean! From here you just make the plot.


#Vis 5: Barplot (Frequency of Conditions)
# I'm going to do this one later since it's my graph and I don't want to keep you two from working any longer than I have to
# That's all for data cleaning. If you have any questions or I did something wrong, let me know! Happy coding!


#This is just a correlation plot I was messing with. You can look at it or get rid of it, I won't be offended.
'''
#Getting subset of variables that I want to examine
df_small = df.iloc[:, 1:31]
print(df_small.head())
print(df_small.info())
print(df_small.describe())
print(df_small.isna().sum())

# Making correlation matrix
corr_matrix = df_small.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, cmap='coolwarm')
plt.title("Framingham Correlation Matrix Heatmap")
plt.show()
'''