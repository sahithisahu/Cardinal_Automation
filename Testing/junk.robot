*** Settings ***
Library    SeleniumLibrary
Test Template

*** Variables ***
${URL}        https://specialtyanalytics.cardinalhealth.com/
${BROWSER}   chrome

*** Test Cases ***
Switch Between Windows
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Click the link that opens a new window
    Click Element   //a[normalize-space()='Take me back to Previous Version']

    # Get all window handles
    ${all_windows}=    Get Window Handles

    # Log the window handles for debugging purposes
    Log    All window handles: ${all_windows}

    # Assume the new window is the last in the list
    ${new_window}=    Set Variable    ${all_windows}[-1]

    # Switch to the new window
    Select Window    ${new_window}

    # Perform actions in the new window
    Wait Until Page Contains Element    xpath=//td[normalize-space()='Analytics Center']
    ${element_text}=    Get Text    xpath=//td[normalize-space()='Analytics Center']
    Log    Text in new window: ${element_text}

    # Switch back to the original window (assuming the original window is the first in the list)
    ${original_window}=    Set Variable    ${all_windows}[0]
    Select Window    ${original_window}

    # Optionally, perform actions in the original window or validate the switch
    Log    Switched back to the original window



    # Close the browser
    Close Browser
