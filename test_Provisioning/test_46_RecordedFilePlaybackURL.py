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

SheetName=	'46-Recorded File Playback URL'

class test_1_GetRecordedFilePlayBackURL(TestCase):
    
    UrlForGetPlayBackURL = '/Calls/GetCallPlaybackURL'

    def testcase_01_Get_RecordedFile_PlayBackURL(self, TestCasesStatus=True):
        
        TestCaseID = '46-01'
        common = CF.CommonFunctions()
        common.Header('RecordedPlayBackURL' , 'Using Get Method Get RecordedPlayBackURL' , 'Get all Data RecordedPlayBackURL .')
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
                      'SiteCode':"",
                      'DBRecordID':''+CallDetailId+'',
                      'PlayCallChannels': ''
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetPlayBackURL+''
        response = requests.get(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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

    def testcase_02_Get_RecordedFile_PlayBackURL(self, TestCasesStatus=True):
        
        TestCaseID = '46-02'
        common = CF.CommonFunctions()
        common.Header('RecordedPlayBackURL' , 'Using Get Method Get RecordedPlayBackURL' , 'Get all Data RecordedPlayBackURL where dbrecord id is null.')
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'DBRecordID':'123456',
                      'PlayCallChannels': ''
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetPlayBackURL+''
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
            
    def testcase_03_Get_RecordedFile_PlayBackURL(self, TestCasesStatus=True):
        
        TestCaseID = '46-03'
        common = CF.CommonFunctions()
        common.Header('RecordedPlayBackURL' , 'Using Get Method Get RecordedPlayBackURL' , 'Get all Data RecordedPlayBackURL where SiteCode is invalid.')
        
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
                      'SiteCode':"00000",
                      'DBRecordID':''+CallDetailId+'',
                      'PlayCallChannels': ''
                    }
        
        URL = ''+common.Domain+''+self.UrlForGetPlayBackURL+''
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