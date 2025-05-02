'''
Created on Mar 13, 2020

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

SheetName=	'56-Dashboard Configurations'

class Test_1_UpdateDashboardConfiguration(TestCase):
    
    # Url For UpdateDashboardConfigurations
    UrlUpdateDashboardConfigurations='/SiteSettings/UpdateDashboardConfigurations'
    
    def test_01_UpdateDashboardConfigurations(self, TestCaseStatus = True):
        
        TestCaseID = '56-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Dashboard Settings', 'Calling Update Method of Dashboard Configurations', 'Update DashboardConfigurations')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Chart':'0',
                      'Enabled':'True',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateDashboardConfigurations+''
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
    
    def test_02_UpdateDashboardConfigurations(self, TestCaseStatus = True):
        
        TestCaseID = '56-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Dashboard Settings', 'Calling Update Method of Dashboard Configurations', 'Update DashboardConfigurations for all charts')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Chart':'0,1,2,3,4,5,6',
                      'Enabled':'True,True,True,True,True,True,True',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateDashboardConfigurations+''
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
    
    def test_03_UpdateDashboardConfigurations(self, TestCaseStatus = True):
        
        TestCaseID = '56-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Dashboard Settings', 'Calling Update Method of Dashboard Configurations', 'Update DashboardConfigurations and disable any chart')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Chart':'0',
                      'Enabled':'False',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateDashboardConfigurations+''
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
    
    def test_04_UpdateDashboardConfigurations(self, TestCaseStatus = True):
        
        TestCaseID = '56-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Dashboard Settings', 'Calling Update Method of Dashboard Configurations', 'Update DashboardConfigurations and disable all charts')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Chart':'0,1,2,3,4,5,6',
                      'Enabled':'False,False,False,False,False,False,False',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+self.UrlUpdateDashboardConfigurations+''
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

