*** Settings ***
Library   ExcelKeywords.py

*** Test Cases ***
Example Test Case
    ${output_path}=     ASP Value   r"C:\Users\A. Sahithi\Downloads
    Log to console  ${output_path}

    ${df}=      ASP_Qlik_final
    Log To Console   ${df}