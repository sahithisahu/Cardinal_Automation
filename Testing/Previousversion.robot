*** Settings ***
Library         SeleniumLibrary
Library         XML

*** Variables ***
${url}          https://specialtyanalytics.cardinalhealth.com/
${browser}      chrome
${username}     rozario_joseph
${password}     Info@@712

*** Test Cases ***

successfullogin
    [Documentation]    Test to interact with the Bootstrap icon
    Open Browser    ${url}   ${browser}
    Maximize Browser Window
    set selenium speed     1
    login in to cardinal
    #Wait Until Element Is Visible   (//button[@class='mat-focus-indicator mat-menu-trigger topNavButton black-font mat-button mat-button-base'])[2]  timeout= 40sec
    #Close Browser

Open advanced practical analysis

    Wait Until Element Is Visible   (//button[@class='mat-focus-indicator mat-menu-trigger topNavButton black-font mat-button mat-button-base'])[2]  timeout= 30sec
    Click Element  (//button[@class='mat-focus-indicator mat-menu-trigger topNavButton black-font mat-button mat-button-base'])[2]

revenue cycle

    Wait Until Element Is Visible  //a[normalize-space()='Revenue Cycle']    timeout= 30sec
    Click Element   //a[normalize-space()='Revenue Cycle']

Charge details
    Wait Until Element Is Visible    //span[normalize-space()='Charge Details']    timeout= 30s
    Click Element    //span[normalize-space()='Charge Details']

applyfilter
    click apply

Take me back to previous version
    Click Element   //a[normalize-space()='Take me back to Previous Version']
    ${all_windows}=    Get Window Handles
    log    All window handles: ${all_windows}
    ${first_window}=   Set Variable  ${all_windows}[-1]


    Switch Window  ${first_window}
    Wait Until Page Contains Element    xpath=//td[normalize-space()='Analytics Center']
    ${element_text}=    Get Text    xpath=//td[normalize-space()='Analytics Center']
    Log    Text in new window: ${element_text}

    #Switch Window  title=Analytics Center
    #Wait Until Element Is Visible  //td[normalize-space()='Analytics Center']  timeout= 20s

    Click Element   //td[normalize-space()='Diagnosis Management']
    Wait Until Element Is Visible  //td[contains(text(),'How many patients are associated with a diagnosis?')]
    Click Element  //*[@id="76"]/div[2]/table/tbody/tr/td

    ${all_windows}=  Get window handles
    log   Get Window handles: ${all_windows}
    ${second_tab}   Set Variable  ${all_windows}[-2]


    switch window  ${second_tab}
    Wait Until Element Is Visible  xpath://td[normalize-space()='Diagnosis Summary']    timeout= 20s



*** Keywords ***
login in to cardinal
    Wait Until Element Is Visible    id=okta-signin-username    timeout=30s
    Input Text    id=okta-signin-username      ${USERNAME}
    Input text    id= okta-signin-password     ${password}
    Click Button  id=okta-signin-submit
    #Wait Until Element Is Visible    xpath://h4[normalize-space()='Welcome!']   timeout=30s

click apply
    Click Element   xpath://button[normalize-space()='Apply Filters']
    Wait Until Element Is Visible   xpath://button[normalize-space()='Apply Filters']
    sleep  3sec



