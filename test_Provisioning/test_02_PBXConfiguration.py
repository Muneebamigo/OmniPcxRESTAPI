'''
Created on Jun 14, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed

----------------pre requisite--------------------------------------
System setting must be configured otherwise
Node operation can not performed
get_OXENameAndIP() function which is in DataFunction.py File
is used to get the data which is take as parameter.

------------------OutPut----------------------------
This module will be ada/update/get/Delete the PBX (Node),
All the node(PBX) which will be added  will be shown on Node page of the server Administration.
All the node(PBX) which will be Updated  will be shown on Node page of the server Administration.
the node(PBX) which  will be delete , remove Node page of the server Administration.

'''

import time, requests
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
from test_Provisioning import test_01_SystemSettings as systemsettingsFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from test_Provisioning import test_19_Branch as BFun
from Settings import dataFunction as DS
from Key import config

SheetName = '2-PBX Configuration'


class test_1_AddPBXConfiguration(TestCase):
    # Url For Add Node/PBX
    UrlForAddPBX = '/PBX/Add/'

    # Start Test Case No 02-01
    def testcase_01_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-01'
        method_name = "testcase_01_AddPBXConfiguration"
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Recorder type is Main.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select OXEIP From PBXDetail Where OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand1)
        primarip = cursor.fetchone()
        SQLCommand2 = ("Select OXEName From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand2)
        pbxname = cursor.fetchone()
        cursor.commit()

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if primarip[0] == ValidIP:
                        print('b')
                        if pbxname[0] == OXEName:
                            print(common.SuccessMessage)
                            status = 'Passed'
                            ds.add_data(method_name, Parameters, resp, URL)
                else:
                    status = 'Failed'
                    # assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    # Start Test Case No 02-02
    def testcase_02_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System When Duplicate PBX IP.')

        OXEName, ValidIP = ds.get_OXENameAndIP(False)
        OXEName = OXEName
        pbxname = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + pbxname + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 409:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-03
    def testcase_03_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System When Duplicate PBX Name.')

        OXEName, ValidIP = ds.get_OXENameAndIP(False)
        ValidIP = ValidIP
        pbxip = common.GenrateValidIPString()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + pbxip + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # Hit API Through Methods
        response.json()
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 409:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-04
    def testcase_04_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Recorder type is Main with IPDR Logger.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()
        # Generate Valid IP
        loggerIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '' + loggerIP + '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }
        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # SQL Queries for Data Verification
        SQLCommand1 = ("Select OXEIP From PBXDetail Where OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand1)
        oxeIP = cursor.fetchone()
        SQLCommand2 = ("Select IPLogger From PBXDetail Where IPLogger = '" + loggerIP + "';")
        cursor.execute(SQLCommand2)
        LoggerIP = cursor.fetchone()
        SQLCommand3 = ("Select OXEName From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand3)
        pbxname = cursor.fetchone()
        cursor.commit()

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if oxeIP[0] == ValidIP:
                        print('b')
                        if LoggerIP[0] == loggerIP:
                            print('c')
                            if pbxname[0] == OXEName:
                                print(common.SuccessMessage)
                                status = 'Passed'
                else:
                    status = 'Failed'

            # Write Output Result in Excel File        
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-05
    def testcase_05_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to system with more then 250 characters in IP field.')

        # Generate Valid IP
        ValidIP = common.GenrateDesc250()
        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + 'test',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': ''
                      }

        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-06 
    def testcase_06_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System When Server Role as Secondary.')

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-07
    def testcase_07_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System When Server Role as Branch.')

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-08
    def testcase_08_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node of branch to System When Branch in not configured.')

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()
        branchID = '123'

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '' + branchID + '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End

        # Start Test Case No 02-09

    def testcase_09_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node of branch to System When Branch is configured.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        BranchFunction = BFun.test_1_AddBranch()
        BranchName = BranchFunction.testcase_01_AddBranch(common.PrereqTestCasesStatusUpdate)

        OXEName1, ValidIPp = ds.get_OXENameAndIP(False)
        # OXEName1, ValidIPp = test_1_AddPBXConfiguration.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)

        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID From Branch Where BranchName = '" + BranchName + "';")
        cursor.execute(SQLCommand)
        branchid = cursor.fetchone()
        BranchID = str(branchid[0])
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName1 + "' and OXEIP = '" + ValidIPp + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '' + BranchID + '',
                      'MainPBXID': '' + PBXID + '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False

        return OXEName, BranchID
        # Test Case End

    # Start Test Case No 02-17
    def testcase_17_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Null Name.')

        # Generate Simple Character String Limit 10 Characters
        OXEName = ''
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    # Start Test Case No 02-18
    def testcase_18_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System with invalid/Non Existing MainPBXID.')

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '123456',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    # Start Test Case No 02-19
    def testcase_19_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Recorder type is branch and add IPDR Logger.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()
        IPLogger = common.GenrateValidIPString()

        BranchName = BFun.test_1_AddBranch()
        BranchName = BranchName.testcase_01_AddBranch(common.PrereqTestCasesStatusUpdate)

        OXEName1, ValidIPp = ds.get_OXENameAndIP(False)

        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID From Branch Where BranchName = '" + BranchName + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        BranchID = str(pbxid[0])
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName1 + "' and OXEIP = '" + ValidIPp + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '' + IPLogger + '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '' + BranchID + '',
                      'MainPBXID': '' + PBXID + '',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select OXEIP From PBXDetail Where OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand1)
        primarip = cursor.fetchone()
        SQLCommand2 = ("Select OXEName From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand2)
        pbxname = cursor.fetchone()
        cursor.commit()

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if primarip[0] == ValidIP:
                        print('b')
                        if pbxname[0] == OXEName:
                            print(common.SuccessMessage)
                            status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    # Start Test Case No 02-20
    def testcase_20_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Recorder type is branch with invalid IPDR Logger..')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()
        IPLogger = '123abc123'

        BranchName = BFun.test_1_AddBranch()
        BranchName = BranchName.testcase_01_AddBranch(common.PrereqTestCasesStatusUpdate)
        OXEName1, ValidIPp = ds.get_OXENameAndIP(False)

        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID From Branch Where BranchName = '" + BranchName + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        BranchID = str(pbxid[0])
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName1 + "' and OXEIP = '" + ValidIPp + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '' + IPLogger + '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '' + BranchID + '',
                      'MainPBXID': '' + PBXID + '',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    # Start Test Case No 02-21
    def testcase_21_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System with more then 250 characters PBX Name.')

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateDesc250()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    # Start Test Case No 02-22
    def testcase_22_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Null Primary IP.')

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = ''

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    def testcase_23_AddPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Recorder type is Main with site session key.')
        # Config DB Connectivity Function calling
        # cursor  = common.StringDBConnectivity()

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 401:
                    print('401')

                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False

    def testcase_24_AddPBXConfiguration(self, TestCasesStatus=True):

        # add node with EnableNativeEncryption is false

        TestCaseID = '02-28'
        method_name = "testcase_01_AddPBXConfiguration"
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Recorder type is Main and encryption is disabled .')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',
                      'EnableNativeEncryption': "false"

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select OXEIP From PBXDetail Where OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand1)
        primarip = cursor.fetchone()
        SQLCommand2 = ("Select OXEName From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand2)
        pbxname = cursor.fetchone()
        cursor.commit()

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if primarip[0] == ValidIP:
                        print('b')
                        if pbxname[0] == OXEName:
                            print(common.SuccessMessage)
                            status = 'Passed'
                            ds.add_data(method_name, Parameters, resp, URL)
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End

    def testcase_25_AddPBXConfiguration(self, TestCasesStatus=True):

        # add node with EnableNativeEncryption is True

        TestCaseID = '02-29'
        method_name = "testcase_01_AddPBXConfiguration"
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Post Method Add PBX Configuration',
                      'Adding PBX/Node to System when Recorder type is Main.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # Generate Simple Character String Limit 10 Characters
        OXEName = common.GenrateSimpleStringLimit10()
        # Generate Valid IP
        ValidIP = common.GenrateValidIPString()

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'PCSIP': '',
                      'EnableNativeEncryption': "True"

                      }

        # Url For Add Node/PBX
        UrlForAddPBX = '/PBX/Add/'
        URL = '' + common.Domain + '' + UrlForAddPBX + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select OXEIP From PBXDetail Where OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand1)
        primarip = cursor.fetchone()
        SQLCommand2 = ("Select OXEName From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand2)
        pbxname = cursor.fetchone()
        cursor.commit()

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if primarip[0] == ValidIP:
                        print('b')
                        if pbxname[0] == OXEName:
                            print(common.SuccessMessage)
                            status = 'Passed'
                            ds.add_data(method_name, Parameters, resp, URL)
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False

        return OXEName, ValidIP
        # Test Case End


class test_2_UpdatePBXConfiguration(TestCase):
    # Url For Update Node/PBX
    UrlForUpdatePBX = '/PBX/Update/'

    # Start Test Case No 02-10
    def testcase_10_UpdatePBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Put Method Update PBX Configuration',
                      'Update PBX/Node to System with Valid Input Data.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # PBX/Node Function Calling
        OXEName, ValidIP = ds.get_OXENameAndIP(False)
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName + "' and OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        UrlForUpdatePBX = '/PBX/Update/'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'id': '' + PBXID + '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + UrlForUpdatePBX + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select OXEIP From PBXDetail Where OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand1)
        primarip = cursor.fetchone()
        SQLCommand2 = ("Select OXEName From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand2)
        pbxname = cursor.fetchone()
        cursor.commit()

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if primarip[0] == ValidIP:
                        print('b')
                        if pbxname[0] == OXEName:
                            print(common.SuccessMessage)
                            status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-11
    def testcase_11_UpdatePBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Put Method Update PBX Configuration',
                      'Update PBX/Node to System with InValid ID Data.')

        # PBX/Node Function Calling
        OXEName, ValidIP = ds.get_OXENameAndIP(False)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PBXID = '123456'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'id': '' + PBXID + '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForUpdatePBX + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End

    def testcase_24_UpdatePBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Put Method Update PBX Configuration',
                      'Update PBX/Node to System with Valid Input Data and site session key.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # PBX/Node Function Calling
        OXEName, ValidIP = ds.get_OXENameAndIP(False)
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName + "' and OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        UrlForUpdatePBX = '/PBX/Update/'
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'id': '' + PBXID + '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + UrlForUpdatePBX + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select OXEIP From PBXDetail Where OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand1)
        primarip = cursor.fetchone()
        SQLCommand2 = ("Select OXEName From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand2)
        pbxname = cursor.fetchone()
        cursor.commit()

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 401:
                    print('401')
                    if primarip[0] == ValidIP:
                        print('b')
                        if pbxname[0] == OXEName:
                            print(common.SuccessMessage)
                            status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False

        # Start Test Case No 02-11

    def testcase_27_UpdatePBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-27'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Put Method Update PBX Configuration',
                      'Update PBX/Node to System with empty data PBXID.')

        # PBX/Node Function Calling
        OXEName, ValidIP = ds.get_OXENameAndIP(False)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PBXID = ''
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryIP': '' + ValidIP + '',
                      'SecondaryIP': '',
                      'Description': '',
                      'RemoteRecorder': '',
                      'IPLogger': '',
                      'PBXName': '' + OXEName + '',
                      'BranchID': '',
                      'MainPBXID': '',
                      'id': '' + PBXID + '',
                      'PCSIP': '',

                      }

        URL = '' + common.Domain + '' + self.UrlForUpdatePBX + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End


