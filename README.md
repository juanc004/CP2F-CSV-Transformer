
# CP2F-CSV-Transformer

## Overview

This Python script is designed to transform raw CSV data from CP2F evaluations into a more readable and standardized format. The script reads the input CSV, filters and renames fields, reorders columns, and then saves the transformed data into a new CSV file.

## Requirements

- Python 3.x
- Pandas library

You can install the required package using:
```bash
pip install pandas
```

## How to Run

1. Update the `csv_path` in the script with the path to your input CSV file.
2. Update the `output_csv_path` with the directory where you'd like to save the transformed CSV file.
3. Run the script.

## Features

- Reads raw CP2F data from a CSV file.
- Filters the DataFrame to only include specified fields.
- Renames columns to standardized names.
- Reorders columns to match a specific format.
- Saves the transformed DataFrame to a new CSV file.

## Code Walkthrough

### Import Required Libraries

```python
import pandas as pd
```

### Read CSV File into DataFrame

```python
csv_path = ''  # Replace with your CSV file path
cp2f_df = pd.read_csv(csv_path)
```

### Display Column Names

```python
print("Columns in the DataFrame:", cp2f_df.columns)
```

### Filter DataFrame

```python
required_fields = [
    'Date', 'About', 'Candidate', 'Iteration', 'Top 3 or Bottom 3', 'Trainability',
    'Stress Tolerance', 'Drive', 'Communication',
    'Problem Solving', 'Teamwork', 'Physical Fitness', 'Comment'
]
filtered_cp2f_df = cp2f_df[required_fields]
```

### Rename Columns

```python
transformed_fields = {
    'About': 'Reviewer',
    'Candidate': 'Reviewee',
    'Iteration': 'Iteration',
    'Top 3 or Bottom 3': 'T3B3',
    'Comment': 'Comment',
    'Trainability': 'Trainability',
    'Stress Tolerance': 'Stress Tolerance',
    'Drive': 'Drive',
    'Communication': 'Communication',
    'Problem Solving': 'Problem Solving',
    'Teamwork': 'Teamwork',
    'Physical Fitness': 'Physical Fitness'
}
gpsddb_df = filtered_cp2f_df.rename(columns=transformed_fields)
```

### Reorder Columns

```python
gpsddb_columns_order = [
    'Reviewee', 'Date', 'Iteration', 'Trainability', 'Drive', 'Stress Tolerance',
    'Communication', 'Problem Solving', 'Teamwork', 'Physical Fitness', 'T3B3', 'Comment', 'Reviewer',
]
gpsddb_df = gpsddb_df[gpsddb_columns_order]
```

### Save Transformed DataFrame

```python
output_csv_path = '/summarized_PF_1.csv'  # Replace with your desired output path
gpsddb_df.to_csv(output_csv_path, index=False)
```

### Confirmation Message

```python
print(f"Transformed DataFrame has been saved to {output_csv_path}")
```

## License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## Changelog

For all notable changes to this project, see `CHANGELOG.md`.
