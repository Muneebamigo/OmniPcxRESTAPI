'''
Created on Jul 20, 2018

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
from Key import config

SheetName=	'11-Autentication Settings'
class UpdateAuthenticationSettings(TestCase):
    # Url For Update Authentication Settings
    UrlForUpdateAuthenticationSettings = '/SystemSettings/UpdateAuthenticationSettings'
    # Start Test Case No 11-01
    def testcase_01_UpdateAuthenticationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '11-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings When Authentication Type is Authentication through OmniPCX Record database/0 and ActiveDirectoryCriteria is Include all default/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        AuthenticationType = '0'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': '',
                      'RadiusSecretKey': '',
                      'RadiusServerIPSecondary': '',
                      'RadiusSecretKeySecondary': '',
                      'EnableContainerUser':'False',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-02   
    def testcase_02_UpdateAuthenticationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '11-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings When Authentication through Active Directory interface/1 and ActiveDirectoryCriteria is Include all default/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ActiveDirectoryDomain = 'ghostsoftware.local'
        ActiveDirectoryUsername = 'ahsan.rehman'
        ActiveDirectoryPassword = 'Abc123*'
        AuthenticationType = '1'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': ''+ActiveDirectoryDomain+'',
                      'ActiveDirectoryUsername': ''+ActiveDirectoryUsername+'',
                      'ActiveDirectoryPassword': ''+ActiveDirectoryPassword+'',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'False',
                      'RadiusServerIP': '',
                      'RadiusSecretKey': '',
                      'RadiusServerIPSecondary': '',
                      'RadiusSecretKeySecondary': '',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-03   
    def testcase_03_UpdateAuthenticationSettings(self, TestCasesStatus=True):
       
        TestCaseID = '11-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings When Authentication through OmniPCXRecord and Active Directory interface/2 and ActiveDirectoryCriteria is Include all default/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ActiveDirectoryDomain = 'ghostsoftware.local'
        ActiveDirectoryUsername = 'ahsan.rehman'
        ActiveDirectoryPassword = 'Abc123*'
        AuthenticationType = '2'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': ''+ActiveDirectoryDomain+'',
                      'ActiveDirectoryUsername': ''+ActiveDirectoryUsername+'',
                      'ActiveDirectoryPassword': ''+ActiveDirectoryPassword+'',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'False',
                      'RadiusServerIP': '',
                      'RadiusSecretKey': '',
                      'RadiusServerIPSecondary': '',
                      'RadiusSecretKeySecondary': '',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-04
    def testcase_04_UpdateAuthenticationSettings(self, TestCasesStatus=True):

        TestCaseID = '11-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings when Authentication through Radius Server/3 and ActiveDirectoryCriteria id default/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        RadiusServerIP = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKey = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        RadiusServerIPSecondary = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKeySecondary = common.GenrateSimpleStringLimit10()
        AuthenticationType = '3'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'False',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': ''+RadiusServerIP+'',
                      'RadiusSecretKey': ''+RadiusSecretKey+'',
                      'RadiusServerIPSecondary': ''+RadiusServerIPSecondary+'',
                      'RadiusSecretKeySecondary': ''+RadiusSecretKeySecondary+'',
                      'EnableContainerUser':'False',


                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-05  
    def testcase_05_UpdateAuthenticationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '11-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings when authentication type is Radius Server and ActiveDirectoryCriteria is Include all containers/1.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        RadiusServerIP = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKey = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        RadiusServerIPSecondary = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKeySecondary = common.GenrateSimpleStringLimit10()
        AuthenticationType = '3'
        ActiveDirectoryCriteria = '1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': ''+RadiusServerIP+'',
                      'RadiusSecretKey': ''+RadiusSecretKey+'',
                      'RadiusServerIPSecondary': ''+RadiusServerIPSecondary+'',
                      'RadiusSecretKeySecondary': ''+RadiusSecretKeySecondary+'',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-06 
    def testcase_06_UpdateAuthenticationSettings(self, TestCasesStatus=True):
       
        TestCaseID = '11-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings when authentication type is Radius Server and ActiveDirectoryCriteria is Specific container/2.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        RadiusServerIP = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKey = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        RadiusServerIPSecondary = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKeySecondary = common.GenrateSimpleStringLimit10()
        AuthenticationType = '3'
        ActiveDirectoryCriteria = '2'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': ''+RadiusServerIP+'',
                      'RadiusSecretKey': ''+RadiusSecretKey+'',
                      'RadiusServerIPSecondary': ''+RadiusServerIPSecondary+'',
                      'RadiusSecretKeySecondary': ''+RadiusSecretKeySecondary+'',
                      'EnableContainerUser':'False',

                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-07  
    def testcase_07_UpdateAuthenticationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '11-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings  with invalid/non existing ActiveDirectoryCriteria.')
        # Generate Valid IP
        RadiusServerIP = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKey = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        RadiusServerIPSecondary = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKeySecondary = common.GenrateSimpleStringLimit10()
        AuthenticationType = '3'
        ActiveDirectoryCriteria = '123456'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': ''+RadiusServerIP+'',
                      'RadiusSecretKey': ''+RadiusSecretKey+'',
                      'RadiusServerIPSecondary': ''+RadiusServerIPSecondary+'',
                      'RadiusSecretKeySecondary': ''+RadiusSecretKeySecondary+'',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-08
    def testcase_08_UpdateAuthenticationSettings(self, TestCasesStatus=True):
       
        TestCaseID = '11-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings  with authentication type is Null/empty.')
        # Generate Valid IP
        RadiusServerIP = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKey = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        RadiusServerIPSecondary = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKeySecondary = common.GenrateSimpleStringLimit10()
        AuthenticationType = ''
        ActiveDirectoryCriteria = '2'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': ''+RadiusServerIP+'',
                      'RadiusSecretKey': ''+RadiusSecretKey+'',
                      'RadiusServerIPSecondary': ''+RadiusServerIPSecondary+'',
                      'RadiusSecretKeySecondary': ''+RadiusSecretKeySecondary+'',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-09
    def testcase_09_UpdateAuthenticationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '11-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings When Authentication through Active Directory interface/1 and ActiveDirectoryCriteria is Include all default/0 and AuthenticationType 1 and Null/invalid password.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ActiveDirectoryDomain = ''
        ActiveDirectoryUsername = 'ahsan.rehman'
        ActiveDirectoryPassword = 'abc123abc123'
        AuthenticationType = '1'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': ''+ActiveDirectoryDomain+'',
                      'ActiveDirectoryUsername': ''+ActiveDirectoryUsername+'',
                      'ActiveDirectoryPassword': ''+ActiveDirectoryPassword+'',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'False',
                      'RadiusServerIP': '',
                      'RadiusSecretKey': '',
                      'RadiusServerIPSecondary': '',
                      'RadiusSecretKeySecondary': '',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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
            
    # Start Test Case No 11-10
    def testcase_10_UpdateAuthenticationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '11-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings When Authentication Type is Authentication through OmniPCX Record database/0 and ActiveDirectoryCriteria is Include all default/0 when server role configured as secondary.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        AuthenticationType = '0'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': '',
                      'RadiusSecretKey': '',
                      'RadiusServerIPSecondary': '',
                      'RadiusSecretKeySecondary': '',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
            
    # Start Test Case No 11-11
    def testcase_11_UpdateAuthenticationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '11-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings When Authentication Type is Authentication through OmniPCX Record database/0 and ActiveDirectoryCriteria is Include all default/0 when server role configured as branch.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        AuthenticationType = '0'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': '',
                      'RadiusSecretKey': '',
                      'RadiusServerIPSecondary': '',
                      'RadiusSecretKeySecondary': '',
                      'EnableContainerUser':'False',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End
            
    def testcase_12_UpdateAuthenticationSettings(self, TestCasesStatus=True):
       
        TestCaseID = '11-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method', 'Configure Update Authentication Settings When Authentication through OmniPCXRecord and Active Directory interface/2 and ActiveDirectoryCriteria is Include all default/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ActiveDirectoryDomain = 'ghostsoftware.local'
        ActiveDirectoryUsername = 'ahsan.rehman'
        ActiveDirectoryPassword = 'Abc123*'
        AuthenticationType = '2'
        ActiveDirectoryCriteria = '1' #ActiveDirectoryCriteria = '2'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AuthenticationType': ''+AuthenticationType+'',
                      'ActiveDirectoryAuthenticationEnabled': 'True',
                      'ActiveDirectoryDomain': ''+ActiveDirectoryDomain+'',
                      'ActiveDirectoryUsername': ''+ActiveDirectoryUsername+'',
                      'ActiveDirectoryPassword': ''+ActiveDirectoryPassword+'',
                      'ActiveDirectoryCriteria': ''+ActiveDirectoryCriteria+'',
                      'ActiveDirectoryContainer': '', #OU=Development / OU=Development1
                      'RadiusAuthenticationEnabled': 'False',
                      'RadiusServerIP': '',
                      'RadiusSecretKey': '',
                      'RadiusServerIPSecondary': '',
                      'RadiusSecretKeySecondary': '',
                      'EnableContainerUser':'True',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateAuthenticationSettings+ ''
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

        # Start Test Case No 11-04

    def testcase_14_UpdateAuthenticationSettings(self, TestCasesStatus=True):

        TestCaseID = '11-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method',
                      'Configure Update Authentication Settings when Authentication through Radius Server/3 '
                      'and ActiveDirectoryCriteria id default/0.PrimaryRadiusServerPort is 1812')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        RadiusServerIP = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKey = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        RadiusServerIPSecondary = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKeySecondary = common.GenrateSimpleStringLimit10()
        AuthenticationType = '3'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'AuthenticationType': '' + AuthenticationType + '',
                      'ActiveDirectoryAuthenticationEnabled': 'False',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': '' + ActiveDirectoryCriteria + '',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': '' + RadiusServerIP + '',
                      'RadiusSecretKey': '' + RadiusSecretKey + '',
                      'RadiusServerIPSecondary': '' + RadiusServerIPSecondary + '',
                      'RadiusSecretKeySecondary': '' + RadiusSecretKeySecondary + '',
                      'EnableContainerUser': '',
                      'PrimaryRadiusServerPort': '1812',
                      'SecondaryRadiusServerPort': '7621'

                      }
        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateAuthenticationSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End

    def testcase_15_UpdateAuthenticationSettings(self, TestCasesStatus=True):

        TestCaseID = '11-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Authentication Settings', 'Authentication Settings Through Put Method',
                      'Configure Update Authentication Settings when Authentication through Radius Server/3 and'
                      ' ActiveDirectoryCriteria id default/0. and PrimaryRadiusServerPort is empty')
        # # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        RadiusServerIP = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKey = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        RadiusServerIPSecondary = common.GenrateValidIPString()
        # Generate Simple Character String Limit 10 Characters
        RadiusSecretKeySecondary = common.GenrateSimpleStringLimit10()
        AuthenticationType = '3'
        ActiveDirectoryCriteria = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'AuthenticationType': '' + AuthenticationType + '',
                      'ActiveDirectoryAuthenticationEnabled': 'False',
                      'ActiveDirectoryDomain': '',
                      'ActiveDirectoryUsername': '',
                      'ActiveDirectoryPassword': '',
                      'ActiveDirectoryCriteria': '' + ActiveDirectoryCriteria + '',
                      'ActiveDirectoryContainer': '',
                      'RadiusAuthenticationEnabled': 'True',
                      'RadiusServerIP': '' + RadiusServerIP + '',
                      'RadiusSecretKey': '' + RadiusSecretKey + '',
                      'RadiusServerIPSecondary': '' + RadiusServerIPSecondary + '',
                      'RadiusSecretKeySecondary': '' + RadiusSecretKeySecondary + '',
                      'EnableContainerUser': 'False',
                      'PrimaryRadiusServerPort': '',
                      'SecondaryRadiusServerPort': ''

                      }
        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateAuthenticationSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
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