'''
Created on Aug 10, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time,requests, random

from requests.utils import from_key_val_list

from Settings import CommonFunctions as CF
from unittest import TestCase
from openpyxl import load_workbook
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config

SheetName=	'49-Email Template'

class test_1_UpdateEmailTemplate(TestCase):
    # Url For UpdateSMTP Settings 
    UrlForUpdateEmailTemplate = '/EmailTemplate/Update'
    # Start Test Case No 49-01    
    def testcase_01_UpdateEmailTemplate(self, TestCasesStatus=True):
        
        TestCaseID = '49-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Email Template', 'Email Template Through Put Method', 'Update Email Template with valid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID=str(random.randint(1 , 12))
        Subject='This is Dummy Subject by Testing'
        Body='This is Dummy Mail Body by Testing'
        IsEnable='True'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+ID+'',
                      'Subject': ''+Subject+'',
                      'Body': ''+Body+'',
                      'IsEnable': ''+IsEnable+'',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateEmailTemplate+ ''
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
          
    # Start Test Case No 49-02
    def testcase_02_UpdateEmailTemplate(self, TestCasesStatus=True):
        
        TestCaseID = '49-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Email Template', 'Email Template Through Put Method', 'Update Email Template with Null Mandatory data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID=str(random.randint(1 , 12))
        Subject=''
        Body=''
        IsEnable='True'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+ID+'',
                      'Subject': ''+Subject+'',
                      'Body': ''+Body+'',
                      'IsEnable': ''+IsEnable+'',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateEmailTemplate+ ''
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
            
    # Start Test Case No 49-03
    def testcase_03_UpdateEmailTemplate(self, TestCasesStatus=True):
       
        TestCaseID = '49-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Email Template', 'Email Template Through Put Method', 'Update Email Template with invalid ID.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID='123456'
        Subject='This is Dummy Subject by Testing'
        Body='This is Dummy Mail Body by Testing'
        IsEnable='True'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+ID+'',
                      'Subject': ''+Subject+'',
                      'Body': ''+Body+'',
                      'IsEnable': ''+IsEnable+'',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateEmailTemplate+ ''
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
            

class test_2_GetEmailTemplate(TestCase):
    
    # URL For Get Email Template
    UrlForGetEmailTemplate='/EmailTemplate/Get/'
    
    # Start Test Case No 49-04
    def testcase_04_UpdateEmailTemplate(self, TestCasesStatus=True):
       
        TestCaseID = '49-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Email Template', 'Email Template Through Get Method', 'Get All Email Template with valid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+ID+'',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForGetEmailTemplate+ ''+ID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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
            
    # Start Test Case No 49-05
    def testcase_05_UpdateEmailTemplate(self, TestCasesStatus=True):
        TestCaseID = '49-05'
        common = CF.CommonFunctions()
        common.Header('Email Template', 'Email Template Through Get Method',
                      'Get a single Email Template with valid ID.')

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        ID = str(random.randint(1, 10))
        starttime = time.process_time()

        # Header Parameters of Rest API
        Parameters = {
            'AuthToken': config.sessionkey,
            'AuthUser': config.auth_user,
            'ID': ID,
        }

        # URL
        URL = f'{common.Domain}{self.UrlForGetEmailTemplate}{ID}'
        print("Request URL:", URL)
        print("Request Headers:", Parameters)

        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        resp = response.json()
        print("API Response:", resp)

        # Response Code Verification
        if TestCasesStatus:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    print(
                        f"Failed with Response Code: {resp['ResponseCode']}, Description: {resp['ResponseDescription']}")
                    assert False, f"Expected Response Code 200, but got {resp['ResponseCode']}"
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End
            
    # Start Test Case No 49-06
    def testcase_06_UpdateEmailTemplate(self, TestCasesStatus=True):
        
        TestCaseID = '49-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Email Template', 'Email Template Through Get Method', 'Get a single Email Template with invalid ID.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID='22568'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+ID+'',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForGetEmailTemplate+ ''+ID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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