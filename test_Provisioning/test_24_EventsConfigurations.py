'''
Created on Jul 30, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests, random
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config
SheetName=	'24-Event'

class test_1_Get_Events(TestCase):
    
    # Url For Get Events
    UrlToGetEvents = '/Event/Get/'
    
    # Start Test Case No 24-01
    def testcase_01_Get_Events_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '24-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Primary when EventSeverityType is 0.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '0',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End
    
    # Start Test Case No 24-02
    def testcase_02_Get_Events_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '24-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Primary  when EventSeverityType is 1.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '1',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            
         
    # Start Test Case No 24-03
    def testcase_03_Get_Events_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '24-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Primary when EventSeverityType is 2.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '2',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
          
          
    # Start Test Case No 24-04
    def testcase_04_Get_Events_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '24-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Primary when EventSeverityType is 3.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '3',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            
           
    # Start Test Case No 24-05
    def testcase_05_Get_Events_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '24-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Primary when EventSeverityType is 4.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '4',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
    
    
    # Start Test Case No 24-06
    def testcase_06_Get_Events_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '24-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Primary with invalid or non existing EventSeverityType.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '123456',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            
            
    # Start Test Case No 24-07
    def testcase_07_Get_Events_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '24-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Primary when EventSeverityType is empty/null.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
    
    
    # Start Test Case No 24-08    
    def testcase_08_Get_Events_Branch(self, TestCasesStatus=True):
        
        TestCaseID = '24-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Get Event Method' , 'Get Events at Branch when EventSeverityType is 0.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'EventSeverityType': '0',
                    
                    }
        
        # Url For Get Events
        URL = ''+common.Domain+''+self.UrlToGetEvents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End
            
            
            
class test_2_Update_Events(TestCase):
    
    # Url For Update Events
    UrlUpdateEvents = '/Event/Update/'
    
    # Start Test Case No 24-09
    def testcase_01_Update_Events(self, TestCasesStatus=True):
        
        TestCaseID = '24-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Put Method Update Events ' , 'Update Events in system with all valid data.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID = '287'
        NoAudioInCallThreshold = str(random.randint(1 , 59))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'ID': ''+ID+'',
                    'NoAudioInCallThreshold': ''+NoAudioInCallThreshold+'',
                    
                    }
        
        # Url For Update Events
        URL = ''+common.Domain+''+self.UrlUpdateEvents
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End
            
    
    # Start Test Case No 24-10
    def testcase_02_Update_Events(self, TestCasesStatus=True):
        
        TestCaseID = '24-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Put Method Update Events ' , 'Update Events in system with empty/null ID.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID = ''
        NoAudioInCallThreshold = str(random.randint(1 , 59))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'ID': ''+ID+'',
                    'NoAudioInCallThreshold': ''+NoAudioInCallThreshold+'',
                    
                    }
        
        # Url For Update Events
        URL = ''+common.Domain+''+self.UrlUpdateEvents
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End
            
            
    # Start Test Case No 24-11
    def testcase_03_Update_Events(self, TestCasesStatus=True):
        
        TestCaseID = '24-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Events ' , 'Using Put Method Update Events ' , 'Update Events in system with empty/null NoAudioInCallThreshold.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID = str(random.randint(1 , 99))
        NoAudioInCallThreshold = ''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'ID': ''+ID+'',
                    'NoAudioInCallThreshold': ''+NoAudioInCallThreshold+'',
                    
                    }
        
        # Url For Update Events
        URL = ''+common.Domain+''+self.UrlUpdateEvents
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End