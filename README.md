# Student Performance Analysis

## About the Project

I built this project to practice data cleaning and analysis using Python. The dataset contains student names, genders, and grades in Mathematics, Python, and Statistics.

The main goal was to clean the data, analyze student performance, and present the results through charts.

## What I Did

- Checked the dataset for missing values and duplicates.
- Cleaned student names and standardized their format.
- Replaced invalid grades with missing values and filled them using the median.
- Calculated each student's average grade.
- Classified students as Pass or Fail.
- Compared performance across subjects and gender groups.
- Analyzed correlations between subjects.
- Created charts to visualize the results.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib

## Project Files

- `analysis.py`: Contains the data cleaning, analysis, and visualization code.
- `data/students.csv`: Original dataset.
- `data/student_results.csv`: Cleaned dataset with calculated results.
- `chart/`: Contains the generated charts.

## Results

After running the analysis, I found that:

- Python had the highest average grade.
- Mathematics had the lowest average grade.
- Nour achieved the highest average with 18/20.
- The overall pass rate was 91.67%.

## Chart

The project generates charts showing:

- Average grades by subject.
- Pass and Fail distribution.
- Distribution of student averages.
- Correlation between subjects.

## Running the Project

Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

Run the analysis:

```bash
python analysis.py
```

The cleaned dataset and charts will be generated automatically.

## Note

The dataset is synthetic and was created for learning and portfolio demonstration purposes.