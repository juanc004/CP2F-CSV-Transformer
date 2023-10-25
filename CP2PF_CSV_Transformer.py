# Import required libraries
import pandas as pd

# Read the CSV file into a DataFrame
csv_path = ''  # Replace with your CSV file path
cp2f_df = pd.read_csv(csv_path)

# Display the column names for debugging
print("Columns in the DataFrame:", cp2f_df.columns)

required_fields = [
    'Date', 'About', 'Candidate', 'Iteration', 'Top 3 or Bottom 3', 'Trainability',
    'Stress Tolerance', 'Drive', 'Communication',
    'Problem Solving', 'Teamwork', 'Physical Fitness', 'Comment'
]

# Filter the DataFrame to only include the required fields
filtered_cp2f_df = cp2f_df[required_fields]

# Display the first few rows of the filtered DataFrame
print(filtered_cp2f_df.head())

# Rename columns according to the mapping rules
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

# Perform the transformation
gpsddb_df = filtered_cp2f_df.rename(columns=transformed_fields)

# Reorder columns to match the required format
gpsddb_columns_order = [
    'Reviewee', 'Date', 'Iteration', 'Trainability', 'Drive', 'Stress Tolerance',
    'Communication', 'Problem Solving', 'Teamwork', 'Physical Fitness', 'T3B3', 'Comment', 'Reviewer',
]

gpsddb_df = gpsddb_df[gpsddb_columns_order]

# Display the first few rows of the transformed DataFrame
print(gpsddb_df.head())

# Specify the output path for the transformed CSV file
output_csv_path = '/summarized_PF_1.csv'  # Replace with your desired output path

# Save the DataFrame to a new CSV file
gpsddb_df.to_csv(output_csv_path, index=False)

# Confirm that the CSV file has been saved
print(f"Transformed DataFrame has been saved to {output_csv_path}")