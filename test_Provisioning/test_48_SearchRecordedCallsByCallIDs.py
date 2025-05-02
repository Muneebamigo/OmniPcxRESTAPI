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

SheetName=	'48-SearchByCallIDs'

class test_1_SearchRecordedCallsByCallIDs(TestCase):
   
    
    def testcase_01_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-01'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with GlobalCallID When server role as primary role.')
        
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
                    'DBRecordID':'',
                    'PBXCallID':'',
                    'CorrelatorID':'',
                    }
        
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
       
        TestCaseID = '48-02'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls with GlobalCallID When server role as Secondary role.')
        
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
                    'DBRecordID':'',
                    'PBXCallID':'',
                    'CorrelatorID':'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_03_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-03'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls with GlobalCallID When server role as Branch role..')
        
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
                    'DBRecordID':'',
                    'PBXCallID':'',
                    'CorrelatorID':'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_04_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-04'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with DBRecordID When server role as primary role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        Device=Device
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':''+CallDetailId+'',
                    'PBXCallID':'',
                    'CorrelatorID':'',
                    }
        
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
       
        TestCaseID = '48-05'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with DBRecordID When server role as secondary role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        Device=Device
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':''+CallDetailId+'',
                    'PBXCallID':'',
                    'CorrelatorID':'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_06_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-06'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with DBRecordID When server role as branch role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        Device=Device
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':''+CallDetailId+'',
                    'PBXCallID':'',
                    'CorrelatorID':'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_07_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-07'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with PBXCallID When server role as primary role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        CorrelatorID=CorrelatorID
        Device=Device
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':'',
                    'PBXCallID':''+PBXCallID+'',
                    'CorrelatorID':'',
                    }
        
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_08_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-08'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with PBXCallID When server role as secondary role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        CorrelatorID=CorrelatorID
        Device=Device
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':'',
                    'PBXCallID':''+PBXCallID+'',
                    'CorrelatorID':'',
                    }
        
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_09_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-09'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with PBXCallID When server role as branch role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        CorrelatorID=CorrelatorID
        Device=Device
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':'',
                    'PBXCallID':''+PBXCallID+'',
                    'CorrelatorID':'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_10_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-10'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with CorrelatorID When server role as primary role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        Device=Device
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':'',
                    'PBXCallID':'',
                    'CorrelatorID':''+CorrelatorID+'',
                    }
        
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_11_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-11'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with CorrelatorID When server role as secondary role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        Device=Device
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':'',
                    'PBXCallID':'',
                    'CorrelatorID':''+CorrelatorID+'',
                    }
        
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_12_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-12'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with CorrelatorID When server role as branch role.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        Device=Device
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':'',
                    'DBRecordID':'',
                    'PBXCallID':'',
                    'CorrelatorID':''+CorrelatorID+'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_13_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-13'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with all valid parameters when server role as primary role.')
        
        GlobalCallID='123abc456'
        CallDetailId='123abc456'
        PBXCallID='123abc456'
        CorrelatorID='123acb456'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'DBRecordID':''+CallDetailId+'',
                    'PBXCallID':''+PBXCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
           
    def testcase_14_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-14'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls  with all invalid parameters when server role as primary role.')
        
        # Calling System Settings Functions
        systemsettings=test_01_SystemSettings.test_1_UpdateSystemSettings()
        systemsettings.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        GlobalCallID=''
        DBRecordID=''
        PBXCallID=''
        CorrelatorID=''
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'GlobalCallID':''+GlobalCallID+'',
                    'DBRecordID':''+DBRecordID+'',
                    'PBXCallID':''+PBXCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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
            
    def testcase_15_GetRecordedCallsByGlobalCallID(self, TestCasesStatus=True):
       
        TestCaseID = '48-15'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Calls' , 'Search Recorded Calls by Get Method' , 'Search Recorded Calls with non-existing/invalid SiteCode.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        Device=Device
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        SiteCode='123456'
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': ''+SiteCode+'',
                    'GlobalCallID':''+GlobalCallID+'',
                    'DBRecordID':''+CallDetailId+'',
                    'PBXCallID':''+PBXCallID+'',
                    'CorrelatorID':''+CorrelatorID+'',
                    }
        UrlForGetRecordedCallsByCallIDs = '/Calls/SearchByCallIDs/'
        
        URL = ''+common.Domain+''+UrlForGetRecordedCallsByCallIDs
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