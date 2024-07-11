import os
import pandas as pd
from robot.api import logger
from typing import Any


class ExcelKeywords:
    @property
    def _get_instance(self):
        return BuiltIn().get_library_instance('Selenium2Library')

    @property
    def _driver(self):
        return self._get_instance._current_browser()

    def ASP_value(self, directory: str) -> str:
        try:
            extension = ".xlsx"
            files = [f for f in os.listdir(directory) if f.endswith(extension)]
            if not files:
                logger.warn(f"No Excel files found in directory: {directory}")
                return None

            full_paths = [os.path.join(directory, f) for f in files]
            latest_file = max(full_paths, key=os.path.getmtime)

            file_path1 = os.path.join(directory, "ASP_Q3_CMS.xlsx")
            output_file_path = os.path.join(directory, "Not_Matching_Results.xlsx")


            ex1 = pd.read_excel(file_path1)
            ex2 = pd.read_excel(latest_file)

            ex1 = ex1[['hcpcs_code', 'payment_limit']]
            ex2 = ex2[['Procedure Code', 'ASP+6.0% per BU']]
            ex2.rename(columns={'Procedure Code': 'hcpcs_code'}, inplace=True)

            ex1['hcpcs_code'] = ex1['hcpcs_code'].str.strip()
            ex2['hcpcs_code'] = ex2['hcpcs_code'].str.strip()

            merged = pd.merge(ex1, ex2, on='hcpcs_code', how='inner')
            merged.drop_duplicates(subset=['hcpcs_code'], keep='first', inplace=True)

            merged['Equal'] = merged['payment_limit'] == merged['ASP+6.0% per BU']
            merged['Equal'] = merged['Equal'].replace({True: 'matching', False: 'not matching'})

            # match_counts = merged['Equal'].value_counts()
            not_matching = merged[merged['Equal'] == 'not matching']
            not_matching.to_excel(output_file_path, index=False)

            logger.info(f"Not matching results have been saved to {output_file_path}")
            logger.info(f"Number of columns in the DataFrame: {not_matching.shape[1]}")
            logger.info(f"Number of rows in the DataFrame: {not_matching.shape[0]}")
            logger.info(f"Number of distinct values in 'hcpcs_code': {merged['hcpcs_code'].nunique()}")
            logger.info(f"Matching count: {match_counts.get('matching', 0)}")
            logger.info(f"Not matching count: {match_counts.get('not matching', 0)}")

            for index, row in not_matching.iterrows():
                logger.info(
                    f"hcpcs_code: {row['hcpcs_code']}, payment_limit: {row['payment_limit']}, ASP+6.0% per BU: {row['ASP+6.0% per BU']}, Equal: {row['Equal']}"
                )

            return output_file_path

        except Exception as e:
            logger.error(f"An error occurred in ASP_value: {e}")
            return None

    def ASP_Qlik_final()-> pd.DataFrame:

        directory = r"C:\Users\A. Sahithi\Downloads"
        extension = ".xlsx"
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        if not files:
            logger.warn(f"No Excel files found in directory: {directory}")
            return None

        full_paths = [os.path.join(directory, f) for f in files]
        latest_file = max(full_paths, key=os.path.getmtime)
        df = pd.read_excel(latest_file)
        logger.info(f"Data from the latest file {latest_file}: \n{df}")
        return df


# BuiltIn().register_library_class(ExcelKeywords)
