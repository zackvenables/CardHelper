import pandas as pd
from datetime import datetime


def transform_csv(input_file, output_file, columns_to):
    # Read the original CSV file
    old_df = pd.read_csv(input_file, low_memory=False)
    print('File Read.' + str(datetime.now()))
    
    # Melt the DataFrame to transform from wide to long format
    id_vars = [col for col in old_df.columns if col not in columns_to]
    new_df = pd.melt(old_df, id_vars=id_vars, value_vars=columns_to, var_name='Question', value_name='Answer')
    print('File melted.' + str(datetime.now()))

    # Add 'Question' and 'Answer' columns
    new_df['Question'] = new_df['Question'].apply(lambda x: x)  # Assuming columns are named as 'Q_xxx'
    print('Questions added.' + str(datetime.now()))

    new_df = new_df[id_vars + ['Question'] + ['Answer']]  # Rearrange columns
    print('Columns rearranged.' + str(datetime.now()))

    # Save the transformed DataFrame to a new CSV file
    new_df.to_csv(output_file, index=False)
    print('File saved.' + str(datetime.now()))


# creating inputs
columns_to_rearrange = ['name', 'type']
transform_csv('wrestlers.csv', 'output.csv', columns_to_rearrange)
