# Daily Expense Tracker – Advanced Data Cleaning Project

This project analyzes a real-world messy expense dataset generated using Python.
The dataset contains inconsistent date formats, spelling errors, duplicate rows,
negative and zero expenses, and missing values.

The goal is to clean the data, normalize categories, perform financial analysis,
and extract behavioral insights using Python.

## Files in this Project

-   messy_expense_dataset.csv : Raw generated dataset
-   data_generator.py : Script used to generate messy dataset
-   expense_tracker.ipynb : Data cleaning, analysis and visualization notebook
-   insights.txt : Personal finance insights & saving strategies
-   report.txt : Data quality and analysis summary
-   charts/ : All generated charts

## Tools Used

-   Python
-   pandas
-   matplotlib
-   numpy

## Data Cleaning Performed

-   Removed duplicate rows
-   Converted inconsistent date formats into datetime
-   Fixed spelling mistakes in Category
-   Normalized Payment_Mode values
-   Removed rows with missing categories
-   Removed zero and negative expense values

## Feature Engineering

-   Extracted month name from Date
-   Extracted day of week from Date

## Analysis Performed

-   Total spending calculation
-   Top 5 spending categories
-   Most expensive month
-   Most expensive day of week

## Visualizations

-   Pie Chart – Top spending categories
-   Line Chart – Daily spending trend
-   Bar Chart – Spending by weekday
