import pandas as pd


def transform_csv(input_file, output_file, columns_to):
    # Read the original CSV file
    df = pd.read_csv(input_file, low_memory=False)
    #get unique names
    wrestlers = df['name'].unique()
    types = []
    dup_wrestlers = []
    for wrestler in wrestlers:

        values = df.loc[df['name'] == wrestler, 'type']

        modval = modify_columns(values, wrestler)
        types.append(modval)

    data = {'name': wrestlers, 'type': types}


    new_df = pd.DataFrame(data);
    new_df.to_csv('outputA.csv', index=False)


def modify_columns(strings, wrestler):
    modified_strings = []
    wrestlers = []
    base_types = ['Base', 'Base Amethyst', 'Base Emerald', 'Base Gold', 'Base Platinum', 'Base Ruby']

    for s in strings:
        # Split the string into words
        words = s.split()

        first_two_words = words[0]
        # Check if there are at least two words
        if len(words) >= 2 and s not in base_types:
            # Compare the first two words to the others
            first_two_words = words[0] +' '+ words[1]


        if first_two_words not in modified_strings:
            modified_strings.append(first_two_words)


    return ", ".join(modified_strings)

# creating inputs
columns_to_rearrange = ['name', 'type']
transform_csv('wrestlers.csv', 'output.csv', columns_to_rearrange)
