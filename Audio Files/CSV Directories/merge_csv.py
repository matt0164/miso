import pandas as pd

#load individual sound data
df_sounds = pd.read_csv("audio_analysis.csv")

#load annoyance level data
df_annoyance = pd.read_csv("severity_heatmap.csv")

df_sounds["category"] = df_sounds["category"].astype(str)
df_annoyance["category"] = df_annoyance["category"].astype(str)

df_combined = df_sounds.merge(df_annoyance, on="category", how="left")
print(df_combined.head())

df_combined.to_csv("merged_data.csv", index=False)
