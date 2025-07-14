import json
import pandas as pd
import matplotlib.pyplot as plt

# Load the JSON file
with open('categorized_ecu_links.json', 'r') as file:
    data = json.load(file)

# Extract category counts
category_counts = data["Category Counts"]

# Convert category counts to a pandas DataFrame
df = pd.DataFrame(list(category_counts.items()), columns=["Category", "Count"])

# Sort the DataFrame by count for better visualization
df = df.sort_values(by="Count", ascending=False)

"""The upper portion is code for analyzing data using pandas and the below portion is for visualizing data using matplotlib"""

# Display the DataFrame
print("Category Counts:")
print(df)

# Save the DataFrame to a CSV file for further analysis
df.to_csv("category_counts.csv", index=False)
print("\nCategory counts saved to 'category_counts.csv'.")

# Visualize the data
plt.figure(figsize=(12, 8))
plt.barh(df['Category'], df['Count'], color='skyblue')
plt.xlabel("Number of Links")
plt.ylabel("Categories")
plt.title("Number of Links per Category")
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.tight_layout()

# Save the plot
plt.savefig("category_counts.png")
print("Visualization saved as 'category_counts.png'.")

# Show the plot
plt.show()

"""The below code generates data in Pie Chart format"""


# Prepare data for pie chart
sizes = df["Count"].values  # Get the counts as an array
labels = df["Category"].values  # Get the categories as an array
total = sizes.sum()
percentages = [f"{(count / total) * 100:.1f}%" for count in sizes]

# Create the pie chart
colors = plt.cm.tab20.colors  # Use a colormap for diverse colors
plt.figure(figsize=(12, 8))
wedges, texts = plt.pie(
    sizes,
    labels=None,  # Remove labels from the pie itself
    startangle=140,
    colors=colors,
    textprops=dict(color="black", fontsize=10)
)

# Add legend with percentages outside the chart
legend_labels = [f"{label} - {perc}" for label, perc in zip(labels, percentages)]
plt.legend(
    wedges,
    legend_labels,
    title="Categories (with %)",
    loc="center left",
    bbox_to_anchor=(1, 0.5),  # Position the legend outside
    fontsize=12
)

# Ensure equal aspect ratio
plt.axis("equal")

# Set the title
plt.title("Distribution of Links Across ECU Categories", fontsize=14)

# Save the pie chart
plt.savefig("category_counts.png", bbox_inches="tight")
print("Visualization saved as 'category_counts.png'.")

# Show the pie chart
plt.show()

