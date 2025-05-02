'''
Created on Mar 12, 2020

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''


import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from openpyxl import load_workbook
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from InputDataFiles import InputData
from Key import config
SheetName=	'55-PBX User Management'

class UpdatePBXUserManagementConfiguration(TestCase):
    
    # Calling Input Data File
    ssinputdata = InputData.InputData()
    
    UrlForUpdatePBXUserManagementConfiguration = '/SystemSettings/UpdateOXEUserManagementConfigurations'
    
    # Start Test Case No 55-01
    def testcase_01_UpdatePBXUserManagementConfigurationwithHTTP(self, TestCasesStatus=True):
        
        TestCaseID = '55-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBXUserManagement Settings', 'PBXUserManagement Settings Through Put Method', 'Configure PBX settings with valid Data when Protocol is HTTP.')
        # Generate Valid IP
        ValidIP=common.GenrateValidIPString()
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Protocol': '0',
                      'ServerIP': ''+ValidIP+'',
                      'Port': '8091',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePBXUserManagementConfiguration+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
            
    def testcase_02_UpdatePBXUserManagementConfigurationwithHTTPS(self, TestCasesStatus=True):
        
        TestCaseID = '55-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBXUserManagement Settings', 'PBXUserManagement Settings Through Put Method', 'Configure PBX settings with valid Data when Protocol is HTTPs.')
        # Generate Valid IP
        ValidIP=common.GenrateValidIPString()
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Protocol': '1',
                      'ServerIP': ''+ValidIP+'',
                      'Port': '8091',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePBXUserManagementConfiguration+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
            
    def testcase_03_UpdatePBXUserManagementConfiguration(self, TestCasesStatus=True):
        
        TestCaseID = '55-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBXUserManagement Settings', 'PBXUserManagement Settings Through Put Method', 'Configure PBX settings with valid Data when Server IP is Hostname.')
        # Generate Valid IP
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Protocol': '0',
                      'ServerIP': 'Testing-PC',
                      'Port': '8091',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePBXUserManagementConfiguration+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
            
    def testcase_04_UpdatePBXUserManagementConfiguration(self, TestCasesStatus=True):
        
        TestCaseID = '55-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBXUserManagement Settings', 'PBXUserManagement Settings Through Put Method', 'Configure PBX settings with Invalid Data when Protocol is empty.')
        # Generate Valid IP
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Protocol': '',
                      'ServerIP': 'Testing-PC',
                      'Port': '8091',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePBXUserManagementConfiguration+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
    
    def testcase_05_UpdatePBXUserManagementConfiguration(self, TestCasesStatus=True):
        
        TestCaseID = '55-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBXUserManagement Settings', 'PBXUserManagement Settings Through Put Method', 'Configure PBX settings with Invalid Data when Server Ip is Empty.')
        # Generate Valid IP
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Protocol': '0',
                      'ServerIP': '',
                      'Port': '8091',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePBXUserManagementConfiguration+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
            
    def testcase_06_UpdatePBXUserManagementConfiguration(self, TestCasesStatus=True):
        
        TestCaseID = '55-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBXUserManagement Settings', 'PBXUserManagement Settings Through Put Method', 'Configure PBX settings with Invalid Data when Port is Empty.')
        # Generate Valid IP
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Protocol': '0',
                      'ServerIP': 'Testing-PC',
                      'Port': '',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePBXUserManagementConfiguration+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
            
    def testcase_07_UpdatePBXUserManagementConfiguration(self, TestCasesStatus=True):
        
        TestCaseID = '55-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBXUserManagement Settings', 'PBXUserManagement Settings Through Put Method', 'Configure PBX settings with Invalid Data when protocol value is other than 0 or 1.')
        # Generate Valid IP
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Protocol': '2',
                      'ServerIP': 'Testing-PC',
                      'Port': '8091',
                      
                     }
        # Url For Update PRS Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdatePBXUserManagementConfiguration+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End