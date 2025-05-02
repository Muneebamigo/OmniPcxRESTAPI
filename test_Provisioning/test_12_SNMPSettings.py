'''
Created on Jul 20, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time,requests,random
from Settings import CommonFunctions as CF
from unittest import TestCase
from openpyxl import load_workbook
import test_Provisioning.test_01_SystemSettings as systemsettingsFun
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config

SheetName=	'12-SNMP settings'
class test_1_AddSNMPSettings(TestCase):
    # Url For Update SNMP Settings
    UrlToAddSNMPSettings = '/SNMPSettings/Add'
    
    # Start Test Case No 12-01
    def testcase_01_AddSNMPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '12-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SNMP Settings', 'SNMP Settings Through Post Method', 'Configure the SNMP Settings with Valid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFun.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        ValidIP1=common.GenrateValidIPString()
        
        # Generate Random Integer Value
        SNMPPort=str(random.randint(9000 , 9999))
        # Generate Simple Character String Limit 10 Characters
        SNMPCommunityString=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'RecieverIP': ''+ValidIP1+'',
                      'Port': ''+SNMPPort+'',
                      'CommunityString': ''+SNMPCommunityString+'',
                      
                     }
        
        URL = '' +common.Domain+ '' +self.UrlToAddSNMPSettings+ ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
        return ValidIP1
            
    # Start Test Case No 12-02
    def testcase_02_AddSNMPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '12-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SNMP Settings', 'SNMP Settings Through Post Method', 'Configure the SNMP Settings with InValid data.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFun.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        InValidIP1='abc123*'
        
        # Generate Random Integer Value
        SNMPPort=str(random.randint(9000 , 9999))
        # Generate Simple Character String Limit 10 Characters
        SNMPCommunityString=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'RecieverIP': ''+InValidIP1+'',
                      'Port': ''+SNMPPort+'',
                      'CommunityString': ''+SNMPCommunityString+'',
                      
                     }
        
        URL = '' +common.Domain+ '' +self.UrlToAddSNMPSettings+ ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
    def testcase_03_AddSNMPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '12-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SNMP Settings', 'SNMP Settings Through Post Method', 'Configure the SNMP Settings with Empty IP.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFun.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        
        
        # Generate Random Integer Value
        SNMPPort=str(random.randint(9000 , 9999))
        # Generate Simple Character String Limit 10 Characters
        SNMPCommunityString=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'RecieverIP': '',
                      'Port': ''+SNMPPort+'',
                      'CommunityString': ''+SNMPCommunityString+'',
                      
                     }
        
        URL = '' +common.Domain+ '' +self.UrlToAddSNMPSettings+ ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
    def testcase_04_AddSNMPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '12-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SNMP Settings', 'SNMP Settings Through Post Method', 'Configure the SNMP Settings with Empty Port.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFun.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        ValidIP1='172.20.1.16'
        
        # Generate Random Integer Value
        # SNMPPort=str(random.randint(9000 , 9999))
        # Generate Simple Character String Limit 10 Characters
        SNMPCommunityString=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'RecieverIP': ''+ValidIP1+'',
                      'Port': '',
                      'CommunityString': ''+SNMPCommunityString+'',
                      
                     }
        
        URL = '' +common.Domain+ '' +self.UrlToAddSNMPSettings+ ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
    def testcase_05_AddSNMPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '12-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SNMP Settings', 'SNMP Settings Through Post Method', 'Configure the SNMP Settings with Empty Community String.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFun.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        # Generate Valid IP
        ValidIP1='172.20.1.16'
        
        # Generate Random Integer Value
        SNMPPort=str(random.randint(9000 , 9999))
        # Generate Simple Character String Limit 10 Characters
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'RecieverIP': ''+ValidIP1+'',
                      'Port': ''+SNMPPort+'',
                      'CommunityString': '',
                      
                     }
        
        URL = '' +common.Domain+ '' +self.UrlToAddSNMPSettings+ ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
            
class test_2_UpdateSNMPSettings(TestCase):
    # Url For Update SNMP Settings
    UrlToUpdateSNMPSettings = '/SNMPSettings/Update'
    
    # Start Test Case No 12-01
    def testcase_06_UpdateSNMPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '12-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SNMP Settings', 'SNMP Settings Through PUT Method', 'Update the SNMP IP Settings with Valid data.')
        #ValidIP1=test_1_AddSNMPSettings.testcase_01_AddSNMPSettings(common.PrereqTestCasesStatusUpdate)
        #print(ValidIP1)
        AddSNMPSett1=test_1_AddSNMPSettings()
        Ip = AddSNMPSett1.testcase_01_AddSNMPSettings(common.PrereqTestCasesStatusUpdate)
        
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("  SELECT ID from OPR_SNMP_Setting where ReceiverIP = '"+Ip+"'")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        Id = str(vals[0])
        # Config DB Connectivity Function c
        # Test Case Start Time
        starttime = time.process_time()
        
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID':''+Id+'',
                      'RecieverIP': '172.20.1.100',
                      'Port': '162',
                      'CommunityString': 'updated',
                      
                     }
        
        URL = '' +common.Domain+ '' +self.UrlToUpdateSNMPSettings+ ''
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
            

class test_3_DeleteSNMPSettings(TestCase):
    # Url For Update SNMP Settings
    UrlToDeleteSNMPSettings = '/SNMPSettings/Delete/'
    
    # Start Test Case No 12-01
    def testcase_07_DeleteSNMPSettings(self, TestCasesStatus=True):
       
        TestCaseID = '12-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SNMP Settings', 'SNMP Settings Through Delete Method', 'Delete the SNMP Settings with ID.')
        AddSNMPSett = test_1_AddSNMPSettings()
        ValidIP1 = AddSNMPSett.testcase_01_AddSNMPSettings(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function c
        # Test Case Start Time
        starttime = time.process_time()
        
        
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("  SELECT ID from OPR_SNMP_Setting where ReceiverIP = '"+ValidIP1+"'")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        Id = str(vals[0])
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID':''+ Id +'',
                      
                     }
        
        URL = '' +common.Domain+ '' +self.UrlToDeleteSNMPSettings+''+Id+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
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
        
    