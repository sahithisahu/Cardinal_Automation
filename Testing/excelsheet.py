import pandas as pd
import os
import openpyxl

file_path1 = r"C:\Users\A. Sahithi\Downloads\ASP_Q3_CMS.xlsx"
file_path2 = r"C:\Users\A. Sahithi\Downloads\ASP_Q3_QLIK.xlsx"

ex1 = pd.read_excel(file_path1)
ex2 = pd.read_excel(file_path2)


ex1 = ex1[['hcpcs_code', 'payment_limit']]
ex2 = ex2[['Procedure Code', 'ASP+6.0% per BU']]
print(ex1.duplicated().sum())
print(ex2.duplicated().sum())

ex2.rename(columns={'Procedure Code': 'hcpcs_code'}, inplace=True)

ex1['hcpcs_code'] = ex1['hcpcs_code'].str.strip()
ex2['hcpcs_code'] = ex2['hcpcs_code'].str.strip()


merged = pd.merge(ex1, ex2, on='hcpcs_code', how='inner')

merged.drop_duplicates(subset=['hcpcs_code'], keep='first', inplace=True)

# nan_rows = merged[merged['hcpcs_code'].isna() | merged['ASP+6.0% per BU'].isna()]
# if not nan_rows.empty:
#     print("Rows with NaN values:")
#     print(nan_rows)

num_columns = merged.shape[1]
num_rows = merged.shape[0]
print(f"Number of columns in the DataFrame: {num_columns}")
print(f"Number of rows in the DataFrame: {num_rows}")

distinct_count = merged['hcpcs_code'].nunique()
print(f"Number of distinct values in 'Column1': {distinct_count}")

for index, row in merged.iloc[1:].iterrows():
    print(
        f"hcpcs_code: {row['hcpcs_code']}, payment_limit: {row['payment_limit']}, ASP+6.0% per BU: {row[
            'ASP+6.0% per BU']}")

