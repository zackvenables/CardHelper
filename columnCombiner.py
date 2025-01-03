import pandas as pd


def combine_columns(file, columns, out_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Select the specified columns
    selected_columns = df[columns]

    # Combine the selected columns into a single column
    combined_column = selected_columns.apply(lambda col: col, axis=1)

    # Remove the columns used in the combination from the original DataFrame
    df.drop(columns=columns, inplace=True)

    # Add the combined column to the DataFrame
    df['Questions'] = combined_column

    # Save the modified DataFrame to a new CSV file
    df.to_csv(out_file, index=False)

    print(f"Combined columns {columns} and saved to {out_file}")


# Example usage
csv_file = 'input.csv'
output_file = 'combined_output.csv'
columns_to_combine = ['Column2', 'Column3']

combine_columns(csv_file, columns_to_combine, output_file)
