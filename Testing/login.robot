*** Settings ***
Library     SeleniumLibrary
Library     XML
Library     Collections
Library     SeleniumPython.py
#Library     DataDriver   ../Testing/Patient_visit.xlsx   sheet_name=sheet1
Resource    ./../ElementLocators/Variables.robot
Resource    ./../ElementLocators/Lookerversion.robot
Resource    ./../ElementLocators/QlikVersion.robot
Library      BuiltIn
Library      String
Library    OperatingSystem




*** Test Cases ***

Login

    login in to cardinal

open looker Dashboard
    Dashboard
    Filters
    click apply
    Retrieve patient count from looker

Previous Version

    Take me back to previous version
    Open second window
    Qlik unselect month
    Qlik select year


Retrieve Values

    Retrieve patient served from Qlik
    Retrieve Total charges from Qlik
    Retrieve Patient count from Qlik
    ${patient_visit}=   get_patient_visit
    Set Global Variable   ${patient_visit}
    Log To Console   ${patient_visit}

    Retrieve patient count from looker

Compare Cleaned Numbers
    [Documentation]    Compare dynamically fetched values after cleaning.
#    ${cleaned_looker}=    Clean Number    ${looker_new_patient}
#    ${cleaned_qlik}=      Clean Number    ${patient_visit}
    ${looker_number}=     Convert To String    ${new_patient}
    ${qlik_number}=       Convert To String    ${patient_visit}
    Log To Console   Cleaned Looker value: ${looker_number}
    Log To Console  Cleaned Qlik value: ${qlik_number}

    Should Not Be Equal  ${new_patient}   ${qlik_number}


Payment details
    Wait Until Element Is Visible   //a[normalize-space()="Payment Details"]
    Click element   //a[normalize-space()="Payment Details"]
    Payment details Amount payed
#    Close Window
    Retrieve payment details from Qlik
    sleep  2s
    ${Qlik_payment_details}=  get_payment_details
    Log To Console   ${Qlik_payment_details}




#*** Keywords ***
#Clean Number
#    [Arguments]    ${number}
#    ${number}=    strip String    ${number}
#    ${cleaned_number}=    Replace String    ${number}    ,    ${EMPTY}
#    [RETURN]    ${cleaned_number}