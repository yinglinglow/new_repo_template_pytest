"""
to run:
C:\ProgramData\Anaconda3\python.exe main.py

"""
import sys
import pandas as pd

def test_function(df):
    col_names = df.columns
    return col_names

if __name__ == '__main__':
    # for debug
    # filepath = 'C:\\blahblah\\filename.csv'
    # sys.stdout = open("C:/check/stdout.txt", "w")
    # sys.stderr = open("C:/check/stderr.txt", "w")
    # end debug
    
    # read in variables
    filepath = sys.argv[1]
    
    # run function
    df = pd.read_csv(filepath)
    col_names = test_function(df)

    print(col_names)
