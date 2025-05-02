'''
Created on Jul 16, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed

----------------pre requisite--------------------------------------
System setting must be configured.
Basic Recording Transfer Settings is by default define when install the PBX Recorder.
1-BranchTransferURL
2-BranchTransferUsername
3-BranchTransferPassword
above mention three parameters is define in the  InputData.py file

------------------OutPut----------------------------
This module will be Update the Recording Transfer Settings by Put
Request.

All the updation which is perform is Shown on the system settings page
(There is heading with the name of Recording Transfer Settings)
 of the server administration
'''

import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase

import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from Key import config
from InputDataFiles import InputData
SheetName=    '7-Recording Transfer Settings'

class UpdateRecordingTransderSettings(TestCase):
    
    # Calling Input Data File
    ssinputdata = InputData.InputData()
    # Url For Update Transfer Settings
    UrlUpdateTransferSettings = '/SystemSettings/UpdateRecordingTransferSettings'
    
    # Start Test Case No 07-01
    def testcase_01_UpdateSettings_FTP(self):
        
        TestCaseID = '07-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method', 'Update Recording Transfer Settings when Transfer Type is FTP ')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TransferTypeUrl = '0'
        TrabsferUrl = self.ssinputdata.BranchTransferURL
        TransferUsername = self.ssinputdata.BranchTransferUsername
        TransferPassword = self.ssinputdata.BranchTransferPassword
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ ''
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
                    
    # Start Test Case No 07-02
    def testcase_02_UpdateSettings_FTP(self):
        
        TestCaseID = '07-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method', 'Update Recording Transfer Settings when Transfer Type is Secure FTP ')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TransferTypeUrl = '1'
        TrabsferUrl = self.ssinputdata.BranchTransferURL
        TransferUsername = self.ssinputdata.BranchTransferUsername
        TransferPassword = self.ssinputdata.BranchTransferPassword
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
    
    
    # Start Test Case No 07-03
    def testcase_03_UpdateSettings_Network(self):
        
        TestCaseID = '07-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer Using Put Method', 'Update Recording Transfer Settings when Transfer Type is Network ')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TransferTypeUrlLocal = '2'
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' +TransferTypeUrlLocal+ '',
                      'TransferURL': "\\\\172.20.0.2\\Share Data backup folders\\Quality Assurance",
                      'TransferUsername': '',
                      'TransferPassword': '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
          
    # Start Test Case No 07-04
    def testcase_04_UpdateSettings_Local(self):
        
        TestCaseID = '07-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer Using Put Method', 'Update Recording Transfer Settings when Transfer Type is Local with valid path')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TransferTypeUrlLocal = '3'
        TransferURLLocal  = 'C:\\'
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' +TransferTypeUrlLocal+ '',
                      'TransferURL': '' +TransferURLLocal+ '',
                      'TransferUsername': '',
                      'TransferPassword': '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
    
    # Start Test Case No 07-05
    def testcase_05_UpdateSettings_Loacl(self):
        
        TestCaseID = '07-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer Using Put Method', 'Update Recording Transfer Settings when Transfer Type is Local with invalid Path ')
        
        # Header Parameters of Rest API
        TransferTypeUrlLocal = '3'
        TransferURLLocal  = '\\172.20.5.99::'
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' +TransferTypeUrlLocal+ '',
                      'TransferURL': '' +TransferURLLocal+ '',
                      'TransferUsername': '',
                      'TransferPassword': '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End   
    
    # Start Test Case No 07-06
    def testcase_06_UpdateSettings_FTP(self):
        
        TestCaseID = '07-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method', 'Update Recording Transfer Settings with invalid/Non Existing TransferURLType.')
        
        # Header Parameters of Rest API
        TransferTypeUrl = '12345'
        TrabsferUrl = self.ssinputdata.BranchTransferURL
        TransferUsername = self.ssinputdata.BranchTransferUsername
        TransferPassword = self.ssinputdata.BranchTransferPassword
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
                    
    # Start Test Case No 07-07
    def testcase_07_UpdateSettings_FTP(self):
        
        TestCaseID = '07-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method', 'Update Recording Transfer Settings with TransferURLType 0 and TansferUsername null/invalid.')
        
        # Header Parameters of Rest API
        TransferTypeUrl = '0'
        TrabsferUrl = self.ssinputdata.BranchTransferURL
        TransferUsername = 'abc123abc123'
        TransferPassword = self.ssinputdata.BranchTransferPassword
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
                    
    # Start Test Case No 07-08
    def testcase_08_UpdateSettings_FTP(self):
        
        TestCaseID = '07-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method', 'Update Recording Transfer Settings with TransferURLType 0 and TansferPassword invalid/null.')
        
        # Header Parameters of Rest API
        TransferTypeUrl = '0'
        TrabsferUrl = self.ssinputdata.BranchTransferURL
        TransferUsername = self.ssinputdata.BranchTransferUsername
        TransferPassword = 'abc123abc123abc'
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
                    
    # Start Test Case No 07-09
    def testcase_09_UpdateSettings_FTP(self):
        
        TestCaseID = '07-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method', 'Update Recording Transfer Settings when server role as secondary ')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TransferTypeUrl = '0'
        TrabsferUrl = self.ssinputdata.BranchTransferURL
        TransferUsername = self.ssinputdata.BranchTransferUsername
        TransferPassword = self.ssinputdata.BranchTransferPassword
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
                    # Test Case End


    def testcase_10_UpdateSettings_FTP(self):
        
        TestCaseID = '07-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method', 'Update Settings with Site Session Key')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TransferTypeUrl = '0'
        TrabsferUrl = self.ssinputdata.BranchTransferURL
        TransferUsername = self.ssinputdata.BranchTransferUsername
        TransferPassword = self.ssinputdata.BranchTransferPassword
        ScheduleInterval= '100000'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval+ '',
                      
                     }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
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
                    status = 'Failed'
                    assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

        # Start Test Case No 07-011

    def testcase_11_UpdateSettings_FTP_invalid_branchTrnsferURL(self):

        TestCaseID = '07-011'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recording Transfer Settings ', 'Updating Recording Transfer using Put Method',
                      'Update Recording Transfer Settings when Transfer Type is FTP with Invalid BranchTransferURL ')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TransferTypeUrl = '0'
        TrabsferUrl =""
        TransferUsername = self.ssinputdata.BranchTransferUsername
        TransferPassword = self.ssinputdata.BranchTransferPassword
        ScheduleInterval = '100000'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'TransferURLType': '' + TransferTypeUrl + '',
                      'TransferURL': '' + TrabsferUrl + '',
                      'TransferUsername': '' + TransferUsername + '',
                      'TransferPassword': '' + TransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'UploadTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'DownloadScheduleIntervalMiliSeconds': '' + ScheduleInterval + '',

                      }
        # Url For Update Transfer Settings
        URL = '' + common.Domain + '' + self.UrlUpdateTransferSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
            # Test Case End
    