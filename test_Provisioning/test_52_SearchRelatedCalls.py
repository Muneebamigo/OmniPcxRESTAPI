'''
Created on Feb 18, 2019

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
from test_Provisioning import test_39_AddCalls
from test_Provisioning import test_01_SystemSettings
from Key import config

SheetName=	'52-Search Related Calls'

class test_1_SearchRelatedCalls(TestCase):
    
    # Start Test Case No 52-01
    def testcase_01_SearchRelatedCalls(self, TestCasesStatus=True):
       
        TestCaseID = '52-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method with valid GlobalCallID and CorrelatorID when server is role primary.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_02_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    'Channel':'',
                    'BoardID':'',
                    'CallDuration':'',
                    'CallDate':'',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
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
            
            
    # Start Test Case No 52-02
    def testcase_02_SearchRelatedCalls(self, TestCasesStatus=True):
       
        TestCaseID = '52-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method with invalid or non existing site code.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_02_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        # Test Case Start Time 
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '123456',
                    'GlobalCallID':''+GlobalCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    'Channel':'',
                    'BoardID':'',
                    'CallDuration':'',
                    'CallDate':'',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 500:
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
            
      
    # Start Test Case No 52-03
    def testcase_03_SearchRelatedCalls(self, TestCasesStatus=True):
       
        TestCaseID = '52-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method when non existing GlobalCallID.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        globalcallID, CorrelatorID, PBXCallID, Device=calls.testcase_02_AddCalls(common.PrereqTestCasesStatusUpdate)
        globalcallID=globalcallID
        PBXCallID=PBXCallID
        Device=Device
        
        GlobalCallID = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    'Channel':'',
                    'BoardID':'',
                    'CallDuration':'',
                    'CallDate':'',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
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
            
            
        
    # Start Test Case No 52-04
    def testcase_04_SearchRelatedCalls(self, TestCasesStatus=True):
       
        TestCaseID = '52-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method when non existing CorrelatorID.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, correlatorID, PBXCallID, Device=calls.testcase_02_AddCalls(common.PrereqTestCasesStatusUpdate)
        correlatorID=correlatorID
        PBXCallID=PBXCallID
        Device=Device
        
        CorrelatorID = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    'Channel':'',
                    'BoardID':'',
                    'CallDuration':'',
                    'CallDate':'',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
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
            
            
            
    # Start Test Case No 52-05
    def testcase_05_SearchRelatedCalls(self, TestCasesStatus=True):
       
        TestCaseID = '52-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method when Server role configured secondary.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_02_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    'Channel':'',
                    'BoardID':'',
                    'CallDuration':'',
                    'CallDate':'',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
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
            
            
            
    # Start Test Case No 52-06
    def testcase_06_SearchRelatedCalls(self, TestCasesStatus=True):
       
        TestCaseID = '52-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method when Server role configured  branch.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_02_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    'Channel':'',
                    'BoardID':'',
                    'CallDuration':'',
                    'CallDate':'',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
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
            
    
    # Start Test Case No 52-07
    def testcase_07_SearchRelatedCalls(self, TestCasesStatus=True):
       
        TestCaseID = '52-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method with invalid date format.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_02_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    'Channel':'12',
                    'BoardID':'12',
                    'CallDuration':'50',
                    'CallDate':'abc123abc123',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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
            
            
            
    # Start Test Case No 52-08
    def testcase_08_SearchRelatedCalls(self, TestCasesStatus=True):
        
        TestCaseID = '52-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method with invalid data when insert channel but BoardID,CallDuration and CallDate is empty/null.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'CorrelatorID':'',
                    'Channel':'15',
                    'BoardID':'123',
                    'CallDuration':'',
                    'CallDate':'',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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
            
            
    # Start Test Case No 52-09
    def testcase_09_SearchRelatedCalls(self, TestCasesStatus=True):
        
        TestCaseID = '52-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Search Related Calls' , 'Search Related Calls by Get Method' , 'Search Related Calls by Get Method with invalid data when insert channel but BoardID,CallDuration and CallDate is empty/null.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'CorrelatorID':'',
                    'Channel':'15',
                    'BoardID':'123',
                    'CallDuration':'50',
                    'CallDate':'12/12/2018 08:08:08',
                    'CallStatus':'5',
                    
                    }
        
        # Url For Add Board  
        UrlForGetSearchRelatedCalls = '/Calls/RelatedCalls/'
        URL = ''+common.Domain+''+UrlForGetSearchRelatedCalls
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