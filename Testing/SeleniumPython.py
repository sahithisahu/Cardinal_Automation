from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import os
import logging


class SeleniumPython:

    @property
    def _get_instance(self):
        return BuiltIn().get_library_instance('Selenium2Library')

    @property
    def _driver(self):
        return self._get_instance._current_browser()

    # def get_patient_visit_count(self):
    #     file_path = r"C:\Users\A. Sahithi\Downloads\patientvisit.xlsx"
    #     df = pd.read_excel(file_path)
    #     print(df)
    #     patients23 = df["Patient_visit"].sum()
    #     print("Patient_visit", patients23)
    #     return patients23

    def get_patient_visit(self):
        directory = r"C:\Users\A. Sahithi\Downloads"
        extension = ".xlsx"
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        full_paths = [os.path.join(directory, f) for f in files]
        latest_file = max(full_paths, key=os.path.getmtime)
        df = pd.read_excel(latest_file)
        # print(df)
        df.rename(columns={' ': 'Value'}, inplace=True)
        print(df)
        patients23 = df["Value"].sum()
        print("Patient_visit", patients23)
        return patients23

    def get_payment_details(self):
        directory = r"C:\Users\A. Sahithi\Downloads"
        extension = ".xlsx"
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        full_paths = [os.path.join(directory, f) for f in files]
        latest_file = max(full_paths, key=os.path.getmtime)
        df = pd.read_excel(latest_file)
        payment_details23 = df["Primary Payments:"].head(1) + df["Supplemental Payments: "].head(1)
        payment_float = float(payment_details23.iloc[0])
        formatted_sum = "{:.6f}".format(payment_float)
        print("Payment: ", formatted_sum)
        return formatted_sum