import pandas as pd

# Load your CSV file
df = pd.read_csv("Fish_Data.csv")

# Display the first column
print(df.iloc[:, 0])  # This prints the entire first column
