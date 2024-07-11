*** Settings ***
Library    SeleniumLibrary
Library    Process
Library  ASP.py

*** Variables ***

*** Test Cases ***

Compare ASP Values

    ${ASP_compare}=      ASP_Qlik
    Log To Console   ${ASP_compare}6