class test_3_GetPBXConfiguration(TestCase):
    # Url For Get Node/PBX Data
    UrlForGetAllPBXData = '/PBX/Get/'
    UrlForGetSinglePBXData = '/PBX/Get/'

    # Start Test Case No 02-12
    def testcase_12_GetPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Get Method Get a PBX Data', 'Get a Single PBX/Node Data.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # PBX/Node Function Calling
        OXEName, ValidIP = ds.get_OXENameAndIP(False)
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + PBXID + '',

                      }

        URL = '' + common.Domain + '' + self.UrlForGetSinglePBXData + '' + PBXID + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if resp['list'][0]['PrimaryIP'] == ValidIP:
                        print('b')
                        if resp['list'][0]['PBXName'] == OXEName:
                            print(common.SuccessMessage)
                            status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-13
    def testcase_13_GetPBXConfiguration(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '02-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Get Method Get All PBX Data', 'Get All PBX/Node Data.')

        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,

                      }

        URL = '' + common.Domain + '' + self.UrlForGetAllPBXData + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 02-14
    def testcase_14_GetPBXConfiguration(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '02-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Get Method Get PBX Data', 'Get PBX/Node Data with Invalid ID.')

        # Header Parameters of Rest API
        PBXID = '123456'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + PBXID + '',

                      }

        URL = '' + common.Domain + '' + self.UrlForGetSinglePBXData + '' + PBXID + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End

    def testcase_25_GetPBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Get Method Get a PBX Data',
                      'Get a Single PBX/Node Data with site session key.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # PBX/Node Function Calling
        OXEName, ValidIP = ds.get_OXENameAndIP(False)
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'id': '' + PBXID + '',

                      }

        URL = '' + common.Domain + '' + self.UrlForGetSinglePBXData + '' + PBXID + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 401:
                    print('a')
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End


