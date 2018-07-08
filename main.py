"""
to run:
python main.py

"""

import pandas as pd

def sample_get_column_names(df):
    col_names = df.columns
    return col_names

if __name__ == '__main__':

    df = pd.read_csv('abc.csv')
    col_names = sample_get_column_names(df)

    print(col_names)