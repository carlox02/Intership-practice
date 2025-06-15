import pandas as pd

# Load the dataset
df = pd.read_csv("Fish_Data.csv")

# Clean temp columns (remove °F and convert to float)
df["Water Temp (F)"] = df["Water Temp (F)"].str.replace("°F", "").astype(float)
df["Outside Temp (F)"] = df["Outside Temp (F)"].str.replace("°F", "").astype(float)

# Convert Date to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Fill missing values
df["Lure Used"] = df["Lure Used"].fillna("Unknown")
df["Depth"] = df["Depth"].fillna("Unknown")
df["Weight (lb)"] = df["Weight (lb)"].fillna(df["Weight (lb)"].median())
df["Length (in)"] = df["Length (in)"].fillna(df["Length (in)"].median())
df["Water Temp (F)"] = df["Water Temp (F)"].fillna(df["Water Temp (F)"].mean())
df["Outside Temp (F)"] = df["Outside Temp (F)"].fillna(df["Outside Temp (F)"].mean())
df["Time"] = df["Time"].fillna("8:00 AM")
df["Moon Phase"] = df["Moon Phase"].fillna("Unknown")
df["Notes"] = df["Notes"].fillna("No additional info")

# Confirm no missing values
print("Missing values after fill:")
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv("cleaned_Fish_Data.csv", index=False)
