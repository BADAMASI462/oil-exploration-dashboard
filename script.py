import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate simulated data
data = {
    "Field": ["Field A", "Field B", "Field C", "Field D", "Field E"],
    "Exploration Costs ($M)": [50, 80, 60, 70, 90],
    "Barrels Produced (Million)": [2.5, 3.2, 2.8, 3.0, 3.5],
    "Success Rate (%)": [50, 70, 65, 60, 75]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV
df.to_csv("mock_oil_exploration_data.csv", index=False)

# Visualization 1: Bar chart of success rates
plt.figure(figsize=(8, 6))
sns.barplot(x="Field", y="Success Rate (%)", data=df, palette="viridis", hue="Field", dodge=False, legend=False)
plt.title("Success Rates by Field")
plt.ylabel("Success Rate (%)")
plt.xlabel("Field")
plt.legend([], [], frameon=False)
plt.show()

# Visualization 2: Scatter plot of costs vs. barrels produced
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Exploration Costs ($M)", y="Barrels Produced (Million)", data=df, s=100, color="b")
plt.title("Exploration Costs vs. Barrels Produced")
plt.ylabel("Barrels Produced (Million)")
plt.xlabel("Exploration Costs ($M)")
plt.show()

# Visualization 3: Heatmap of correlations between numeric columns
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=["float64", "int64"])  # Select only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
