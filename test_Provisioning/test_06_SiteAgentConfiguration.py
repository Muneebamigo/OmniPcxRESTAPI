'''
Created on Jul 16, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase

from test_Provisioning import test_05_TeamConfigurations as teamfunctions
from test_Provisioning import test_04_DeviceConfigurations as devicefunctions
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from Key import config



SheetName=	'6-Site Agent Configuration'

class test_1_AddSiteAgentConfigurations(TestCase):

    # Start Test Case No 06-01
    def testcase_01_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('01-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with valid data')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'FirstName': '' + AgentFName + '',
                      'LastName': '' + AgentLName + '',
                      'Email': '' + email + '',
                      'Username': '' + username + '',
                      'Password': '' + password + '',
                      # In updated release the password string will be change
                      # 'Password': "Admin@1234",

                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': '' + TimeZone + '',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': '' + DevID + '',
                      'SitePermission': '3',
                      'Team': '' + TeamID + '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '0',

                      }

        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

        return username,teamname,ExtVal,pbxid
        # Test Case End

    # Start Test Case No 06-02
    def testcase_02_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('02-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with Invalid data, invalid team Id and Device Id')

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        DevID='12345'
        TeamID = '12345'
        # Generate Simple Character String Limit 10 Characters       
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Email
        email = common.GenerateEmail()
        # Generate Valid Password
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '3',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = '' + common.Domain + '' + UrlAddAgent + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File       
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 06-12
    def testcase_12_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('12-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with valid data with Null FirstName')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = ''
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '5',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

        return username,teamname,ExtVal,pbxid
        # Test Case End

    # Start Test Case No 06-13
    def testcase_13_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('13-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with valid data with invalid TimeZone Format')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "acb123abc000"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

        return username,teamname,ExtVal,pbxid
        # Test Case End

    # Start Test Case No 06-14
    def testcase_14_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('14-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with valid data with duplicate username.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        username,teamname,ExtVal1,pbxid1=test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        pbxid1=pbxid1
        ExtVal1=ExtVal1
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 409:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

    # Start Test Case No 06-15
    def testcase_15_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('15-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with invalid site code.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '1234567',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 500:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

    # Start Test Case No 06-16
    def testcase_16_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('16-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with valid data when server role configured as secondary.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
        # Test Case End

    # Start Test Case No 06-17
    def testcase_17_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('17-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with valid data when server role configured as branch.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

        # Test Case End

    # Start Test Case No 06-18
    def testcase_18_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('18-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with special character username.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        usernamee,teamname,ExtVal1,pbxid=test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        usernamee=usernamee
        pbxid=pbxid
        ExtVal1=ExtVal1
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"
        username = '!@#$%^&*'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False


    # Start Test Case No 06-19
    def testcase_19_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('19-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with special character, single qoute in first name and last name.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid

        # # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        firstname=common.GenrateSimpleStringLimit10()
        lastname=common.GenrateSimpleStringLimit10()
        AgentFName = ""+firstname+"'"
        AgentLName = ""+lastname+"'"
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"
        username = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False


    # Start Test Case No 06-20
    def testcase_20_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('20-Site Agent', 'Calling Adding Method of Agent', 'User is not able to add agent from REST API with empty email when "SendEmailEnabled" parameter is passed as True.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()

        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': '',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'True',
                      'DefaultLandingPage': '0',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

        # Test Case End


    # Start Test Case No 06-21
    def testcase_21_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('01-Site Agent', 'Calling Adding Method of Agent', 'User is not able to add agent from REST API when "SendEmailEnabled" parameter is passed as True and device is passed as SIPTrunk/Trunk. ')

        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()

        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': '1',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'True',
                      'DefaultLandingPage': '0',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False



    # Start Test Case No 06-22
    def testcase_22_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('01-Site Agent', 'Calling Adding Method of Agent', 'Add Agent with invalid data when DefaultLandingPage value is in valid or non existing 50.')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '50',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False

        return username,teamname,ExtVal,pbxid
        # Test Case End

    def testcase_23_AddAgent(self, TestCasesStatus=True):

        TestCaseID = '06-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('23-Site Agent', 'Calling Adding Method of Agent', 'Add Site Agent with Server Session Key')

        # Devices/Extenssions Configurations Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        teamname = common.GenrateSimpleStringLimit10()
        teamdesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+teamname+"','"+teamdesc+"',1 );")
        cursor.execute(SQLCommand1)
        cursor.commit()

        # SQL Queries for Data Verification
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand4)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()
        # SQL Queries for Data Verification
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand5)
        devid=cursor.fetchone()
        DevID=str(devid[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Valid Email 
        email = common.GenerateEmail()
        # Generate Valid Password String
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '0',

                     }
        # Url For Add Agent
        UrlAddAgent = '/SiteAgent/Add'
        URL = ''+common.Domain+''+UrlAddAgent+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 401:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False


class test_4_DeleteSiteAgentConfigurations(TestCase):

    # Url For Delete Agent
    UrlDeleteAgent = '/SiteAgent/Delete/'

    # Start Test Case No 06-03
    def testcase_03_DeleteAgent(self):

        TestCaseID = '06-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('03-Site Agent', 'Calling Delete Method of Agent', 'Delete Agent with valid Id')
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # Add Site Agent Function calling
        username,teamname,ExtVal,PBXID = test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        PBXID=PBXID
        # SQL Queries for Data Verification
        SQLCommand = ("Select UserId from Users where Username = '"+username+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        UserId = str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': ''+UserId+'',
                     }
        # Url For Delete Agent
        URL = ''+common.Domain +''+self.UrlDeleteAgent+''+UserId+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 200:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

    # Start Test Case No 06-04
    def testcase_04_DeleteAgent(self):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '06-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('04-Site Agent', 'Calling Delete Method of Agent', 'Delete Agent with invalid ID')

        UserId = '123456'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': ''+UserId+'',
                     }
        # Url For Delete Agent
        URL = '' + common.Domain + '' + self.UrlDeleteAgent + UserId
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 400:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
    def testcase_24_DeleteAgent(self):

        TestCaseID = '06-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('24-Site Agent', 'Calling Delete Method of Agent', 'Delete Site Agent with Server Session Key')
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # Add Site Agent Function calling
        username,teamname,ExtVal,PBXID = test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        PBXID=PBXID
        # SQL Queries for Data Verification
        SQLCommand = ("Select UserId from Users where Username = '"+username+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        UserId = str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'id': ''+UserId+'',
                     }
        # Url For Delete Agent
        URL = ''+common.Domain +''+self.UrlDeleteAgent+''+UserId+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 401:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

class test_2_UpdateSiteAgentConfigurations(TestCase):

    # Url For Update Agent
    UrlUpdateAgent = '/SiteAgent/Update'

    # Start Test Case No 06-05
    def testcase_05_updateAgent(self):

        TestCaseID = '06-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('05-Site Agent', 'Calling Updating Method of Agent', 'Update Agent with Valid')
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()

        # Add Site Agent Function calling
        username,teamname,ExtVal,PBXID = test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # SQL Queries for Data Verification   
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand1)
        vals = cursor.fetchone()
        TeamID = str(vals[0])

        # SQL Queries for Data Verification
        SQLCommand2 = ("Select UserId from Users where Username = '"+username+"';")
        cursor.execute(SQLCommand2)
        valss = cursor.fetchone()

        agantid = str(valss[0])

        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Email
        email = common.GenerateEmail()
        # Generate Password
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': ''+agantid+'',
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Update Agent
        URL = '' + common.Domain + '' + self.UrlUpdateAgent + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 200:
                print(common.SuccessMessage)
                status ='Passed'
            else:
                status='Failed'
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

    # Start Test Case No 06-06
    def testcase_06_updateAgent(self):

        TestCaseID = '06-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('06-Site Agent', 'Calling Updating Method of Agent', 'Update Agent with invalid ID')
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # Team Function calling
        TeamFunction = teamfunctions.Test_1_AddTeamCofiguration()
        team = TeamFunction.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)
        # Device Function calling
        DeviceFunctions = devicefunctions.test_1_AddDeviceConfiguration()
        ExtVal, pbxid = DeviceFunctions.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        pbxid=cursor.fetchone()
        DevID=str(pbxid[0])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select Groupid from Groups Where Name = '"+team+"';")
        cursor.execute(SQLCommand1)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()

        agantid = '123456'
        # Generate Simple Character String Limit 10 Characters         
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Email
        email = common.GenerateEmail()
        # Generate Valid Password
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': ''+agantid+'',
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Update Agent
        URL = '' + common.Domain + '' + self.UrlUpdateAgent + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 400:
                print(common.SuccessMessage)
                status ='Passed'
            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
    def testcase_25_updateAgent(self):

        TestCaseID = '06-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('25-Site Agent', 'Calling Updating Method of Agent', 'Update Site Agent with Server Session Key')
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()

        # Add Site Agent Function calling
        username,teamname,ExtVal,PBXID = test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # SQL Queries for Data Verification   
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand1)
        vals = cursor.fetchone()
        TeamID = str(vals[0])

        # SQL Queries for Data Verification
        SQLCommand2 = ("Select UserId from Users where Username = '"+username+"';")
        cursor.execute(SQLCommand2)
        valss = cursor.fetchone()

        agantid = str(valss[0])

        cursor.commit()
        # Generate Simple Character String Limit 10 Characters        
        AgentFName = common.GenrateSimpleStringLimit10()
        AgentLName = common.GenrateSimpleStringLimit10()
        username = common.GenrateSimpleStringLimit10()
        # Generate Email
        email = common.GenerateEmail()
        # Generate Password
        password = common.GenrateValidPasswordString()
        TimeZone = "12:00:00"

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'id': ''+agantid+'',
                      'SiteCode': '',
                      'FirstName': ''+AgentFName+'',
                      'LastName': ''+AgentLName+'',
                      'Email': ''+email+'',
                      'Username': ''+username+'',
                      'Password': ''+password+'',
                      'WindowsUsername': '',
                      'ScreenCapturingEnabled': 'False',
                      'TimeZone': ''+TimeZone+'',
                      'QualityMonitorLoginEnabled': 'False',
                      'LoginEnabled': 'True',
                      'ActiveDirectoryEnabled': 'False',
                      'ADSID': '',
                      'PasswordNeverExpireEnabled': 'True',
                      'LoginPasswordChangeEnabled': 'False',
                      'Device': ''+DevID+'',
                      'SitePermission': '3',
                      'Team': '' +TeamID+ '',
                      'SendEmailEnabled': 'False',
                      'DefaultLandingPage': '',

                     }
        # Url For Update Agent
        URL = '' + common.Domain + '' + self.UrlUpdateAgent + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 401:
                print(common.SuccessMessage)
                status ='Passed'
            else:
                status='Failed'
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

class test_3_GetSiteAgentConfigurations(TestCase):

    # Url For Get Agent
    UrlGetAgent =  '/SiteAgent/Get/'
    UrlGetAgentById =  '/SiteAgent/Get/'
    UrlGetAgentByUsername =  '/SiteAgent/Get/?username='

    # Start Test Case No 06-07
    def testcase_07_GetAllAgent(self):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '06-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('07-Site Agent', 'Get Method of Agent', 'Get All Agent')
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': '',
                      'username': ''
                     }
        # Url For Get Agent
        URL = '' + common.Domain + '' + self.UrlGetAgent + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 200:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End


    # Start Test Case No 06-08
    def testcase_08_GetAgentById(self):

        TestCaseID = '06-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('08-Site Agent', 'Get By ID Method of Agent', 'Get Agent by valid Id')
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # Add Site Agent Function calling
        username,teamname,ExtVal,PBXID = test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        PBXID=PBXID
        # SQL Queries for Data Verification
        SQLCommand = ("Select UserId from Users where Username = '"+username+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        AgentId = str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': ''+AgentId+'',
                      'username': ''

                     }
        # Url For Get Agent
        URL = ''+common.Domain+''+self.UrlGetAgentById+''+AgentId+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 200:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

    # Start Test Case No 06-09
    def testcase_09_GetAgentById(self):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '06-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('09-Site Agent', 'Get By ID Method of Agent', 'Get Agent by Invalid Id')

        AgentId = '123456'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': ''+AgentId+'',
                      'username': ''

                     }
        # Url For Get Agent
        URL = ''+common.Domain+''+self.UrlGetAgentById+''+AgentId+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 400:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End


    #Start Test Case No 06-10
    def testcase_10_GetAgentByUsername(self):

        TestCaseID = '06-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('10-Site Agent', 'Get By Username Method of Agent', 'Get Agent by valid username')

        # Add Site Agent Function calling
        username,teamname,ExtVal,PBXID = test_1_AddSiteAgentConfigurations.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        PBXID=PBXID

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': '',
                      'username': ''+username+'',
                     }
        # Url For Get Agent
        URL = '' + common.Domain + '' + self.UrlGetAgentByUsername + "'"+username+"'" + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 200:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

    # Start Test Case No 06-01
    def testcase_11_GetAgentByUsername(self):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '06-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('11-Site Agent', 'Get By Username Method of Agent', 'Get Agent by invalid username')

        username = 'abcd'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'id': '',
                      'username': ''+username+'',
                     }
        # Url For Get Agent
        URL = '' + common.Domain + '' + self.UrlGetAgentByUsername + "'"+username+"'" + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 400:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End


    def testcase_26_GetAllAgent(self):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '06-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('26-Site Agent', 'Get Method of Agent', 'Get All Agent with Server session Key')
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'id': '',
                      'username': ''
                     }
        # Url For Get Agent
        URL = '' + common.Domain + '' + self.UrlGetAgent + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 401:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status='Failed'
        # Write Output Result in Excel File        
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End