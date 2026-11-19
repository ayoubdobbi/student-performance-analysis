import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")

# Initial inspection
print("Initial shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nData types:\n", df.dtypes)
print("\nUnique names:\n", df["student_name"].unique())
# =========================
# Data Cleaning
# =========================

# 1. Clean student names
df["student_name"] = df["student_name"].str.strip().str.title()

# 2.Remove duplicates after normalizing names
df = df.drop_duplicates()

# 3. Validate grades (grades must be between 0 and 20)
subjects = ["math", "python", "statistics"]

for col in subjects:
    df.loc[~df[col].between(0, 20), col] = np.nan

# 4. Handle missing values using the median
for col in subjects:
    df[col] = df[col].fillna(df[col].median())

# 5. Display cleaned data
print("\nCleaned Dataset:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicates after cleaning:")
print(df.duplicated().sum())

print("\nFinal Shape:", df.shape)
# =========================
# Feature Engineering
# =========================

# Calculate student average
df["average"] = df[subjects].mean(axis=1)

# Determine pass or fail
df["result"] = np.where(df["average"] >= 10, "Pass", "Fail")

# Classify performance
conditions = [
    df["average"] < 10,
    df["average"] < 14
]

choices = ["Needs Improvement", "Average"]

df["performance"] = np.select(
    conditions,
    choices,
    default="Excellent"
)

# Display results
print("\nFinal Dataset with New Features:")
print(df)
# =========================
# Data Analysis
# =========================

# 1. Subject averages
print("\nSubject Averages:")
print(df[subjects].mean())

# 2. Highest average student
print("\nTop Student:")
print(df.loc[df["average"].idxmax()])

# 3. Lowest average student
print("\nLowest Student:")
print(df.loc[df["average"].idxmin()])

# 4. Pass and Fail counts
print("\nPass/Fail Counts:")
print(df["result"].value_counts())

# 5. Pass percentage
pass_percentage = (df["result"].eq("Pass").mean()) * 100

print(f"\nPass Percentage: {pass_percentage:.2f}%")

# 6. Overall average
print("\nOverall Average:")
print(df["average"].mean())

# =========================
# Performance by Gender
# =========================

gender_analysis = df.groupby("gender").agg(
    student_count=("student_name", "count"),
    average_grade=("average", "mean"),
    pass_count=("result", lambda x: (x == "Pass").sum())
)

gender_analysis["pass_rate"] = (
    gender_analysis["pass_count"] / gender_analysis["student_count"] * 100
)

print("\nPerformance by Gender:")
print(gender_analysis.round(2))
# =========================
# Correlation Analysis
# =========================

correlation = df[subjects].corr()

print("\nCorrelation Matrix:")
print(correlation.round(2))
# =========================
# Data Visualization
# =========================

# 1. Average grades by subject
# 1. Average grades by subject

subject_avg = df[subjects].mean().sort_values()

plt.figure(figsize=(9, 5))

bars = plt.bar(
    subject_avg.index,
    subject_avg.values
)

plt.title("Average Grade by Subject", fontsize=14)
plt.xlabel("Subject")
plt.ylabel("Average Grade")
plt.ylim(0, 20)
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        f"{bar.get_height():.2f}",
        ha="center"
    )

plt.tight_layout()
plt.savefig("chart/subject_averages.png", dpi=300)
plt.close()

# 2. Pass vs Fail
result_counts = df["result"].value_counts()

plt.figure(figsize=(6, 6))
result_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.ylabel("")
plt.tight_layout()
plt.savefig("chart/pass_fail.png")
plt.close()


# 3. Students' average distribution

plt.figure(figsize=(9, 5))

plt.hist(
    df["average"],
    bins=6,
    edgecolor="black"
)

plt.axvline(
    df["average"].mean(),
    linestyle="dashed",
    linewidth=2,
    label=f'Mean: {df["average"].mean():.2f}'
)

plt.title("Distribution of Student Averages", fontsize=14)
plt.xlabel("Average Grade")
plt.ylabel("Number of Students")
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("chart/average_distribution.png", dpi=300)
plt.close()
# 4. Correlation Heatmap

correlation = df[subjects].corr()

plt.figure(figsize=(7, 5))
plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(subjects)), subjects)
plt.yticks(range(len(subjects)), subjects)

for i in range(len(subjects)):
    for j in range(len(subjects)):
        plt.text(j, i, f"{correlation.iloc[i, j]:.2f}",
                 ha="center", va="center")

plt.title("Correlation Between Subjects")
plt.tight_layout()
plt.savefig("chart/correlation_heatmap.png")
plt.close() 

print("\nCharts saved successfully!")

# =========================
# Export Cleaned Data
# =========================

df.to_csv("data/student_results.csv", index=False)

print("\nCleaned dataset exported successfully!")
# =========================
# Key Insights
# =========================

subject_avg = df[subjects].mean()

weakest_subject = subject_avg.idxmin()
best_subject = subject_avg.idxmax()

top_student = df.loc[df["average"].idxmax(), "student_name"]
top_average = df["average"].max()

pass_rate = (df["result"] == "Pass").mean() * 100

print("\n========== KEY INSIGHTS ==========")

print(f"Best performing subject: {best_subject}")
print(f"Lowest performing subject: {weakest_subject}")
print(f"Top student: {top_student} ({top_average:.2f}/20)")
print(f"Overall pass rate: {pass_rate:.2f}%")

print("=================================")