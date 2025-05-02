'''
Created on Apr 29, 2019

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

SheetName=	'53-Incident Settings'

class test_1_UpdateIncidentSettings(TestCase):
    
    # Url For Update Incident Settings
    UrlToUpdateIncidentSettings = '/SystemSettings/UpdateIncidentSettings/'
    
    # Start Test Case No 53-01
    def testcase_01_UpdateIncidentSettings(self, TestCasesStatus=True):
        
        TestCaseID = '53-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Incident Settings ' , 'Using PUT Method Update Incident Settings' , 'Update  Incident Settings in system with all valid data.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        IgnoreEmailAndTrapsOlderThan = str(random.randint(1 , 48))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'IgnoreEmailAndTrapsOlderThan': ''+IgnoreEmailAndTrapsOlderThan+'',
                    
                    }
        
        # Url For Update Incident Settings
        URL = ''+common.Domain+''+self.UrlToUpdateIncidentSettings
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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
            
            
    # Start Test Case No 53-02
    def testcase_02_UpdateIncidentSettings(self, TestCasesStatus=True):
        
        TestCaseID = '53-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Incident Settings ' , 'Using PUT Method Update Incident Settings' , 'Update  Incident Settings in system with empty/null IgnoreEmailAndTrapsOlderThan.')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        IgnoreEmailAndTrapsOlderThan = ''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'IgnoreEmailAndTrapsOlderThan': ''+IgnoreEmailAndTrapsOlderThan+'',
                    
                    }
        
        # Url For Update Incident Settings
        URL = ''+common.Domain+''+self.UrlToUpdateIncidentSettings
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
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