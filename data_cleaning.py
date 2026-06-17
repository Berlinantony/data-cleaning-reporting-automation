import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = r"C:\Users\berli\Downloads\archive\train.csv"
df = pd.read_csv(file_path)

# -----------------------------
# Basic Dataset Information
# -----------------------------
print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# Missing Values Report
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna("Unknown")

# -----------------------------
# Remove Duplicates
# -----------------------------
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()
duplicates_after = df.duplicated().sum()

print(f"\nDuplicates Removed: {duplicates_before}")
print(f"Remaining Duplicates: {duplicates_after}")

# -----------------------------
# Standardize Text Columns
# -----------------------------
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip().str.title()

# -----------------------------
# Save Cleaned Data
# -----------------------------
df.to_excel("cleaned_data.xlsx", index=False)

print("\nCleaned data saved as cleaned_data.xlsx")

# -----------------------------
# Generate Automated Report
# -----------------------------
report = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values,
    "Data Type": df.dtypes.values
})

report.to_excel("data_report.xlsx", index=False)

print("Report saved as data_report.xlsx")

# -----------------------------
# Visualization
# -----------------------------
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

if len(numeric_cols) > 0:
    first_numeric = numeric_cols[0]

    plt.figure(figsize=(8, 5))
    df[first_numeric].hist(bins=20)
    plt.title(f"Distribution of {first_numeric}")
    plt.xlabel(first_numeric)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("report_chart.png")
    plt.show()

    print("Chart saved as report_chart.png")

print("\nAutomation completed successfully!")