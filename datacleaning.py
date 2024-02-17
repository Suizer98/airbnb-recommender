import pandas as pd

# Read CSV file with Latin-1 encoding
df = pd.read_csv("mocksurveydata.csv", encoding="latin1")

# Remove completely blank rows
df = df.dropna(how="all")
df = df.dropna()

# Save modified data back to the same CSV file
df.to_csv("mocksurveydata.csv", index=False, encoding="latin1")
