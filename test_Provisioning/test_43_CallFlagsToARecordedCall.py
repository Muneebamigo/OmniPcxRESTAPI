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
import random
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from test_Provisioning import test_39_AddCalls
from Key import config

SheetName=	'43-Call Flags'

class test_1_Update_Call_Flags(TestCase):
    
    UrlForUpdateCallFlag = '/Calls/AssignCallFlag'
    
    def testcase_01_Update_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-03'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Put Method to update Call Flags' , 'Update specific record.')
        
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
        
        FlagID= str(random.randint(1, 7))

        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'DBRecordID':''+CallDetailId+'',
                      'FlagID':''+FlagID+'',
    
                    }
        
        UrlForUpdateCallFlag = '/Calls/AssignCallFlag'
        URL = ''+common.Domain+''+UrlForUpdateCallFlag+''
        response = requests.put(URL, headers=Parameters)
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

        return CallDetailId, FlagID


    def testcase_02_Update_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-04'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Put Method to update Call Flags' , 'Update Call Flag with null/invalid flagID.')
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
        
        FlagID= ''

        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'DBRecordID':''+CallDetailId+'',
                      'FlagID':''+FlagID+'',
    
                    }
        
        
        URL = ''+common.Domain+''+self.UrlForUpdateCallFlag+''
        response = requests.put(URL, headers=Parameters)
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
            
    def testcase_03_Update_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-08'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Put Method to update Call Flags' , 'Update Call Flag with null/invalid DBRecordID.')
        

        
        FlagID= str(random.randint(1, 7))

        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'DBRecordID':'',
                      'FlagID':''+FlagID+'',
    
                    }
        
        
        URL = ''+common.Domain+''+self.UrlForUpdateCallFlag+''
        response = requests.put(URL, headers=Parameters)
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
            
    def testcase_04_Update_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-09'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Put Method to update Call Flags' , 'Update Call Flag with invalid Site Code.')
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
        
        FlagID= str(random.randint(1, 7))

        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'1234567',
                      'DBRecordID':''+CallDetailId+'',
                      'FlagID':''+FlagID+'',
    
                    }
        
        
        URL = ''+common.Domain+''+self.UrlForUpdateCallFlag+''
        response = requests.put(URL, headers=Parameters)
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


class test_2_Get_Call_Flags(TestCase):
    
    UrlForGetCallFlag = '/Calls/GetCallFlags'
    
    def testcase_01_Get_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-01'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Get Method to Get Call Flags' , 'Get all Call Flag details.')
        
        CallDetailId, FlagID=test_1_Update_Call_Flags.testcase_01_Update_Call_Flags(common.PrereqTestCasesStatusUpdate)
        FlagID=FlagID
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'DBRecordID':''+CallDetailId+'',
    
                    }
        
        
        URL = ''+common.Domain+''+self.UrlForGetCallFlag+''
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





    def testcase_02_Get_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-02'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Get Method to Get Call Flags' , 'Get Call Flag with null dbRecordid.')
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'DBRecordID':"",
    
                    }
        
        
        URL = ''+common.Domain+''+self.UrlForGetCallFlag+''
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

class test_3_Delete_Call_Flags(TestCase):
    
    UrlForDelCallFlag = '/Calls/RemoveCallFlag'
    
    def testcase_01_Delete_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-05'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Delete Method to remove Call Flags' , 'Remove  Call Flag details.')
        
        CallDetailId, FlagID=test_1_Update_Call_Flags.testcase_01_Update_Call_Flags(common.PrereqTestCasesStatusUpdate)
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'DBRecordID':''+CallDetailId+'',
                      'FlagID':''+FlagID+'',
    
                    }
        
        URL = ''+common.Domain+''+self.UrlForDelCallFlag+''
        response = requests.delete(URL, headers=Parameters)
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


    def testcase_02_Delete_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-06'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Delete Method to Delete Call Flags' , 'Delete all Call Flag with invalid DBRecordID.')
        
        DBRecordID='123456789'

        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'DBRecordID':''+DBRecordID+'',
                      'FlagID':"",
    
                    }
        
        
        URL = ''+common.Domain+''+self.UrlForDelCallFlag+''
        response = requests.delete(URL, headers=Parameters)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
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





    def testcase_03_Call_Flags(self, TestCasesStatus=True):
        
        TestCaseID = '43-07'
        common = CF.CommonFunctions()
        common.Header('Call flags' , 'Using Delete Method to Delete Call Flags' , 'Delete method with invalid Site Code.')
        
        CallDetailId='123123123152315621'
        SiteCode='123456'
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':''+SiteCode+'',
                      'DBRecordID':''+CallDetailId+'',
                      'FlagID':"",
    
                    }
        
        
        URL = ''+common.Domain+''+self.UrlForDelCallFlag+''
        response = requests.delete(URL, headers=Parameters)
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