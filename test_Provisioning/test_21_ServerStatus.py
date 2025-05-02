'''
Created on Jul 26, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config

SheetName=	'21-Server Status'
class test_1_GetServerStatus(TestCase):
    
    # Url For Get Server Status
    UrlForGetServerStatus = '/SystemSettings/ServerStatus/'
    
    # Start Test Case No 21-01
    def testcase_01_GetServerStatus(self, TestCasesStatus=True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '21-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Status' , 'Using Get Method' , 'Get Server Status Details.')
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      
                    }
        
        # Url For Get Server Status
        URL = ''+common.Domain+''+self.UrlForGetServerStatus+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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