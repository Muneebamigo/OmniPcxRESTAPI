'''
Created on Oct 28, 2021

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''
import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from Settings import dataFunction as DS
from pickle import FALSE, TRUE
from Key import config
from test_Provisioning import test_01_SystemSettings as SS
from pickle import FALSE

SheetName=    '57-Notification Settings'


class Test_1_UpdateNotificationSettings(TestCase):
    
    # Url For UpdateDashboardConfigurations
    
    
    def test_01_UpdateNotificationSettings(self, TestCaseStatus = True):
        
        TestCaseID = '57-01'
        
        UrlUpdateNotificationSettings='/SystemSettings/UpdateNotificationSettings'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Notification Settings', 'Calling Update Method of Notification Settings', 'Update NotificationSettings')
        
        # System Settings Function calling
        systemFunc = SS.test_1_UpdateSystemSettings()
        systemFunc.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Provider':'0',
                      'AccountSID':''+common.GenerateValidExtension()+'',
                      'AccountToken':''+common.GenerateValidExtension()+'',
                       'SenderNumber':''+common.GenerateValidExtension()+'',
                     }
        
        # Url For Update Site Settings
        URL = ''+common.Domain+''+UrlUpdateNotificationSettings+''
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

class test_2_AddNotificationSettings(TestCase):
    
    # Url For Update Node/PBX
    
    
    # Start Test Case No 57-02
    def testcase_2_AddNotificationSettings(self, TestCasesStatus=True):
        
        TestCaseID = '57-02'
        method_name = 'testcase_2_AddNotificationSettings'
        UrlForaddNotificationSettings = '/SystemSettings/AddReceiverNumber/'
        
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds= DS.DataStorage()
        common.Header('Update Notification Settings' , 'Using Put Method Update Notification Settings' , 'Update ReceiverNumber to System with Valid Input Data.')
        Test_1_UpdateNotificationSettings.test_01_UpdateNotificationSettings(FALSE)     
        ReceiverNumber = common.GenerateValidExtension()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'ReceiverNumber': ''+ReceiverNumber+''
                    ,
        
                    }
        
        URL = ''+common.Domain+''+UrlForaddNotificationSettings+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        data = str(resp['ResponseCode'])
        
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                                     
                    print(common.SuccessMessage)
                    status = 'Passed'
                    ds.add_data(method_name, Parameters,resp, URL)
                            
                            
                else:
                    status = 'Failed'
                    assert False
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
        return ReceiverNumber
            # Test Case End


class test_4_DeleteNotificationSettings(TestCase):  
    
    # Url For Delete Node/PBX
    
    
    # Start Test Case No 02-15
    def testcase_3_DeleteReceiverNumber(self, TestCasesStatus=True):
        
        TestCaseID = '57-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        df= DS.DataStorage()
        common.Header('PBX Configuration' , 'Using Delete Method Delete a ReceiverNumber' , 'Using Delete Method Delete a Receiver Number Data With Valid ID.')
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        urltodeletereceivernumber = '/SystemSettings/DeleteReceiverNumber/'
        # PBX/Node Function Calling
        ReceiverNumber = df.get_ReceiverNumber(TRUE)
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From OPR_Notification_Receivers Where ReceiverNumber = '"+ReceiverNumber+"' ;")
        cursor.execute(SQLCommand)
        receiverid=cursor.fetchone()
        ReceiverID=str(receiverid[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                           
                    }
        
        URL = ''+common.Domain+''+urltodeletereceivernumber+''+ReceiverID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            # Test Case End