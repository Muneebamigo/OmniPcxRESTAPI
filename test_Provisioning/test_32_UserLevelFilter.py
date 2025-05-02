'''
Created on Jul 31, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests, random
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from test_Provisioning import test_06_SiteAgentConfiguration
from unittest import TestCase
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from Key import config
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill

SheetName=	'32-User Level Filter'

class test_1_AddUserLevelFilter(TestCase):
    
    #Url For Add User Level Filters
    UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
    
    
    # Start Test Case No 32-01
    def testcase_01_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record both parties", condition is "All Calls" , Call type is "both".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        ULFName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+ULFName+'',
                      'Action': '0',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+ULFName+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == ULFName:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
        return ULFName, username
            
    # Test Case End
    
    # Start Test Case No 32-02
    def testcase_02_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record both parties", condition is "All Calls" , Call type is "internal".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '0',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'1',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End

    # Start Test Case No 32-03
    def testcase_03_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record both parties", condition is "All Calls" , Call type is "external".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '0',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'2',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-04
    def testcase_04_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record local party only (for IPDR only)", condition is "All Calls" , Call type is "both".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '1',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-05
    def testcase_05_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record local party only (for IPDR only)", condition is "All Calls" , Call type is "internal".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '1',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'1',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End

    # Start Test Case No 32-06
    def testcase_06_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record local party only (for IPDR only)", condition is "All Calls" , Call type is "external".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '1',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'2',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-07
    def testcase_07_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record external party only (for IPDR only)", condition is "All Calls" , Call type is "both".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '2',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-08
    def testcase_08_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record external party only (for IPDR only)", condition is "All Calls" , Call type is "internal".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '2',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'1',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End

    # Start Test Case No 32-09
    def testcase_09_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record external party only (for IPDR only)", condition is "All Calls" , Call type is "external".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '2',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'2',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-10
    def testcase_10_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Ignore Call", condition is "All Calls" , Call type is "both".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '3',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-11
    def testcase_11_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Ignore Call", condition is "All Calls" , Call type is "internal".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '3',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'1',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
           
    # Test Case End

    # Start Test Case No 32-12
    def testcase_12_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Ignore Call", condition is "All Calls" , Call type is "external".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '3',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'2',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
      
    # Start Test Case No 32-13
    def testcase_13_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When Action is "Record both parties", condition is "Random between 0 to 24" , Call type is "both".')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        print(username)
        print(ExtVal)
        pbxid=pbxid
        # SQL Queries for Data Verification
        '''
        SQLCommand2 = ("Select Extension from Users Where Username = '"+username+"';")
        cursor.execute(SQLCommand2)
        extvalue=cursor.fetchone()
        Device = str(extvalue[0])
        cursor.commit()
        '''
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        Condition=str(random.randint(1 , 24))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+Name+'',
                      'Action': '0',
                      'Condition': ''+Condition+'',
                      'Device': ''+ExtVal+'',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RuleName from Rules Where RuleName = '"+Name+"';")
        cursor.execute(SQLCommand1)
        RuleName=cursor.fetchone()
        cursor.commit()
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if RuleName[0] == Name:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
        # Test Case End
        
    # Start Test Case No 32-18
    def testcase_18_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF With invalid Site Code.')
        
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        # Generate Simple Character String Limit 10 Characters
        ULFName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '1234567',
                      'UserName': ''+username+'',
                      'Name': ''+ULFName+'',
                      'Action': '0',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 500:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Start Test Case No 32-19
    def testcase_19_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When server role configured as secondary.')
       
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        ULFName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+ULFName+'',
                      'Action': '0',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
    # Test Case End
    
    # Start Test Case No 32-20
    def testcase_20_AddUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Post Method Add UserLevelFilter' , 'Configure the ULF When server role configured as branch.')
       
        # Site Agent Function calling
        SiteAgentFunctions=test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        teamname=teamname
        ExtVal=ExtVal
        pbxid=pbxid
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        ULFName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserName': ''+username+'',
                      'Name': ''+ULFName+'',
                      'Action': '0',
                      'Condition': '25',
                      'Device': '',
                      'CallType':'0',
    
                    }
        
        #Url For Add User Level Filters
        UrlForAddUserLevelFilter = '/UserLevelFilter/Add'
        URL = ''+common.Domain+''+UrlForAddUserLevelFilter+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
    # Test Case End
    
    
class test_2_UpdateUserLevelFilter(TestCase):
    
        
    # Start Test Case No 32-21
    def testcase_21_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When Action is "Record both parties" and day / time not required with valid ID.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-22
    def testcase_22_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF with invalid ID.')
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID='123456'
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+ID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-23
    def testcase_23_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF with invalid site code ID.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'123456',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 500:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-24
    def testcase_24_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF with recordingcalldirection is 1.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '1',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-25
    def testcase_25_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF when recordingcalldirection is 2.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '2',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-26
    def testcase_26_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 1.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        StartTime=time.strftime("%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '1',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': ''+StartTime+'',
                      'EndTime': '23:59:00',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-27
    def testcase_27_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-27'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 2.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        StartTime=time.strftime("%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '2',
                      'Day': '1',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': ''+StartTime+'',
                      'EndTime': '23:59:00',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-28
    def testcase_28_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-28'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 3.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        StartTime=time.strftime("%H:%M:%S")
        StartDate= time.strftime("%d/%m/%Y")
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '3',
                      'Day': '1',
                      'StartDate': ''+StartDate+'',
                      'EndDate': '28/12/2025',
                      'StartTime': ''+StartTime+'',
                      'EndTime': '23:59:00',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-29
    def testcase_29_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-29'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 1 but starttime Endtime is empty or null.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '1',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-30
    def testcase_30_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-30'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 1 but starttime Endtime is invalid format.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '1',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': 'ab12ab12',
                      'EndTime': 'ab12ab12',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-31
    def testcase_31_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-31'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 2 but day is empty or null.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        StartTime=time.strftime("%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '2',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': ''+StartTime+'',
                      'EndTime': '23:59:00',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-32
    def testcase_32_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-32'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 3 but startdate Enddate is empty null.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        StartTime=time.strftime("%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '3',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': ''+StartTime+'',
                      'EndTime': '23:59:00',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-33
    def testcase_33_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-33'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 3 but startdate, Enddate is invalid format.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        StartDate='ab12ab12'
        StartTime=time.strftime("%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '3',
                      'Day': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': 'ab12ab12',
                      'StartTime': ''+StartTime+'',
                      'EndTime': '23:59:00',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    
    # Start Test Case No 32-34
    def testcase_34_UpdateUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-34'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Put Method Update UserLevelFilter' , 'Update the ULF When schedule is 3 when startdate less then enddate.')
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select RecordingFilterId from Users where username = '"+username+"';")
        cursor.execute(SQLCommand1)
        ID=cursor.fetchone()
        RFID=str(ID[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Description = common.GenrateSimpleStringLimit10()
        
        StartTime=time.strftime("%H:%M:%S")
        EndDate= time.strftime("%d/%m/%Y")
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'ID': ''+RFID+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '3',
                      'Day': '1',
                      'StartDate': '28/12/2025',
                      'EndDate': ''+EndDate+'',
                      'StartTime': ''+StartTime+'',
                      'EndTime': '23:59:00',
                      
                     }
        
        #Url For Update User Level Filters
        UrlForUpdateUserLevelFilter = '/UserLevelFilter/Update'
        URL = ''+common.Domain+''+UrlForUpdateUserLevelFilter+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
        
class test_3_GetUserLevelFilter(TestCase):
    
    #Url For Add User Level Filters
    UrlForGetUserLevelFilter = '/UserLevelFilter/Get'
    
    # Start Test Case No 32-14
    def testcase_14_GetUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Get Method Get all UserLevelFilter' , 'Get all ULF data with valid User Name.')
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        ULFName=ULFName
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'Username':''+username+'',
    
                    }
        
        #Url For Add User Level Filters
        URL = ''+common.Domain+''+self.UrlForGetUserLevelFilter+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-14
    def testcase_15_GetUserLevelFilter(self, TestCasesStatus=True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '32-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Get Method Get all UserLevelFilter' , 'Get all ULF data with invalid User Name.')
        
        
        username='ABC12345'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'Username':''+username+'',
    
                    }
        
        #Url For Add User Level Filters
        URL = ''+common.Domain+''+self.UrlForGetUserLevelFilter+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
class test_4_DeleteUserLevelFilter(TestCase):
    
    #Url For Add User Level Filters
    UrlForDeleteUserLevelFilter = '/UserLevelFilter/Delete'
    
    # Start Test Case No 32-16
    def testcase_16_DeleteUserLevelFilter(self, TestCasesStatus=True):
        
        TestCaseID = '32-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Delete Method Delete all UserLevelFilter' , 'Delete all ULF data with valid User Name.')
        
        # ULF Function calling
        ULFName, username= test_1_AddUserLevelFilter.testcase_01_AddUserLevelFilter(common.PrereqTestCasesStatusUpdate)
        username=username
        # Tenant DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select RuleId From Rules Where RuleName = '"+ULFName+"';")
        cursor.execute(SQLCommand2)
        ULFID=cursor.fetchone()
        UserLevelFilterID = str(ULFID[0])
        cursor.commit()
        # Test Case Start Time
        starttime = time.process_time()
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserLevelFilterID':''+UserLevelFilterID+'',
    
                    }
        
        #Url For Add User Level Filters
        URL = ''+common.Domain+''+self.UrlForDeleteUserLevelFilter+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    
    # Start Test Case No 32-17
    def testcase_17_GetUserLevelFilter(self, TestCasesStatus=True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '32-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('UserLevelFilter' , 'Using Delete Method Delete UserLevelFilter data' , 'Delete a single ULF data with invalid User Name.')
        
        UserLevelFilterID='12345'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'UserLevelFilterID':''+UserLevelFilterID+'',
    
                    }
        
        #Url For Add User Level Filters
        URL = ''+common.Domain+''+self.UrlForDeleteUserLevelFilter+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    # Test Case End
    