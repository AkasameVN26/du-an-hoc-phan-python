import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
# Using a raw string to avoid issues with backslashes in the path
file_path = r'D:\CODE\CMC\du-an-hoc-phan-python\thpt-dataset-cleaned\thpt2024.csv'
df = pd.read_csv(file_path)

# Select subject columns for correlation matrix
subject_cols = ['toan', 'ngu_van', 'vat_ly', 'hoa_hoc', 'sinh_hoc', 'lich_su', 'dia_ly', 'gdcd', 'ngoai_ngu']
df_subjects = df[subject_cols]

# Calculate the correlation matrix
corr_matrix = df_subjects.corr()

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Draw the heatmap
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0)

# Add title
plt.title('Ma trận tương quan giữa các môn học - THPT 2024', fontsize=16)

# Find the pair with the highest correlation
corr_unstacked = corr_matrix.unstack()
highest_corr = corr_unstacked[corr_unstacked != 1].sort_values(ascending=False)

print("Cặp môn có tương quan cao nhất:")
print(highest_corr.head(1))

# Show the plot directly
print("\nCửa sổ biểu đồ sẽ được hiển thị. Hãy đóng nó để tiếp tục.")
plt.show()
