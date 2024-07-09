*** Settings ***
Library     SeleniumLibrary
Library    Collections
Resource    ./../ElementLocators/Variables.robot


*** Keywords ***

Take me back to previous version

    Click Element   //a[normalize-space()='Take me back to Previous Version']
    #Wait Until Keyword Succeeds    10x    1s   New Tab Should Be Opened

    ${all_windows}=    Get Window Handles
#   Log To Console     ${all_windows}
    ${first_window}=   Set Variable  ${all_windows}[-1]

#    Log To Console   first_window: ${first_window}
    ${first_url}=  Get Location
    Log To Console   First_tab_url: ${first_url}



    Switch Window  ${first_window}
    Wait Until Page Contains Element    xpath=//td[normalize-space()='Analytics Center']
    ${element_text}=    Get Text    xpath=//td[normalize-space()='Analytics Center']
    Log    Text in new window: ${element_text}



    Click Element   //td[normalize-space()='Diagnosis Management']
    Wait Until Element Is Visible  //td[contains(text(),'How many patients are associated with a diagnosis?')]
    Click Element  //*[@id="76"]/div[2]/table/tbody/tr/td

#    Close Window


Open second window

    ${all_windows}=  Get window handles
#    Log To Console  ${all_windows}
    ${second_tab}   Set Variable  ${all_windows}[-1]
#    Log To Console   second_window: ${second_tab}

#    ${second_url}=  Get Location
#    Log To Console   second tab url: ${second_url}

    Switch Window  ${second_tab}

    Wait Until Element Is Visible   //span[normalize-space()='Diagnosis']    timeout= 30s
    Click Element   //span[normalize-space()='Diagnosis']
    sleep  3s



Qlik unselect month
    Wait Until Element Is Visible  //div[contains(@class,'QvFrame') and contains(@class,'Document_CS30')]/div[2]/div/div[1]/div[5]/div/div[3]/div[2]/div/img   timeout= 20s
    click element  //div[contains(@class,'QvFrame') and contains(@class,'Document_CS30')]/div[2]/div/div[1]/div[5]/div/div[3]/div[2]/div/img

Qlik select year
    click element   //div[@class='QvContent']/div[@class='QvListbox']/div/div[@title='2023']/div[1]
    sleep  3s


Retrieve patient served from Qlik


    Click Element   //td[@title='Fast Change']
    Wait Until Element Is Visible    //td[@title='Fast Change']
    sleep  2s

    ${old_value}=   Get Text    ${Qlik_patient_served}
    Set Global Variable  ${old_value}
    Log To Console  Patients served from old website: ${old_value}

#    ${old}=    Create List
#    ${old_value}=    Get Text    ${Qlik_patient_count}
#    Log To Console  Value from old website: ${old_value}
#    Append To List      ${old}   ${old_value}


Retrieve Total charges from Qlik
#    Fast chnage to get a table format

    Wait Until Element Is Visible   //div[@title='Service Summary']//div[@title='Fast change']  timeout= 20
    Click Element  //div[@title='Service Summary']//div[@title='Fast change']
#    click element  //div[@title='Service Summary']//div[@title='Fast change']

    sleep  2s

    ${old_charge}=  Get Text   ${Qlik_total_charges}
    Log to console  Total charges from old website: ${old_charge}

Retrieve Patient count from Qlik

    Wait Until Element Is Visible   //span[normalize-space()='New Patient']     timeout= 60s
    Click Element  //span[normalize-space()='New Patient']
    sleep  3s

    Click Element  //div[@title='New Office Visits']//div[@title='Send to Excel']



Retrieve payment details from Qlik

    ${all_windows}=    Get Window Handles
    Switch Window  ${all_windows}[-2]


    Wait Until Element Is Visible   //td[normalize-space()='Reimbursement Management']
    Click Element   //td[normalize-space()='Reimbursement Management']
    Click Element   //td[contains(text(),'How can I view details around my denied claims?')]



    ${all_windows}=    Get Window Handles
    Switch Window  ${all_windows}[-1]

#    Execute JavaScript    arguments[0].scrollIntoView()  xpath://a[@class='qvtr-scroll-left']//span[contains(text(),'◄')]
    Wait Until Element Is Visible   //a[@href='javascript:;']//span[contains(text(),'▼')]  timeout= 30
    Click element     //a[@href='javascript:;']//span[contains(text(),'▼')]
    click element   //li[@title='Reimbursement']
    sleep  3

#    Qlik unselect month
    Wait Until Element Is Visible  //div[contains(@class,'QvFrame') and contains(@class,'Document_CS09')]/div[2]/div/div[1]/div[5]/div/div[3]/div[2]/div/img   timeout= 20s
    click element  //div[contains(@class,'QvFrame') and contains(@class,'Document_CS09')]/div[2]/div/div[1]/div[5]/div/div[3]/div[2]/div/img

#    Qlik select year
     click element   //div[contains(@class,'QvFrame') and contains(@class,'Document_LB218')]/div[2]/div/div/div[2]/div
#    sleep  3s

    click element  //div[contains(@class,'QvFrame') and contains(@class,'Document_CH84')]/div/div/div[2]
    sleep  3
