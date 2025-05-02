'''
Created on Aug 2, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests, random
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from test_Provisioning import test_04_DeviceConfigurations
from test_Provisioning import test_27_SystemLevelFilters
from Key import config

SheetName=	'28-System Level Rule'

class test_1_AddSLR(TestCase):
    
    # Start Test Case No 28-01
    def testcase_01_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules when CallType is Both/0, Condition is  All calls/32 and Action is Record both parties/0..')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='0'
        Condition='32'
        CallType='0'
        Device=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
        return SLRName
    # Test Case End
    
    # Start Test Case No 28-02
    def testcase_02_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules when CallType is Internal/1 Condition any(0 to 31)  and Action is Record both parties/0..')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Device Configuration Function calling
        Devices=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=Devices.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='0'
        Condition=str(random.randint(0 , 31))
        CallType='1'
        Device=DevID
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
    # Start Test Case No 28-03
    def testcase_03_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules when CallType is External/1 Condition any(0 to 31)  and Action is Record both parties/0..')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Device Configuration Function calling
        Devices=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=Devices.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='0'
        Condition=str(random.randint(0 , 31))
        CallType='2'
        Device=DevID
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
          
    # Start Test Case No 28-04
    def testcase_04_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules when CallType is both/0 Condition any(0 to 31)  and Action is Record local party only (for IPDR only)/1.')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Device Configuration Function calling
        Devices=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=Devices.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='1'
        Condition=str(random.randint(0 , 31))
        CallType='0'
        Device=DevID
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 28-05
    def testcase_05_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules when CallType is both/0 Condition any(0 to 31)  and Action is Record external party only (for IPDR only)/2.')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Device Configuration Function calling
        Devices=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=Devices.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='2'
        Condition=str(random.randint(0 , 31))
        CallType='0'
        Device=DevID
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
    # Start Test Case No 28-06
    def testcase_06_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules when CallType is both/0 Condition any(0 to 31) and Action is Ignore Call/3.')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        
        # Device Configuration Function calling
        Devices=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=Devices.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='3'
        Condition=str(random.randint(0 , 31))
        CallType='0'
        Device=DevID
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 28-07
    def testcase_07_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules with invalid/null systemLevelFilterID.')
        
        SLFID ='123456'
        
    
        # Device Configuration Function calling
        Devices=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=Devices.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='3'
        Condition=str(random.randint(0 , 31))
        CallType='0'
        Device=DevID
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
    # Start Test Case No 28-08
    def testcase_08_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules with condition  32 and But also add device value.')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Device Configuration Function calling
        Devices=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        ExtVal, pbxid=Devices.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters  
        SLRName=common.GenrateSimpleStringLimit10()
        Action='0'
        Condition='32'
        CallType='0'
        Device=DevID
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
    # Start Test Case No 28-11
    def testcase_11_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules Duplicate Rule Name.')
        
        # System Level Rule Function calling
        SLRName=test_1_AddSLR.testcase_01_AddSLR(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From Rules Where RuleName ='"+SLRName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        Action='0'
        Condition='32'
        CallType='0'
        Device=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 409:
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
    
    # Start Test Case No 28-12
    def testcase_12_AddSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Post Method Add System Level Rules' , 'Add System Level Rules with invalid site code.')
        
        # System Level Filters Function calling
        SLF=test_27_SystemLevelFilters.Test_1_AddSLF()
        SLFName=SLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+SLFName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        SLRName=common.GenrateSimpleStringLimit10()
        Action='0'
        Condition='32'
        CallType='0'
        Device=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SystemLevelFilterID':''+SLFID+'',
                    'SiteCode': '1234567',
                    'Name': ''+SLRName+'',
                    'Action': ''+Action+'',
                    'Condition': ''+Condition+'',
                    'Device': ''+Device+'',
                    'CallType': ''+CallType+'',
                    
                    }
        
        #Url For Add System Level Filters Rules
        UrlForAddSLR = '/SystemLevelFilter/AddRule/'
        URL = ''+common.Domain+''+UrlForAddSLR+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
class test_2_DeleteSLR(TestCase):
    
    # Start Test Case No 28-09
    def testcase_09_DeleteSLR(self, TestCasesStatus=True):
        
        TestCaseID = '28-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Delete Method Delete System Level Rules' , 'Delete System Level with valid SystemLevelRuleID.')
        
        # System Level Filters Function calling
        SLRName=test_1_AddSLR.testcase_01_AddSLR(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RuleId From Rules Where RuleName = '"+SLRName+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLRID = str(vals[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'SystemLevelRuleID': ''+SLRID+'',
                    
                    }
        
        #Url For Delete System Level Filters Rules
        UrlForDeleteSLR = '/SystemLevelFilter/DeleteRule/'
        URL = ''+common.Domain+''+UrlForDeleteSLR+''
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
            
    # Start Test Case No 28-10
    def testcase_10_DeleteSLR(self, TestCasesStatus=True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '28-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLR' , 'Using Delete Method Delete System Level Rules' , 'Delete System Level with Invalid SystemLevelRuleID.')
        
        SLRID='123456'
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'SystemLevelRuleID': ''+SLRID+'',
                    
                    }
        
        #Url For Delete System Level Filters Rules
        UrlForDeleteSLR = '/SystemLevelFilter/DeleteRule/'
        URL = ''+common.Domain+''+UrlForDeleteSLR+''
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