import pandas as pd

# File paths
file_path1 = r"C:/Users/A. Sahithi/Downloads/ASP_Q3_CMS.xlsx"
file_path2 = r"C:/Users/A. Sahithi/Downloads/ASP_Q3_QLIK.xlsx"

ex1 = pd.read_excel(file_path1)
ex2 = pd.read_excel(file_path2)

ex1 = ex1[['hcpcs_code', 'payment_limit']]
ex2 = ex2[['Procedure Code', 'ASP+6.0% per BU']]
print(ex1.duplicated().sum())
print(ex2.duplicated().sum())


ex2.rename(columns={'Procedure Code': 'hcpcs_code'}, inplace=True)

ex1['hcpcs_code'] = ex1['hcpcs_code'].astype(str).str.strip()
ex2['hcpcs_code'] = ex2['hcpcs_code'].astype(str).str.strip()

merged = pd.merge(ex1, ex2, on='hcpcs_code', how='inner')
merged.drop_duplicates(subset=['hcpcs_code'], keep='first', inplace=True)

nan_rows_ex1 = ex1[ex1['hcpcs_code'].isna() | ex1['payment_limit'].isna()]
nan_rows_ex2 = ex2[ex2['hcpcs_code'].isna() | ex2['ASP+6.0% per BU'].isna()]
if not nan_rows_ex1.empty or not nan_rows_ex2.empty:
    print("NaN values found in ex1:")
    print(nan_rows_ex1)
    print("NaN values found in ex2:")
    print(nan_rows_ex2)

num_rows = merged.shape[0]
distinct_count = merged['hcpcs_code'].nunique()
print(f"Number of rows in the DataFrame: {num_rows}")
print(f"Number of distinct values in 'hcpcs_code': {distinct_count}")

for index, row in merged.iterrows():
    print(
        f"hcpcs_code: {row['hcpcs_code']}, payment_limit: {row['payment_limit']}, ASP+6.0% per BU: {row[
            'ASP+6.0% per BU']}")
