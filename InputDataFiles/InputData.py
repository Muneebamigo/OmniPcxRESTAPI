'''
Created on May 17, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed

'''
from Key import config

class InputData():
       
    
    authuser = 'admin'
    authpassword='Admin@123'
    AuthsitePassword ="Admin@123"
    sitecode='010001'
    # Domain = 'http://172.20.11.253/opcxrrestapi'
    # ExcelSheetName=r'C:\Users\muneeb.ahmed\Downloads\OmniPcx_2.5.0.5-RestAPI_Automation\RESTAPI\R2.5.0.16-OmniPCX RECORD REST API Automated Tests Sheet.xlsx'
    #
    Domain = config.base_url
    ExcelSheetName = config.Excel_Sheet

    # Head Office Server IP's
    MainPrimaryServerIP = '172.20.11.253'
    MainSecondaryServerIP = "172.20.10.245"
    # Systems Settings Input Data When Recorder is Main/Head Office(Secondary Data base Credentials).
    MainSecondaryDBName = "opcxr_config_asec_245"
    MainSecondaryDBServerName = "172.20.13.30"
    MainSecondaryDBUsername = "postgres"
    MainSecondaryDBPassword = "0mniPcx"
    # Systems Settings Input Data When Recorder is Main/Head Office(Primary Data base Credentials).
    MainPrimaryDBName = "opcxr_config_apri_253"
    MainPrimaryDBServerName = "172.20.13.30"
    MainPrimaryDBUsername = "postgres"
    MainPrimaryDBPassword = "0mniPcx"
    
    # Branch Server IP's and input data.
    OPRID = "test OPR"
    BranchServerIP = "177.180.111.25"
    BranchRemoteIP = "177.177.177.178"
    # Systems Settings Input Data When Recorder is Branch(Primary Data base Credentials).
    BranchPrimaryDBName = "opcxr_config_abranchpri"
    BranchPrimaryDBServerName = "172.20.13.30"
    BranchPrimaryDBUsername = "postgres"
    BranchPrimaryDBPassword = "0mniPcx"
    # Systems Settings Input Data When Recorder is Branch(Secondary Data base Credentials).
    BranchSecondaryDBName = "opcxr_config_abranchsec"
    BranchSecondaryDBServerName = "172.20.13.30"
    BranchSecondaryDBUsername = "postgres"
    BranchSecondaryDBPassword = "0mniPcx"
    
    # Input Data for Branch Configurations/ Add Branch.
    BranchEmail = "abc@gmail.com"


    # BranchTransferURL = "ftp://172.20.1.246/Muneeb/APIatuo/"
    BranchTransferURL = "ftp://172.20.1.246/Muneeb/APIatuo/"
    BranchTransferUsername = "oxr"
    BranchTransferPassword = "0mniPcx"
    
    # Input Data for SMTP Configurations.
    SMTPServerName='smtp.gmail.com'
    SMTPUsername='sofiagujratan0@gmail.com'
    SMTPPassword='ctlz frmb opgp llwb'
    SenderEmailAddress='sofiagujratan0@gmail.com'

    # Mail Sending Informations
#     UserOne='zeeshan.waheed@amigo-software.com'
#     UserTwo='afnan.ahmad@ghost-software.com' # imran.uddin@amigo-software.com
#     UserThree='muhammad.saqib@amigo-software.com' # adnan.akhtar@amigo-software.com
#     UserFour='adnan.akhtar@amigo-software.com' # khawar.zaidi@amigo-software.com
#     UserFive='ahsan.rehman@amigo-software.com' # junaid.ali@amigo-software.com
#     UserSix='ali.tariq@amigo-software.com' # bilal.ghaffar@amigo-software.com
#     UserSeven='muhammad.haris@amigo-software.com' #  zeeshan.waheed@amigo-software.com
#     Subject='Rest API Test Cases Execution By Automation OPR v2.4.0.7'
#     EmailBody='Hi All,\n\nWe have successfully executed the REST API TEST Automation code on OPR v2.4.0.7 in Branch Office & Multi-Tenant Environment. Results can be seen in the attached excel sheet. \nPlease note that all the methods are executed using the session key generated against integrator token except for the Add Call, Archive Job and Archive Schedule Methods that are executed using session key generated against user token. \nIf You need more details please contact with QA Team.\n\nRegards,\nQA Team\n\n=====================================================================================\nThis is an auto-generated message by Automation Testing. Please do not reply to this email address.\n====================================================================================='
#     

    UserOne='muneeb.ahmed@amigo-software.com'
    # mailto =["muniba.nisar@amigo-software.com",]
    # mailcc = ["muneebanisar99@gmail.com","adnan.akhtar@amigo-software.com"]
    UserTwo='adnan.akhtar@amigo-software.com'
    # UserThree='' # adnan.akhtar@amigo-software.com
    # UserFour='' # khawar.zaidi@amigo-software.com
    # UserFive='' # junaid.ali@amigo-software.com
    # UserSix='' # bilal.ghaffar@amigo-software.com
    # UserSeven='' #  zeeshan.waheed@amigo-software.com
    Subject='Rest API Test Cases Execution By Automation OPR v2.5.0.16'
    EmailBody='Hi All,\n\nWe have successfully executed the REST API TEST Automation code on OPR v2.5.0.16 in Branch Office & Multi-Tenant Environment. Results can be seen in the attached excel sheet. \nPlease note that all the methods are executed using the session key generated against integrator token except for the Add Call, Archive Job and Archive Schedule Methods that are executed using session key generated against user token. \nIf You need more details please contact with QA Team.\n\nRegards,\nQA Team\n\n=====================================================================================\nThis is an auto-generated message by Automation Testing. Please do not reply to this email address.\n====================================================================================='
     
    # # purple_license
    # purple_masterToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBbWlnb1NvZnR3YXJlIiwic3ViIjoiT1BDWFJBUEkiLCJlbWFpbCI6ImFzc2lzdGFuY2VAYW1pZ28tc29mdHdhcmUuY29tIiwicm9sZSI6Ik1hbnVmYWN0dXJlciIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvaXNwZXJzaXN0ZW50IjoiVHJ1ZSIsImlhdCI6MTczOTc5MTk4MiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy92ZXJzaW9uIjoiUHJvZHVjdGlvbiIsImV4cCI6MTczOTc5Mzc4MiwiYXVkIjoiT1BDWFJBUElfRVhUIiwiTElJIjoiRmFsc2UiLCJVTlNUIjoiNCIsIkxJRE9TIjoiIiwiTVBUIjoiRmFsc2UiLCJleHBpcmVzX2F0IjoiMTczOTc5Mzc4MiIsIlJUQiI6IlRydWUiLCJleHBpcmVzX21pbnV0ZXMiOiIzMCIsIm5iZiI6MTczOTc5MTk4Mn0.6Inv5qjY4tDCKieKDxzjNDjkg6H-nwYE0GId6AQhwsE"
    # purple_user = "admin"
    # purple_ath_pwd = "F0rY0urEyes0nly$#@!"
    # purple_domain = "http://172.20.12.160/api"
