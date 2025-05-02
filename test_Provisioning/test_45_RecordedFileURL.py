'''
Created on Aug 1, 2018

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
from Key import config
SheetName=	'45-Recorded File URL'

class test_1_RecordedFileURL(TestCase):
    
    UrlForGetFileURL = '/Calls/GetFileURL'
    
    def testcase_01_Recorded_File_URL(self, TestCasesStatus=True):
        
        TestCaseID = '45-01'
        common = CF.CommonFunctions()
        common.Header('RecordedFileURL' , 'Using Get Method Get RecordedFileURL' , 'Get all Data RecordedFileURL with URLInfiniteDuration true.')
        
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
                      'SiteCode':'',
                      'DBRecordID':''+CallDetailId+'',
                      'URLInfiniteDuration':"True",
    
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetFileURL+''
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    def testcase_02_Recorded_File_URL(self, TestCasesStatus=True):
        
        TestCaseID = '45-02'
        common = CF.CommonFunctions()
        common.Header('RecordedFileURL' , 'Using Get Method Get RecordedFileURL' , 'Get all Data RecordedFileURL with URLInfiniteDuration false.')
        
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
                      'SiteCode':'',
                      'DBRecordID':''+CallDetailId+'',
                      'URLInfiniteDuration':"False",
    
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetFileURL+''
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
          
    def testcase_03_Recorded_File_URL(self, TestCasesStatus=True):
        
        TestCaseID = '45-03'
        common = CF.CommonFunctions()
        common.Header('RecordedFileURL' , 'Using Get Method Get RecordedFileURL' , 'Get all Data RecordedFileURL with non existing Site Code.')
        
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
        
        SiteCode='123456'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':''+SiteCode+'',
                      'DBRecordID':''+CallDetailId+'',
                      'URLInfiniteDuration':'True',
    
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetFileURL+''
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
      
    def testcase_04_Recorded_File_URL(self, TestCasesStatus=True):
        
        TestCaseID = '45-04'
        common = CF.CommonFunctions()
        common.Header('RecordedFileURL' , 'Using Get Method Get RecordedFileURL' , 'Get all Data RecordedFileURL with DBRecordID null.')
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'DBRecordID':"",
                      'URLInfiniteDuration':"",
    
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetFileURL+''
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
            
    def testcase_05_Recorded_File_URL(self, TestCasesStatus=True):
        
        TestCaseID = '45-05'
        common = CF.CommonFunctions()
        common.Header('RecordedFileURL' , 'Using Get Method Get RecordedFileURL' , 'Get all Data RecordedFileURL with URLInfiniteDuration null.')
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'DBRecordID':"",
                      'URLInfiniteDuration':"",
    
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetFileURL+''
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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