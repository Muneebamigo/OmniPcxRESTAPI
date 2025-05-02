'''
Created on Jul 20, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from openpyxl import load_workbook
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from InputDataFiles import InputData
from Key import config

SheetName=	'13-SMTP Settings'
class UpdateSMTPSettings(TestCase):
    # Call input data file
    ssinputdata = InputData.InputData()
    # Url For UpdateSMTP Settings 
    UrlForUpdateSMTPSettings = '/SystemSettings/UpdateSMTPSettings'
    # Start Test Case No 13-01
    def testcase_01_UpdateSMTPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '13-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with Valid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+self.ssinputdata.SMTPServerName+'',
                      'SMTPUsername': ''+self.ssinputdata.SMTPUsername+'',
                      'SMTPPassword': ''+self.ssinputdata.SMTPPassword+'',
                      'SenderEmailAddress': ''+self.ssinputdata.SenderEmailAddress+'',
                      'Port':'587',
                      'SMTPTLSEnabled':'True'

                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
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
            
    # Start Test Case No 13-02
    def testcase_02_UpdateSMTPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '13-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with InValid Email format.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        SMTPServer='auth.smtp.1and1.co.uk'
        SMTPUsername='qa-opr@amigo-software.com'
        SMTPPassword='OPRqa@2017'
        SenderEmailAddress='abc123abc'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+SMTPServer+'',
                      'SMTPUsername': ''+SMTPUsername+'',
                      'SMTPPassword': ''+SMTPPassword+'',
                      'SenderEmailAddress': ''+SenderEmailAddress+'',
                      'Port':'565',
                      
                     }
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
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
            
    # Start Test Case No 13-03
    def testcase_03_UpdateSMTPSettings(self, TestCasesStatus=True):
      
        TestCaseID = '13-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with NULL SMTPServer.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': '',
                      'SMTPUsername': ''+self.ssinputdata.SMTPUsername+'',
                      'SMTPPassword': ''+self.ssinputdata.SMTPPassword+'',
                      'SenderEmailAddress': ''+self.ssinputdata.SenderEmailAddress+'',
                      'Port':'565',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
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
    
    # Start Test Case No 13-04
    def testcase_04_UpdateSMTPSettings(self, TestCasesStatus=True):
      
        TestCaseID = '13-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with NULL SenderEmailAddress.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+self.ssinputdata.SMTPServerName+'',
                      'SMTPUsername': ''+self.ssinputdata.SMTPUsername+'',
                      'SMTPPassword': ''+self.ssinputdata.SMTPPassword+'',
                      'SenderEmailAddress': '',
                      'Port':'565',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
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
    
    # Start Test Case No 13-05
    def testcase_05_UpdateSMTPSettings(self, TestCasesStatus=True):
      
        TestCaseID = '13-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with Server role as branch recorder.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+self.ssinputdata.SMTPServerName+'',
                      'SMTPUsername': ''+self.ssinputdata.SMTPUsername+'',
                      'SMTPPassword': ''+self.ssinputdata.SMTPPassword+'',
                      'SenderEmailAddress': ''+self.ssinputdata.SenderEmailAddress+'',
                      'Port':'565',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus = False
            # Test Case End
            
    # Start Test Case No 13-06
    def testcase_06_UpdateSMTPSettings(self, TestCasesStatus=True):
      
        TestCaseID = '13-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with Server role configured as secondary.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+self.ssinputdata.SMTPServerName+'',
                      'SMTPUsername': ''+self.ssinputdata.SMTPUsername+'',
                      'SMTPPassword': ''+self.ssinputdata.SMTPPassword+'',
                      'SenderEmailAddress': ''+self.ssinputdata.SenderEmailAddress+'',
                      'Port':'565',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus = False
            # Test Case End
            
            
    # Start Test Case No 13-07
    def testcase_07_UpdateSMTPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '13-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with Valid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+self.ssinputdata.SMTPServerName+'',
                      'SMTPUsername': '',
                      'SMTPPassword': '',
                      'SenderEmailAddress': ''+self.ssinputdata.SenderEmailAddress+'',
                      'Port':'565',
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
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
            
    def testcase_08_UpdateSMTPSettings_ValidPort(self, TestCasesStatus=True):
       
        TestCaseID = '13-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with Valid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+self.ssinputdata.SMTPServerName+'',
                      'SMTPUsername': ''+self.ssinputdata.SMTPUsername+'',
                      'SMTPPassword': ''+self.ssinputdata.SMTPPassword+'',
                      'SenderEmailAddress': ''+self.ssinputdata.SenderEmailAddress+'',
                      'Port':'565'
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
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
            
    def testcase_09_UpdateSMTPSettings_InValidPort(self, TestCasesStatus=True):
       
        TestCaseID = '13-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SMTP Settings', 'SMTP Settings Through Put Method', 'Configure the SMTP Settings with Valid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SMTPServer': ''+self.ssinputdata.SMTPServerName+'',
                      'SMTPUsername': ''+self.ssinputdata.SMTPUsername+'',
                      'SMTPPassword': ''+self.ssinputdata.SMTPPassword+'',
                      'SenderEmailAddress': ''+self.ssinputdata.SenderEmailAddress+'',
                      'Port':'acb'
                      
                     }
        
        #URL
        URL = '' +common.Domain+ '' +self.UrlForUpdateSMTPSettings+ ''
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