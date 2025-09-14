import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Score": [85, 92, 78, 90]}
df = pd.DataFrame(data)
average = df["Score"].mean()

print("Scores dataset:")
print(df)
print(f"\nAverage score: {average:.2f}")
