import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# This is the Prevalence of Cardiac Conditions by Current Smoking Status Bar Graph (specifically the normalized one)

df = pd.read_csv("./Data/FraminghamDataset.csv")

# Vis 5: Barplot (Frequency of Conditions Grouped by CURSMOKE)
print("\n\n=====Cluster Bar Plot Cleaning=====\n")
# Getting subset of total df to simplify scope
df_bar = df[["RANDID", "CURSMOKE", "PREVCHD", "PREVAP", "PREVMI", "PREVSTRK", "PREVHYP"]]
df_bar['CURSMOKE'] = df_bar['CURSMOKE'].replace(0, "Non-Smoker")
df_bar['CURSMOKE'] = df_bar['CURSMOKE'].replace(1, "Smoker")# Checking my work
print(df_bar.info())
# Reshaping the data to a long format (this will make grouping by prevalence of condition easier)
df_bar_melt = pd.melt(df_bar, id_vars= ['RANDID', 'CURSMOKE'], value_vars=["PREVCHD", "PREVAP", "PREVMI", "PREVSTRK", "PREVHYP"],
                      var_name= "CONDITION", value_name = "PREVALENCE")
# Checking my work
print("\n\n=====Pre-Melt=====\n")
print(df_bar.head())
print("\n\n=====Post-Melt=====\n")
print(df_bar_melt.head())

#df_bar_melt.to_csv("./Data/MeltedBar.csv")
#Finalizing Groupings
df_bar_group = df_bar_melt.groupby(["CURSMOKE", "CONDITION"])["PREVALENCE"].sum()
print(df_bar_group)
df_bar_group = df_bar_group.reset_index()
print(df_bar_group)

# Creating New table of frequency to normalize data
print("\n\n=====Freq Table for Normalization=====\n")
df_bar_freq = df_bar_melt.groupby(["CURSMOKE", "CONDITION"])["PREVALENCE"].count()
print(df_bar_freq)
df_bar_freq = df_bar_freq.reset_index()
print(df_bar_freq)

# Normalizing Data
df_bar_norm = df_bar_group.copy(deep=True)
df_bar_norm['PREVALENCE'] = df_bar_group["PREVALENCE"] / df_bar_freq["PREVALENCE"] 
print("\n\n=====Normalized Table=====\n")
print(df_bar_norm)

# Creating the barplot in seaborn
bar = sns.catplot(
    data=df_bar_norm, kind = "bar",
    x="CONDITION", y="PREVALENCE", hue="CURSMOKE",
)
plt.title("Prevalence of Heart Conditions Based on Current Smoking Status")
plt.xlabel("Condition")
plt.ylabel("Percent with Condition Prevalent")
plt.tight_layout()
plt.savefig("Prev_heart_cond_by_smoke.png", dpi = 400) #saving the picture
plt.show()