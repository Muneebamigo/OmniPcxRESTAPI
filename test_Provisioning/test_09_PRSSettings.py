'''
Created on Jul 20, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed

----------------pre requisite--------------------------------------
System setting must be configured.
Basic PRS Settings is by default define when install the PBX Recorder.
all asic parameters are define in the  InputData.py file

------------------OutPut----------------------------
This module will be Update the PRS Settings by Put
Request.

All the updation which is perform is Shown on the system settings page
(There is heading with the name of PRS Settings)
 of the server administration

'''

import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase

import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from Key import config
from InputDataFiles import InputData
SheetName=    '9-PRS Settings'


class UpdatePRSSettings(TestCase):
    
    # Calling Input Data File
    ssinputdata = InputData.InputData()
    # Url For Update PRS Settings
    UrlForUpdatePRSSettings = '/SystemSettings/UpdatePRSSettings'
    
    # Start Test Case No 09-01
    def testcase_01_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings with version greater then or equal to 5 when AuthUser is Admin.')
        # Generate Valid IP
        ValidIP=common.GenrateValidIPString()
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+ValidIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
        
    # Start Test Case No 09-02
    def testcase_02_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings with version Less then 5 when AuthUser is admin.')
        # Generate Valid IP
        ValidIP=common.GenrateValidIPString()
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '4.0'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+ValidIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
    
    # Start Test Case No 09-03
    def testcase_03_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings with Invalid IP.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '4.0'
        InValidIP = 'abcd123'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+InValidIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
            
            
    # Start Test Case No 09-04
    def testcase_04_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings PRS IP same as secondary server IP.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
            
            
    # Start Test Case No 09-05
    def testcase_05_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings when PRSIP same as branch primary server IP.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+self.ssinputdata.BranchServerIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
            
            
    # Start Test Case No 09-06
    def testcase_06_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings when PRSIP same as branch secondary server IP.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+self.ssinputdata.BranchRemoteIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
            
            
    # Start Test Case No 09-07
    def testcase_07_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings when PRSIP is same as primary server IP.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
            
            
            
        configdb=common.StringDBConnectivity()
        
        # SQL Queries For Update Config DB Admin password
        SQLCommand = ("Update DefaultSettings SET PRSIP = '' ;")
        configdb.execute(SQLCommand)
        configdb.commit()
        

    def testcase_08_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Update PRS Settings with Site Session Key')
        # Generate Valid IP
        ValidIP=common.GenrateValidIPString()
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+ValidIP+'',
                      'PrsSoapId': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End
            
            
    def testcase_09_UpdatePRSSettings(self, TestCasesStatus=True):
        
        TestCaseID = '09-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method', 'Configure the PRS Settings with version greater then or equal to 5 when AuthUser is Admin and EnableCommonPRSIdentifier is True.')
        # Generate Valid IP
        ValidIP=common.GenrateValidIPString()
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'PRSVersion': ''+PRSVersion+'',
                      'PRSIP': ''+ValidIP+'',
                      'PrsSoapId': '',
                      'EnableCommonPRSIdentifier': 'true',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePRSSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            TestCasesStatus = False
            # Test Case End

    def testcase_10_UpdatePRSSettings(self, TestCasesStatus=True):

        TestCaseID = '09-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PRS Settings', 'PRS Settings Through Put Method',
                      'Configure the PRS Settings with version greater then or equal to 5 when AuthUser is Admin and EnableCommonPRSIdentifier is True'
                      'with empty PRSVersion and PRSIP .')

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PRSVersion = '5.0'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PRSVersion': '',
                      'PRSIP':  '',
                      'PrsSoapId': '',
                      'EnableCommonPRSIdentifier': 'true',

                      }
        # Url For Update PRS Settings
        URL = '' + common.Domain + '' + self.UrlForUpdatePRSSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End