class test_4_DeletePBXConfiguration(TestCase):
    # Url For Delete Node/PBX
    UrlForDeletePBX = '/PBX/Delete/'

    # Start Test Case No 02-15
    # def testcase_15_DeletePBXConfiguration(self, TestCasesStatus=True):

    # TestCaseID = '02-15'
    # # Calling Common Functions
    # common = CF.CommonFunctions()
    # ds = DS.DataStorage()
    # common.Header('PBX Configuration' , 'Using Delete Method Delete a PBX Data' , 'Using Delete Method Delete a PBX Data With Valid ID.')
    # # Config DB Connectivity Function calling
    # cursor  = common.StringDBConnectivity()
    #
    # # PBX/Node Function Calling
    # OXEName, ValidIP=ds.get_OXENameAndIP(False)
    # # SQL Queries for Data Verification
    # SQLCommand = ("Select ID From PBXDetail Where OXEName = '"+OXEName+"' and OXEIP = '"+ValidIP+"';")
    # cursor.execute(SQLCommand)
    # pbxid=cursor.fetchone()
    # PBXID=str(pbxid[0])
    # cursor.commit()
    #
    # # Test Case Start Time
    # starttime = time.process_time()
    # # Header Parameters of Rest API
    # Parameters = {'AuthToken':''+common.authkey_server()+'',
    #             'AuthUser':''+common.authuser+'',
    #             'id': ''+PBXID+'',
    #
    #             }
    #
    # URL = ''+common.Domain+''+self.UrlForDeletePBX+''+PBXID+''
    # # Hit API Through Methods
    # response = requests.delete(URL, headers=Parameters)
    # # API Response in JSon Format
    # resp=response.json()
    # #showcode = str(resp['ResponseCode'])
    #
    # # Response Code Verification
    # if TestCasesStatus==True:
    #     try:
    #         if resp['ResponseCode'] == 200:
    #             print(common.SuccessMessage)
    #             status = 'Passed'
    #         else:
    #             status = 'Failed'
    #             assert False
    #
    #     # Write Output Result in Excel File
    #     finally:
    #         common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
    # else:
    #     TestCasesStatus=False
    #     # Test Case End

    # Start Test Case No 02-16
    def testcase_16_DeletePBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('PBX Configuration', 'Using Delete Method Delete a PBX Data',
                      'Using Delete Method Delete a PBX Data With InValid ID.')

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        PBXID = '123456'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + PBXID + '',

                      }

        URL = '' + common.Domain + '' + self.UrlForDeletePBX + '' + PBXID + ''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End

    def testcase_26_DeletePBXConfiguration(self, TestCasesStatus=True):

        TestCaseID = '02-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ds = DS.DataStorage()
        common.Header('PBX Configuration', 'Using Delete Method Delete a PBX Data',
                      'Using Delete Method Delete a PBX Data With session key.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()

        # PBX/Node Function Calling
        OXEName, ValidIP = ds.get_OXENameAndIP(True)
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName + "' and OXEIP = '" + ValidIP + "';")
        cursor.execute(SQLCommand)
        pbxid = cursor.fetchone()
        PBXID = str(pbxid[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'id': '' + PBXID + '',

                      }

        URL = '' + common.Domain + '' + self.UrlForDeletePBX + '' + PBXID + ''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 401:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus = False
            # Test Case End
