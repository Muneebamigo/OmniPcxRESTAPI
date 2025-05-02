'''
Created on Jul 23, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from openpyxl import load_workbook
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from test_Provisioning import test_01_SystemSettings as SS
from Key import config

SheetName=	'30-Site Settings'
class Test_1_UpdateSiteSettings(TestCase):
    
    # Url For Update Site Settings
    UrlUpdateSiteSetting='/SiteSettings/Update'
    
    # Start Test Case No 30-01
    def test_01_UpdateSiteSettings_AllowBeep_Off(self, TestCaseStatus = True):
        
        TestCaseID = '30-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where allow beep recording is off and Beep Interval is not set as -1')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '1',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '0',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',

                     }


        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    
    # Start Test Case No 30-02
    def test_02_UpdateSiteSettings_RecordingType_MP3(self, TestCaseStatus = True):
        
        TestCaseID = '30-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording Type is MP3')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate' : '0'
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
            
    # Start Test Case No 30-03        
    def test_03_UpdateSiteSettings_RecordingType_MP3WithEncryption(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '30-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording Type is MP3 and Encryption is on')
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '1',
                      'BeepInterval_Seconds': '10',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '1',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    # Start Test Case No 30-04
    def test_04_UpdateSiteSettings_TrunkROD_REC(self, TestCaseStatus = True):
        
        TestCaseID = '30-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording on Demand for trunk calls is set to Record Entire Call and RecordingType is 2')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    # Start Test Case No 30-05
    def test_05_UpdateSiteSettings_TrunkROD_RFN_WithEncryption(self, TestCaseStatus = True):
        
        TestCaseID = '30-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording on Demand for trunk calls is set to Record From Now Call and Encryption is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    # Start Test Case No 30-07
    def test_06_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '30-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Allow beep during call is on')
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '10',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',


                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False

    def test_07_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus=True):

        TestCaseID = '30-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings',
                      'Update Site Settings when recording type is GSM610')
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': 'akhtar123',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled': 'True', 'RecordSilence': 'False',
                      'IncludeSilenceIn': '0',
                      'CallPlayBack': 'True',
                      'VoiceGuideDirection': '0',
                      'SampleRate' : '0'

                      }

        # Url For Update Site Settings
        URL = '' + common.Domain + '' + self.UrlUpdateSiteSetting + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    # Start Test Case No 30-08
    def test_08_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus = True):
        
        TestCaseID = '30-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings when recording type is GSM610')
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': 'akhtar123',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True','RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    # Start Test Case No 30-09       
    def test_09_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus = True):
        
        TestCaseID = '30-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings when recording type is WAV')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '1',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': 'akhtar123',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
      
    # Start Test Case No 30-10     
    def test_10_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus = True):
        
        TestCaseID = '30-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings  With null/empty TrunkRecordOnDemandOption')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '1',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': 'akhtar123',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    # Start Test Case No 30-11     
    def test_11_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus = True):
        
        TestCaseID = '30-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings with Null / empty SIPTrunkRecordOnDemandOption')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '1',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': 'akhtar123',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
           
    # Start Test Case No 30-13
    def test_13_UpdateSiteSettings_RecordingType_MP3(self, TestCaseStatus = True):
        
        TestCaseID = '30-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording Type is MP3 when server role as secondary configured.')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    # Start Test Case No 30-14
    def test_14_UpdateSiteSettings_RecordingType_MP3(self, TestCaseStatus = True):
        
        TestCaseID = '30-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording Type is MP3 when server role as branch configured.')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    
    # Start Test Case No 30-15
    def test_15_UpdateSiteSettings_RecordingType_MP3(self, TestCaseStatus = True):
        
        TestCaseID = '30-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording Type is MP3 when Silent Monitoring  beep tone ID greater than 2000.')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '2222',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    
    # Start Test Case No 30-16
    def test_16_UpdateSiteSettings_RecordingType_MP3(self, TestCaseStatus = True):
        
        TestCaseID = '30-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording Type is MP3 when recording beep tone ID greater than 2000.')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '20001',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    # Start Test Case No 30-17
    def test_17_UpdateSiteSettings_PBXVoiceGuide_ON(self, TestCaseStatus = True):
        
        TestCaseID = '30-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where PBX Voice Guide is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '3',
                      'BeepInterval_Seconds': '-1',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '565',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    # Start Test Case No 30-18
    def test_18_UpdateSiteSettings_SIPREC_REC(self, TestCaseStatus = True):
        
        TestCaseID = '30-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording on Demand for trunk calls is set to Record Entire Call and RecordingType is 2')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '2',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                      
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    # Start Test Case No 30-04
    def test_19_UpdateSiteSettings_SIPREC_RFN(self, TestCaseStatus = True):
        
        TestCaseID = '30-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where Recording on Demand for trunk calls is set to Record Entire Call and RecordingType is 2')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '1',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                      }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    def test_20_UpdateSiteSettings_NewCall_WithoutSilence(self, TestCaseStatus = True):
        
        TestCaseID = '30-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings with Make new Call on Pause without Silence')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'True',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                      }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    def test_21_UpdateSiteSettings_NewCall_WithSilenceCurrentCall(self, TestCaseStatus = True):
        
        TestCaseID = '30-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings with Make new Call on Pause and Record Silence in Current Call')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'True',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'True',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                      }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    def test_22_UpdateSiteSettings_NewCall_WithoutSilence(self, TestCaseStatus = True):
        
        TestCaseID = '30-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings with Make new Call on Pause and Record Silence in New Call')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'True',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'True',
                      'IncludeSilenceIn':'1',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                      }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    # Start Test Case No 30-22 R2.4.0.9 Sprint 1
    def test_23_UpdateSiteSettings_VGDirection_Both(self, TestCaseStatus = True):
        
        TestCaseID = '30-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where PBX Voice Guide is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '3',
                      'BeepInterval_Seconds': '-1',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '565',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    def test_24_UpdateSiteSettings_VGDirection_Inbound(self, TestCaseStatus = True):
        
        TestCaseID = '30-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where PBX Voice Guide is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '3',
                      'BeepInterval_Seconds': '-1',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '565',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'1',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    def test_25_UpdateSiteSettings_VGDirection_Outbound(self, TestCaseStatus = True):
        
        TestCaseID = '30-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where PBX Voice Guide is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '3',
                      'BeepInterval_Seconds': '-1',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '565',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'2',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    def test_26_UpdateSiteSettings_VGDirection_Invalid(self, TestCaseStatus = True):
        
        TestCaseID = '30-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where PBX Voice Guide is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '3',
                      'BeepInterval_Seconds': '-1',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '565',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'5',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    def test_27_UpdateSiteSettings_CallPlayBack_True(self, TestCaseStatus = True):
        
        TestCaseID = '30-27'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where PBX Voice Guide is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '3',
                      'BeepInterval_Seconds': '-1',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '565',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'True',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    
    def test_28_UpdateSiteSettings_CallPlayBack_True(self, TestCaseStatus = True):
        
        TestCaseID = '30-28'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings', 'Update Site Settings Where PBX Voice Guide is enabled')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '3',
                      'BeepInterval_Seconds': '-1',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '0',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '565',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled':'True',
                      'RecordSilence':'False',
                      'IncludeSilenceIn':'0',
                      'CallPlayBack' : 'False',
                      'VoiceGuideDirection':'0',
                      'SampleRate': '0'
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateSiteSetting+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False

    def test_32_UpdateSiteSettings_TrunkROD_RFN_WithEncryption(self, TestCaseStatus=True):

        TestCaseID = '30-32'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings',
                      'Update Site Settings Where Recording on Demand for trunk calls is set to Record From Now Call and Encryption is enabled')

        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'WrapupEnabled': 'False',
                      'RecordingType': '2',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'False',
                      'EncryptionRecordingEnabled': 'False',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': '',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '15',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled': 'True',
                      'RecordSilence': 'False',
                      'IncludeSilenceIn': '0',
                      'CallPlayBack': 'True',
                      'VoiceGuideDirection': '0',
                      'SampleRate': '0'

                      }

        # Url For Update Site Settings
        URL = '' + common.Domain + '' + self.UrlUpdateSiteSetting + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
    # Test Case End
    def test_34_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus=True):

        TestCaseID = '30-34'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings',
                      'Update Site Settings when recording type is GSM610 and SIPRECVideoEnabled is enabled')
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': 'akhtar123',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled': 'True', 'RecordSilence': 'False',
                      'IncludeSilenceIn': '0',
                      'CallPlayBack': 'True',
                      'VoiceGuideDirection': '0',
                      'SIPRECVideoEnabled':'True',
                      'SampleRate': '0'

                      }

        # Url For Update Site Settings
        URL = '' + common.Domain + '' + self.UrlUpdateSiteSetting + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False

    def test_35_UpdateSiteSettings_AllowBeep_ON(self, TestCaseStatus=True):

        TestCaseID = '30-35'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Update Method of Site Settings',
                      'Update Site Settings when recording type is GSM610 and SIPRECVideoEnabled is enabled RecordingNotificationCallTypei s 0')
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'WrapupEnabled': 'False',
                      'RecordingType': '0',
                      'RecordingQuality': '0',
                      'AllowBeepDuringRecording': '0',
                      'BeepInterval_Seconds': '30',
                      'AutoResumeTime_Seconds': '99',
                      'ShowAttendantCLIDDIEnabled': 'True',
                      'EncryptRecordings': 'True',
                      'EncryptionRecordingEnabled': 'True',
                      'CreateNewRcordingAfterPause': 'False',
                      'EncryptionPassword': 'akhtar123',
                      'SIPExtensionLength': '4',
                      'TrunkRecordOnDemandOption': '2',
                      'SIPTrunkRecordOnDemandOption': '0',
                      'AllowBeepDuringSilentMonitoring': '0',
                      'SilentMonitorBeepInterval': '30',
                      'RecordingBeepToneID': '22',
                      'SilentMonitoringBeepToneID': '22',
                      'SIPRecRecordOnDemandOption': '0',
                      'CCDAgentStatusEnabled': 'True',
                      'ShowCallingPartyNameEnabled': 'True', 'RecordSilence': 'False',
                      'IncludeSilenceIn': '0',
                      'CallPlayBack': 'True',
                      'VoiceGuideDirection': '0',
                      'SIPRECVideoEnabled': 'True',
                      'RecordingNotificationCallType': '0',
                      'SampleRate': '0'

                      }

        # Url For Update Site Settings
        URL = '' + common.Domain + '' + self.UrlUpdateSiteSetting + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False



           
class Test_2_GetSiteSettings(TestCase):
    
    # Url For Get Site Settings
    UrlGetSiteSettings='/SiteSettings/Get'
    
    # Start Test Case No 30-06
    def test_07_GetSystemSettings(self, TestCaseStatus=True):
        
        TestCaseID = '30-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Get Method of Site Settings', 'Getting Site Settings')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':''
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlGetSiteSettings+''
        response = requests.get(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    
    # Start Test Case No 30-12
    def test_12_GetSystemSettings(self, TestCaseStatus=True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '30-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Site Settings', 'Calling Get Method of Site Settings', 'Getting Site Settings with Non Existing/Invalid Site Code')
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'123456'
                      
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlGetSiteSettings+''
        response = requests.get(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
    # Test Case End
    