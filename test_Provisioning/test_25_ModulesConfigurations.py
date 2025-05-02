'''
Created on Jul 30, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config
SheetName=	'25-Modules'

class test_2_Get_Modules(TestCase):
    
    # URL for Get Event Modules
    UrlToGetEventModules = '/Event/GetModule'
    
    # Start Test Case No 25-01
    def testcase_01_Get_Modules_Primary(self, TestCasesStatus=True):
        
        TestCaseID = '25-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Modules' , 'Using Get Event Module Method' , 'Get Event Module at Primary ')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    }
        
        # URL for Get Event Modules
        URL = ''+common.Domain+''+self.UrlToGetEventModules
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
    
    # Start Test Case No 25-02        
    def testcase_02_Get_Modules_Branch(self, TestCasesStatus=True):
        
        TestCaseID = '25-02'
        common = CF.CommonFunctions()
        # Calling Common Functions
        common.Header('Modules' , 'Using Get Event Module Method' , 'Get Event Module at Branch ')
        
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    }
        
        # URL for Get Event Modules
        URL = ''+common.Domain+''+self.UrlToGetEventModules
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