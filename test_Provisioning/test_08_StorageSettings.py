'''
Created on Jul 19, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed


----------------pre requisite--------------------------------------
System setting must be configured.
Basic Storage setting is by default define when install the PBX Recorder.

------------------OutPut----------------------------
This module will be Update the Storage settings by Put
Request.
All the updation which is perform is Shown on the Storage settings page
 of the server administration
'''

import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from Key import config
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions

SheetName=    '8-Storage Settings'

class test_1_UpdateStorageSettings(TestCase):
    
    # Url For Update Storage Settings
    UrlForUpdateStorageSettings = '/SystemSettings/UpdateStorageSettings'
    
    # Start Test Case No 08-01
    def testcase_01_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Master/slave Mode is disabled and Play Archived calls are disabled.')
        
        # System Settings Function calling
        # SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        # SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'False',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
            
    # Start Test Case No 08-02                
    def testcase_02_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Master Mode is enabled/0 and Play Archived calls are disabled.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'True',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
    
    # Start Test Case No 08-03
    def testcase_03_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Slave Mode is enabled/1 and Play Archived calls are disabled.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'True',
                      'MasterSlaveMode': '1',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
    
    # Start Test Case No 08-04
    def testcase_04_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Master/slave Mode is disabled and Play Archived calls are Enabled.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'True',
                      'MasterSlaveModeEnabled': 'False',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
    
    # Start Test Case No 08-05                
    def testcase_05_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Storage Paths are empty.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = ''
        ProcessingStoragePath = ''
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'False',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
            
    # Start Test Case No 08-06
    def testcase_06_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Master/slave Mode is Enabled and Play Archived calls are disabled and PlayArchiveCallsEnabled is Null/Empty.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': '',
                      'MasterSlaveModeEnabled': 'True',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
            
    # Start Test Case No 08-07
    def testcase_07_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Master/slave Mode is disabled and Play Archived calls are disabled and invalid AudioFileStoragePath format.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = '123#$abc10.94ajhsd'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'False',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
            
    # Start Test Case No 08-08
    def testcase_08_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Configure the Storage Settings when Master/slave Mode is disabled and invalid ProcessingStoragePath format.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = '123#$abc10.94ajhsd'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'False',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
            
            
    def testcase_09_UpdateStorageSettings(self, TestCasesStatus=True):
        
        TestCaseID = '08-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method', 'Update Storage Settings with Site Session Key')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'AudioFileStoragePath': ''+AudioFileStoragePath+'',
                      'ProcessingStoragePath': ''+ProcessingStoragePath+'',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'False',
                      'MasterSlaveMode': '0',
                      
                     }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            TestCasesStatus = False
            # Test Case End

    def testcase_10_UpdateStorageSettings(self, TestCasesStatus=True):

        TestCaseID = '08-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Storage Settings', 'Storage Settings Through Put Method',
                      'Configure the Storage Settings when Master/slave Mode is disabled and Play Archived calls are disabled,MasterSlaveMode is empty')

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_02_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        AudioFileStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        ProcessingStoragePath = 'C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\OmniPCXRecord'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'AudioFileStoragePath': '' + AudioFileStoragePath + '',
                      'ProcessingStoragePath': '' + ProcessingStoragePath + '',
                      'ArchiveFileStoragePath': '',
                      'PlayArchiveCallsEnabled': 'False',
                      'MasterSlaveModeEnabled': 'False',
                      'MasterSlaveMode': '',

                      }
        # Url For Update Storage Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateStorageSettings + ''
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
            