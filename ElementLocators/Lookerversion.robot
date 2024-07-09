*** Settings ***
Library     SeleniumLibrary
Library    Collections
Resource    ./../ElementLocators/Variables.robot


*** Keywords ***

login in to cardinal
    [Documentation]    Test to interact with the Bootstrap icon
    Open Browser    ${url}   ${browser}
    Maximize Browser Window
    set selenium speed     1

    Wait Until Element Is Visible    id=okta-signin-username    timeout=30s
    Input Text    id=okta-signin-username      ${USERNAME}
    Input text    id= okta-signin-password     ${password}
    Click Button  id=okta-signin-submit
    Wait Until Element Is Visible   (//button[@class='mat-focus-indicator mat-menu-trigger topNavButton black-font mat-button mat-button-base'])[2]  timeout= 30sec


    ${initial_window}=  Get Window Handles
    Log To Console    initial window: ${initial_window}
    ${initial_url}=    Get Location
    Log To Console    inital URL: ${initial_url}

Dashboard
# Open advanced practical analysis
   #[Tags]  sanity
    Wait Until Element Is Visible   (//button[@class='mat-focus-indicator mat-menu-trigger topNavButton black-font mat-button mat-button-base'])[2]  timeout= 30sec
    Click Element  (//button[@class='mat-focus-indicator mat-menu-trigger topNavButton black-font mat-button mat-button-base'])[2]

# open revenue cycle
    #[Tags]  sanity
    Wait Until Element Is Visible   //a[normalize-space()='Revenue Cycle']    timeout= 30sec
    Click Element   //a[normalize-space()='Revenue Cycle']

#Charge details
    Wait Until Element Is Visible    //span[normalize-space()='Charge Details']    timeout= 30s
    Click Element    //span[normalize-space()='Charge Details']

filters

    Wait Until Element Is Visible   (//button[@class='mat-focus-indicator mat-menu-trigger topNavButton black-font mat-button mat-button-base'])[2]  timeout= 30sec
     #Click Element   //ng-select[@type='checkbox']//span[@class='ng-arrow-wrapper']
    Click Element   (//span[@class='ng-arrow-wrapper'])[1]

    ${checkbox_xpath1}   Set Variable   xpath=//span[@class='ng-star-inserted'][normalize-space()='Alabama Oncology']
    Wait Until Element Is Visible    ${checkbox_xpath1}
    Click Element    ${checkbox_xpath1}

#    ${checkbox_xpath2}    Set Variable    xpath=//span[@class='ng-star-inserted'][normalize-space()='Alvarado Eye Associates Med Clinic INC']
#    Wait Until Element Is Visible    ${checkbox_xpath2}
#    Click Element    ${checkbox_xpath2}

#    ${checkbox_xpath3}    Set Variable    xpath=//span[@class='ng-star-inserted'][normalize-space()='Bolad Arthritis & Rheumatology']
#    Wait Until Element Is Visible    ${checkbox_xpath3}
#    Click Element    ${checkbox_xpath3}

#selectcalender
    Click Element   xpath://mat-icon[normalize-space()='calendar_month']
    ${month_option_xpath}    Set Variable    //span[normalize-space()='Previous Year']
    Wait Until Element Is Visible    ${month_option_xpath}    10s
    Click Element    ${month_option_xpath}

click apply
    Click Element   xpath://button[normalize-space()='Apply Filters']
    Wait Until Element Is Visible   xpath://button[normalize-space()='Apply Filters']
#    sleep  3sec



Retrieve patient count from looker

    ${all_windows}=    Get Window Handles
    Switch Window  ${all_windows}[0]

    Wait Until Element Is Visible    ${IFRAME_LOCATOR}
    Select Frame    ${IFRAME_LOCATOR}
    # Retrieve the value from the old website
    ${new_value}=    Get Text    ${looker_patient_served}
    Set Global Variable    ${new_value}
    Log To Console  Patient served from new website: ${new_value}



    ${new_charge}=    Get Text    ${looker_total_charge}
    Log To Console  Total charges from new website: ${new_charge}

    ${new_patient}=   Get Text  ${looker_new_patient}
    Set Global Variable   ${new_patient}
    Log to console   New patients visited from new website: ${new_patient}

    Unselect Frame

Payment details Amount payed

    Wait Until Element Is Visible    ${IFRAME_LOCATOR}
    Select Frame    ${IFRAME_LOCATOR}
    # Retrieve the value from the old website
    ${Payment_amount}=    Get Text   ${looker_payment}
    Log To Console  Amount payed from new website: ${Payment_amount}



