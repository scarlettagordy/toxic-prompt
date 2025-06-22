import pandas as pd

# Load the detoxify results
df = pd.read_csv("detoxify_results.csv")

# Show basic stats
print("\nSummary of Detoxify Scores:")
print(df.describe())

# Count how many are above toxicity thresholds
thresholds = [0.5, 0.7, 0.9]
for thresh in thresholds:
    count = (df["toxicity"] > thresh).sum()
    print(f"\nToxicity > {thresh}: {count} out of {len(df)}")

# Save summary to file
with open("toxicity_summary.txt", "w") as f:
    f.write(df.describe().to_string())
    f.write("\n")
    for thresh in thresholds:
        count = (df["toxicity"] > thresh).sum()
        f.write(f"Toxicity > {thresh}: {count} out of {len(df)}\n")

print("\nSummary saved to 'toxicity_summary.txt'")