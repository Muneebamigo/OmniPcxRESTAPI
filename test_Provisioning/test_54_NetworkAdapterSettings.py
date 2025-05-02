'''
Created on Nov 23, 2019 OPR 2.4.0.7

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
from Key import config

SheetName=	'54-Network Adapter Settings'

class test_1_UpdateNetwrokAdapterSettings(TestCase):
    
    # Url For Update Network Adapter Settings
    UrlForUpdateNetworkAdapterSettings = '/SystemSettings/UpdateNICSettings'
    
    # Start Test Case No 54-01 OPR 2.4.0.7 Build 4
    def testcase_01_UpdateNetworkAdapterSettings(self, TestCasesStatus=True):
        
        TestCaseID = '54-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Network Adapter Settings', 'Network Adapter Settings Through Put Method', 'Configure the Network Adapter Settings with Valid IP and Adapter')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        ValidIP=common.GenrateValidIPString()
        ValidSecIP=common.GenrateValidIPString()
        NetwrkAdpter= '\\Device\\NPF_{8CCC9DFD-EB46-4883-8876-3476C54B3695}'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'NetworkAdapter': ''+NetwrkAdpter+'',
                      'RecorderType': '8',
                      'PrimaryServerIP':''+ValidIP+'',
                      'SecondaryServerIP':''+ValidSecIP+'',
                      
                     }
        # Url For Update Network Adapter Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateNetworkAdapterSettings+ ''
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
            
            
        # Start Test Case No 54-02 OPR 2.4.0.7 Build 4
    def testcase_02_UpdateNetworkAdapterSettings(self, TestCasesStatus=True):
        
        TestCaseID = '54-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Network Adapter Settings', 'Network Adapter Settings Through Put Method', 'Configure the Network Adapter Settings with Valid IP and Adapter on Secondary Server')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        ValidIP=common.GenrateValidIPString()
        ValidSecIP=common.GenrateValidIPString()
        NetwrkAdpter= '\\Device\\NPF_{8CCC9DFD-EB46-4883-8876-3476C54B3695}'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'NetworkAdapter': ''+NetwrkAdpter+'',
                      'RecorderType': '8',
                      'PrimaryServerIP':''+ValidIP+'',
                      'SecondaryServerIP':''+ValidSecIP+'',
                      
                     }
        # Url For Update Network Adapter Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateNetworkAdapterSettings+ ''
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


    # Start Test Case No 54-03 OPR 2.4.0.7 Build 4
    def testcase_03_UpdateNetworkAdapterSettings(self, TestCasesStatus=True):
        
        TestCaseID = '54-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Network Adapter Settings', 'Network Adapter Settings Through Put Method', 'Configure the Network Adapter Settings with InValid IP')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        InValidIP='12354'
        ValidIP=common.GenrateValidIPString()
        NetwrkAdpter= '\\Device\\NPF_{8CCC9DFD-EB46-4883-8876-3476C54B3695}'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'NetworkAdapter': ''+NetwrkAdpter+'',
                      'RecorderType': '8',
                      'PrimaryServerIP':''+InValidIP+'',
                      'SecondaryServerIP':''+ValidIP+'',
                      
                     }
        # Url For Update Network Adapter Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateNetworkAdapterSettings+ ''
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
            
            
    # Start Test Case No 54-04 OPR 2.4.0.7 Build 4
    def testcase_04_UpdateNetworkAdapterSettings(self, TestCasesStatus=True):
        
        TestCaseID = '54-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Network Adapter Settings', 'Network Adapter Settings Through Put Method', 'Configure the Network Adapter Settings with Recorder Type other than 8')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        ValidIP=common.GenrateValidIPString()
        ValidSecIP=common.GenrateValidIPString()
        NetwrkAdpter= '\\Device\\NPF_{8CCC9DFD-EB46-4883-8876-3476C54B3695}'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'NetworkAdapter': ''+NetwrkAdpter+'',
                      'RecorderType': '0',
                      'PrimaryServerIP':''+ValidIP+'',
                      'SecondaryServerIP':''+ValidSecIP+'',
                      
                     }
        # Url For Update Network Adapter Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateNetworkAdapterSettings+ ''
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
            
    # Start Test Case No 54-05 OPR 2.4.0.7 Build 4
    def testcase_05_UpdateNetworkAdapterSettings(self, TestCasesStatus=True):
        
        TestCaseID = '54-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Network Adapter Settings', 'Network Adapter Settings Through Put Method', 'Configure the Network Adapter Settings with Empty Adapter')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        ValidIP=common.GenrateValidIPString()
        ValidSecIP=common.GenrateValidIPString()
        #NetwrkAdpter= '\\Device\\NPF_{8CCC9DFD-EB46-4883-8876-3476C54B3695}'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'NetworkAdapter': '',
                      'RecorderType': '8',
                      'PrimaryServerIP':''+ValidIP+'',
                      'SecondaryServerIP':''+ValidSecIP+'',
                      
                     }
        # Url For Update Network Adapter Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateNetworkAdapterSettings+ ''
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
            
    # Start Test Case No 54-06 OPR 2.4.0.7 Build 4
    def testcase_06_UpdateNetworkAdapterSettings(self, TestCasesStatus=True):
        
        TestCaseID = '54-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Network Adapter Settings', 'Network Adapter Settings Through Put Method', 'Configure the Network Adapter Settings with Empty IP Address')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        ValidIP=common.GenrateValidIPString()
        NetwrkAdpter= '\\Device\\NPF_{8CCC9DFD-EB46-4883-8876-3476C54B3695}'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'NetworkAdapter': ''+NetwrkAdpter+'',
                      'RecorderType': '8',
                      'PrimaryServerIP':'',
                      'SecondaryServerIP':''+ValidIP+'',
                      
                     }
        # Url For Update Network Adapter Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateNetworkAdapterSettings+ ''
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
            
    def testcase_07_UpdateNetworkAdapterSettings_Attendant(self, TestCasesStatus=True):
        
        TestCaseID = '54-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Network Adapter Settings', 'Network Adapter Settings Through Put Method', 'Configure the Network Adapter Settings for Attendant ')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        
        NetwrkAdpter= '\\Device\\NPF_{8CCC9DFD-EB46-4883-8876-3476C54B3695}'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'NetworkAdapter': ''+NetwrkAdpter+'',
                      'RecorderType': '2',
                      'PrimaryServerIP':'',
                      'SecondaryServerIP':'',
                      
                     }
        # Url For Update Network Adapter Settings
        URL = '' +common.Domain+ '' +self.UrlForUpdateNetworkAdapterSettings+ ''
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