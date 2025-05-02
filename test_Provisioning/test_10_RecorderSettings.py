'''
Created on Jul 20, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed

----------------pre requisite--------------------------------------
System setting must be configured.
Basic Recorder Settings is by default define when install the PBX Recorder.
all asic parameters are define in the  InputData.py file

------------------OutPut----------------------------
This module will be Update the Recorder Settings by Put
Request.

All the updation which is perform is Shown on the system settings page
(There is heading with the name of Recorder Settings)
 of the server administration
'''




import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from Key import config
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions

SheetName=    '10-Recorder Settings'

class test_1_UpdateRecorderSettings(TestCase):
    
    # Url For Update Recorder Settings
    UrlForUpdateRecorderSettings = '/SystemSettings/UpdateRecorderSettings'
    
    # Start Test Case No 10-01
    def testcase_01_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings When TrunkType is T1/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '0'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      'EnableClustering':'False',
                       'AssignLicensesToSites': "False"
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
    
    # Start Test Case No 10-02
    def testcase_02_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings When TrunkType is E1/1.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '1'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',

                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
            
            
    # Start Test Case No 10-03
    def testcase_03_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings with valid date format.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '1'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': '',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
    
    # Start Test Case No 10-04
    def testcase_04_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings with Invalid/incorrect date format.')
        
        # Header Parameters of Rest API
        TrunkType = '1'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': '',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-MM',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
            
    # Start Test Case No 10-05
    def testcase_05_UpdateRecorderSettings(self, TestCasesStatus=True):
    
        TestCaseID = '10-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings with Invalid Email ID.')
        
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        TrunkType = '1'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': '123abc',
                      'NetworkAdapter': '',
                      'DateFormat': 'dd-MM-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
            
    # Start Test Case No 10-06
    def testcase_06_UpdateRecorderSettings(self, TestCasesStatus=True):
    
        TestCaseID = '10-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings with trunk type Null.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        TrunkType = ''
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'dd-MM-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
            
    # Start Test Case No 10-07
    def testcase_07_UpdateRecorderSettings(self, TestCasesStatus=True):
    
        TestCaseID = '10-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings with BypassExtensionPrefixEnabled null.')
        
        # Test Case Start Time    
        starttime = time.process_time()
        # Header Parameters of Rest API
        TrunkType = '123456'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'dd-MM-yyyy',
                      'BypassExtensionPrefixEnabled': '',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
          
    # Start Test Case No 10-08
    def testcase_08_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings When TrunkType is T1/0 when invalid or non existing TrunkType.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        TrunkType = '12345'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
            
    
    # Start Test Case No 10-10
    def testcase_10_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings When TrunkType is T1/0 and ChannelOffsetEnabled is False.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '0'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'False',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
            
    # Start Test Case No 10-11
    def testcase_11_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings When TrunkType is T1/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '0'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'False',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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
            
    def testcase_12_UpdateRecorderSettings(self, TestCasesStatus=True):
        
        TestCaseID = '10-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method', 'Configure the Recorder Settings When TrunkType is T1/0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '0'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': ''+TrunkType+'',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking':'True',
                      
                     }
        # Url For Update Recorder Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateRecorderSettings+ ''
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

    # Start Test Case No 10-13
    def testcase_13_UpdateRecorderSettings(self, TestCasesStatus=True):

        TestCaseID = '10-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method',
                      'Configure the Recorder Settings When TrunkType is T1/0 with site session key')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '0'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': '' + TrunkType + '',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking': 'False',

                      }
        # Url For Update Recorder Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateRecorderSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 401:
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

    # Start Test Case No 10-14
    def testcase_14_UpdateRecorderSettings(self, TestCasesStatus=True):

        TestCaseID = '10-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Recorder Settings', 'Recorder Settings Through Put Method',
                      'Configure the Recorder Settings When TrunkType is T1/0 and EnableClustering is enabled ')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        TrunkType = '0'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'AlertEmail': 'muniba.nisar@amigo-software.com',
                      'NetworkAdapter': '',
                      'DateFormat': 'MM-dd-yyyy',
                      'BypassExtensionPrefixEnabled': 'False',
                      'TrunkType': '' + TrunkType + '',
                      'ChannelOffsetEnabled': 'True',
                      'EnableSIPRecRecordingMasking': 'False',
                      'EnableClustering': 'True',
                      'AssignLicensesToSites': "False"

                      }
        # Url For Update Recorder Settings
        URL = '' + common.Domain + '' + self.UrlForUpdateRecorderSettings + ''
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

