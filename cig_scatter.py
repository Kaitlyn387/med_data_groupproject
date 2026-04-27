import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# This is specifically for the scatter plots I made to look at CIGPDAY vs HEARTRTE and SYSBP

# Read in Data
df = pd.read_csv("./Data/FraminghamDataset.csv")

df_scatter = df.copy(deep=True)
# Cleaning Up Missing Values (if you want to leave the NaNs, just remove/comment this part)
df_cigpday = df[df['CURSMOKE'] == 1] # df with only current smokers
cig_mean = df_cigpday['CIGPDAY'].mean() # finding mean cigarettes per day of only current smokers (so non-smoker 0 doesn't throw it off)
df_scatter['CIGPDAY'] = df_scatter['CIGPDAY'].fillna(cig_mean) # filling calced cigpday avg in for all missing (since missing is only for smokers)
df_scatter['HEARTRTE'] = df_scatter['HEARTRTE'].fillna(df_scatter['HEARTRTE'].mean()) # filling na with mean heart rate
print(df_scatter.isna().sum()) # Checking my work

# CPD and Heartrate Scatter (the less useful one)
plt.figure(figsize=(8,5))
plt.scatter(df_scatter['CIGPDAY'], df_scatter['HEARTRTE'], alpha = 0.25)
plt.title("Cigarettes Per Day vs Heart Rate")
plt.xlabel("Cigarettes Per Day")
plt.ylabel("Heart Rate")
plt.tight_layout() # Saving the image (you can remove/comment this if you don't want it)
plt.savefig("BPM_vs_CPD_scatter.png", dpi = 400)
plt.show()

# CPD and Systolic BP Scatter (the more useful one)
plt.figure(figsize=(8,5))
plt.scatter(df_scatter['CIGPDAY'], df_scatter['SYSBP'], alpha = 0.25)
plt.title("Cigarettes Per Day vs Systolic Blood Pressure")
plt.xlabel("Cigarettes Per Day")
plt.ylabel("Systolic Blood Pressure (mmHg)")
plt.tight_layout()
plt.savefig("SYSBP_vs_CPD_scatter.png", dpi = 400) # Saving the image (you can remove/comment this if you don't want it)
plt.show()