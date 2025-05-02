'''
Created on Aug 2, 2018

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

SheetName=	'47-SearchByGlobalId'

class test_1_SearchRecordedCallsByGlobalCallID(TestCase):
   
    
    def testcase_01_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '47-01'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls by Get Method with valid GlobalCallID when server is role primary.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        CorrelatorID=CorrelatorID
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    }
        
        UrlForGetRecordedCallsByGlobalCallID = '/Calls/SearchByGlobalCallID/'
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByGlobalCallID
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    def testcase_02_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '47-02'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls with null/invalid GlobalCallID.')
        
        GlobalCallID=''
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    }
        UrlForGetRecordedCallsByGlobalCallID = '/Calls/SearchByGlobalCallID/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByGlobalCallID
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    def testcase_03_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '47-03'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls with GlobalCallID and invalid/non-existing SiteCode')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        CorrelatorID=CorrelatorID
        SiteCode='123456'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': ''+SiteCode+'',
                    'GlobalCallID':''+GlobalCallID+'',
                    }
        UrlForGetRecordedCallsByGlobalCallID = '/Calls/SearchByGlobalCallID/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByGlobalCallID
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 500:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
    
    def testcase_04_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '47-04'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls with GlobalCallID when server role is Secondary')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        CorrelatorID=CorrelatorID
        
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    }
        UrlForGetRecordedCallsByGlobalCallID = '/Calls/SearchByGlobalCallID/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByGlobalCallID
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    def testcase_05_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '47-05'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls with GlobalCallID when server role is Branch')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        CorrelatorID=CorrelatorID
        
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    }
        UrlForGetRecordedCallsByGlobalCallID = '/Calls/SearchByGlobalCallID/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByGlobalCallID
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False