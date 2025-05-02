import time, requests, random
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
from InputDataFiles import SeleniumConfigration as SC
from test_Provisioning import test_02_PBXConfiguration as pbxconfigurationFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from test_Provisioning import test_04_DeviceConfigurations as devicefunctions
import os
from InputDataFiles import InputData

class test_1_Unittest(TestCase):
    

    
    # Calling Input Data File
    ssinputdata = InputData.InputData()
    # Url for Get System Settings
    UrlForGetSystemSettings_GetNotificationSettings = '/SystemSettings/GetNotificationSettings/'
    
    # Start Test Case No 01-13
    def testcase_21_GetSystemSettings_NotificationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Get Method System notification Settings' , 'Get System Notification Settings with valid data')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':''+common.authkey_server()+'',
                      'AuthUser':''+common.authuser+'',
                      
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForGetSystemSettings_GetNotificationSettings+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        print(resp)
        #showcode = str(resp['ResponseCode'])
        
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
                print(" ")
                #common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            # Test Case End