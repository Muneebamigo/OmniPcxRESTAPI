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
from test_Provisioning import test_34_CustomFields
from Key import config
SheetName=	'44-CDR Fields'

class test_1_UpdateCDR_Fields(TestCase):
    
    UrlForUpdateCDR_Fields = '/Calls/UpdateCallDetails/'
    
    def testcase_01_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-01'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=CallDetailId
        Device=Device
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        ColumnIndex='13'
        ColumnData='false'
        
        starttime = time.process_time()
        Parameters = {
                    'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
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
            
    def testcase_02_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-02'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with null Column Index.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=CallDetailId
        Device=Device
        GlobalCallID=GlobalCallID
        PBXCallID=PBXCallID
        ColumnIndex=''
        ColumnData='false'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
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
        
    def testcase_03_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-03'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with null ColumnData.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Calling Custom Fields Functions
        CFF=test_34_CustomFields.test_1_UpdateCustomFields()
        CFF.testcase_02_PUTCustomFields(common.PrereqTestCasesStatusUpdate)
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=CallDetailId
        ColumnIndex='0'
        ColumnData=''
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
        
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
        
    def testcase_04_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-04'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with DBRecordID.')
        
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
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=CallDetailId
        Device=''
        GlobalCallID=''
        PBXCallID=''
        ColumnIndex='13'
        ColumnData='false'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
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
    
    def testcase_05_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-05'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with Device & GlobalCallID.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        CorrelatorID=CorrelatorID
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=''
        Device=Device
        GlobalCallID=GlobalCallID
        PBXCallID=''
        ColumnIndex='12'
        ColumnData='I'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
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
            
    def testcase_06_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-06'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with Device & PBXCallID.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        CorrelatorID=CorrelatorID
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=''
        Device=Device
        GlobalCallID=''
        PBXCallID=PBXCallID
        ColumnIndex='13'
        ColumnData='false'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
       
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
            
    def testcase_07_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-07'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with Device & DBRecordID.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        GlobalCallID=GlobalCallID
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=CallDetailId
        Device=Device
        GlobalCallID=''
        PBXCallID=''
        ColumnIndex='13'
        ColumnData='false'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
       
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
            
    def testcase_08_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-08'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with GlobalCallID & DBRecordID.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        PBXCallID=PBXCallID
        Device=Device
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=CallDetailId
        Device=''
        GlobalCallID=GlobalCallID
        PBXCallID=''
        ColumnIndex='13'
        ColumnData='false'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
       
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
            
    def testcase_09_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-09'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields with PBXCallID & DBRecordID.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        Device=Device
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID=CallDetailId
        Device=''
        GlobalCallID=''
        PBXCallID=PBXCallID
        ColumnIndex='12'
        ColumnData='I'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
       
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
            
    def testcase_10_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-10'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields With invalid ColumnData.')
        
        
        # Header Parameters of Rest API
        SiteCode=''
        DBRecordID='1542605B02000100'
        Device=''
        GlobalCallID=''
        PBXCallID=''
        ColumnIndex='13'
        ColumnData='0'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
       
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
    
    def testcase_11_UpdateCDR_Fields(self, TestCasesStatus=True):
        
        TestCaseID = '44-11'
        common = CF.CommonFunctions()
        common.Header('CDR Fields' , 'Using Put Method Update CDR Fields' , 'Update CDR Fields With Non Existing site code.')
        
        # Calling Add Calls Functions
        calls=test_39_AddCalls.test_1_AddCalls()
        GlobalCallID, CorrelatorID, PBXCallID, Device=calls.testcase_42_AddCalls(common.PrereqTestCasesStatusUpdate)
        GlobalCallID=GlobalCallID
        Device=Device
        PBXCallID=PBXCallID
        
        # Tenant DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        SQLCommand = ("Select CallDetailId From CallDetails Where CorrelatorId  = '"+CorrelatorID+"';")
        cursor.execute(SQLCommand)
        calldetailid=cursor.fetchone()
        CallDetailId=str(calldetailid[0])
        
        # Header Parameters of Rest API
        SiteCode='10012232'
        DBRecordID=CallDetailId
        Device=''
        GlobalCallID=''
        PBXCallID=''
        ColumnIndex='13'
        ColumnData='False'
        
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'DBRecordID': ''+DBRecordID+'',
                    'SiteCode': ''+SiteCode+'',
                    'Device': ''+Device+'',
                    'GlobalCallID': ''+GlobalCallID+'',
                    'PBXCallID': ''+PBXCallID+'',
                    'ColumnIndex': ''+ColumnIndex+'',
                    'ColumnData': ''+ColumnData+'',
                    }
        
        URL = ''+common.Domain+''+self. UrlForUpdateCDR_Fields+''
       
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