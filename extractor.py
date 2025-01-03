import pandas as pd
import re


def extract_question_cols(input_file, output_file, pattern):
    # read the original CSV file
    df = pd.read_csv(input_file, low_memory=False)

    cols = df.columns.tolist()

    result = []
    count = 0
    for col in cols:
        if re.search(pattern, col):
            result.append(col)
            count += 1

    # write the list to text file
    print(result)
    print(count)


# creating inputs
pattern = '^[A-Za-z]{1,}\\d[A-Za-z]{1,}\\.[A-Za-z0-9]{1,}$'
extract_question_cols('input.csv', 'col_out.txt', pattern)
