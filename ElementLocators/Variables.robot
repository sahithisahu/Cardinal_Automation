***Variables***

${url}          https://specialtyanalytics.cardinalhealth.com/
${browser}      chrome
${username}     rozario_joseph
${password}     Info@@712
${dropdown}     //ng-select[@type='checkbox']//span[@class='ng-arrow']
${previousversion}   //a[normalize-space()='Take me back to Previous Version']
#${looker_patient_count}  //*[@id="styled-tile-dashboard"]/div/section/div/div[2]/div
${looker_patient_served}  //*[@id="styled-tile-dashboard"]/div/section/div/div[2]/div/div[2]/p/span/a
${iframe_locator}    //iframe[@class='lookerIFrameClass']
${Qlik_patient_served}       //div[contains(@class,'QvFrame') and contains(@class,'Document_CH133_786473925')]/div[2]/div/div/div[6]/div/div[1]
${new_value}=    Get Text   ${looker_patient_served}
${old_value}=   Get Text    ${Qlik_patient_served}
${Qlik_total_charges}     //div[contains(@class,'QvFrame') and contains(@class,'Document_CH88_483033855')]/div[2]/div/div/div[6]/div/div[1]
${looker_total_charge}  //*[@id="styled-tile-dashboard"][4]//p/span
${looker_new_patient}    //*[@id="styled-tile-dashboard"][2]/div/section/div/div[2]/div/div[2]/p/span/a
${looker_payment}      //*[@id="styled-tile-dashboard"]/div/section/div/div[2]/div/div[2]/p/span
${excel_download}      //div[contains(@class,'QvFrame') and contains(@class,'Document_CH131_359387946')]/div/div/div[3]
