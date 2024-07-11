import pandas as pd
import os
import openpyxl

file_path1 = r"C:\Users\A. Sahithi\Downloads\ASP_Q3_CMS.xlsx"
file_path2 = r"C:\Users\A. Sahithi\Downloads\ASP_Q3_QLIK.xlsx"
output_file_path = r"C:\Users\A. Sahithi\Downloads\Not_Matching_Results.xlsx"

ex1 = pd.read_excel(file_path1)
ex2 = pd.read_excel(file_path2)

ex1 = ex1[['hcpcs_code', 'payment_limit']]
ex2 = ex2[['Procedure Code', 'ASP+6.0% per BU']]

ex2.rename(columns={'Procedure Code': 'hcpcs_code'}, inplace=True)

ex1['hcpcs_code'] = ex1['hcpcs_code'].str.strip()
ex2['hcpcs_code'] = ex2['hcpcs_code'].str.strip()

merged = pd.merge(ex1, ex2, on='hcpcs_code', how='inner')

merged.drop_duplicates(subset=['hcpcs_code'], keep='first', inplace=True)

merged['Equal'] = merged['payment_limit'] == merged['ASP+6.0% per BU']
merged['Equal'] = merged['Equal'].replace({True: 'matching', False: 'not matching'})

match_counts = merged['Equal'].value_counts()

not_matching = merged[merged['Equal'] == 'not matching']
# not_matching = not_matching.iloc[1:]

not_matching.to_excel(output_file_path, index=False)
# merged.to_excel(output_file_path, index=False)

print(f"Not matching results have been saved to {output_file_path}")


num_columns = not_matching.shape[1]
num_rows = not_matching.shape[0]
print(f"Number of columns in the DataFrame: {num_columns}")
print(f"Number of rows in the DataFrame: {num_rows}")

# num_columns = merged.shape[1]
# num_rows = merged.shape[0]
# print(f"Number of columns in the DataFrame: {num_columns}")
# print(f"Number of rows in the DataFrame: {num_rows}")

distinct_count = merged['hcpcs_code'].nunique()
print(f"Number of distinct values in 'Column1': {distinct_count}")

print(f"Matching count: {match_counts.get('matching', 0)}")
print(f"Not matching count: {match_counts.get('not matching', 0)}")

# print(f"Not matching count: {not_matching.shape[0]}")

for index, row in not_matching.iterrows():
    print(
        f"hcpcs_code: {row['hcpcs_code']}, payment_limit: {row['payment_limit']}, ASP+6.0% per BU: {row[
            'ASP+6.0% per BU']}, Equal: {row['Equal']}")
