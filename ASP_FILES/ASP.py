import pandas as pd
import os
import sys


def ASP_Qlik():
    directory = r"C:\Users\A. Sahithi\Downloads"
    extension = ".xlsx"
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    full_paths = [os.path.join(directory, f) for f in files]
    latest_file = max(full_paths, key=os.path.getmtime)
    df = pd.read_excel(latest_file)
    print(df)
    return df
