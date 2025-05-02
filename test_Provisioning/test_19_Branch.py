'''
Created on Jul 5, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
from InputDataFiles import InputData as BranchInputData
from test_Provisioning import test_13_SMTPSettings as SMTPSettings
from test_Provisioning import test_01_SystemSettings as SSF
from test_Provisioning import test_02_PBXConfiguration as PBXF
from test_Provisioning import test_03_PacketizerConfiguration as PFun
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config

SheetName = '19-Branch'


class test_1_AddBranch(TestCase):

    # Start Test Case No 19-01
    def testcase_01_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Transfer URL Type is FTP/0 and Schedule Type is 0/Immediate.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()

        systemsettingsfunction = SSF.test_1_UpdateSystemSettings()
        systemsettingsfunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Update SMTP Settings function Calling
        smtpSettingsFunc = SMTPSettings.UpdateSMTPSettings()
        smtpSettingsFunc.testcase_01_UpdateSMTPSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '0',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

        return BranchName

    # Start Test Case No 19-02
    def testcase_02_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Transfer URL Type is FTP/0 and Schedule Type is 0/Immediate and server role as secondary configured.')

        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()

        # Update SMTP Settings function Calling
        smtpSettingsFunc = SMTPSettings.UpdateSMTPSettings()
        smtpSettingsFunc.testcase_01_UpdateSMTPSettings(common.PrereqTestCasesStatusUpdate)

        systemsettingsfunction = SSF.test_1_UpdateSystemSettings()
        systemsettingsfunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    # Start Test Case No 19-03
    def testcase_03_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Transfer URL Type is FTP/0 and Schedule Type is 0/Immediate and server role as branch configured.')

        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()

        # Update SMTP Settings function Calling
        smtpSettingsFunc = SMTPSettings.UpdateSMTPSettings()
        smtpSettingsFunc.testcase_01_UpdateSMTPSettings(common.PrereqTestCasesStatusUpdate)

        systemsettingsfunction = SSF.test_1_UpdateSystemSettings()
        systemsettingsfunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    # Start Test Case No 19-04
    def testcase_04_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Transfer URL Type is Secure FTP/1 and Schedule Type is 0/Immediate.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()

        # Update SMTP Settings function Calling
        smtpSettingsFunc = SMTPSettings.UpdateSMTPSettings()
        smtpSettingsFunc.testcase_01_UpdateSMTPSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '1',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Config DB Connectivity Function calling 
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        # SQL Queries for Data Verification
        SQLCommand = "SELECT BranchName FROM Branch WHERE BranchName = '" + BranchName + "' LIMIT 1;"
        cursor.execute(SQLCommand)

        Name = cursor.fetchone()

        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    if Name[0] == BranchName:
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

        return BranchName
        # Test Case End

    # Start Test Case No 19-05
    def testcase_05_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Transfer URL Type is Secure FTP/1 and Schedule Type is 1/After Every.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()

        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '1',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '1',
                      'Interval': '3',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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
            # Test Case End

    # Start Test Case No 19-06
    def testcase_06_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch', 'Adding Branch to system with existing branch name.')
        # Calling Input Data File      
        ssinputdata = BranchInputData.InputData()
        # Add Branch Function calling
        BranchName = test_1_AddBranch.testcase_01_AddBranch(common.PrereqTestCasesStatusUpdate)
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '1',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '1',
                      'Interval': '3',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
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

    def testcase_14_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Transfer URL Type is empty.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    def testcase_15_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch', 'Adding Branch to system when Transfer URL is empty.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    # Start Test Case No 19-16
    def testcase_16_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system with invalid TransferUserName.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': 'abc123abc123',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    # Start Test Case No 19-17
    def testcase_17_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch', 'Adding Branch to system with invalid ScheduleType.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': 'acb123abc123',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Config DB Connectivity Function calling

        status = 'Failed'
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

    # Start Test Case No 19-18
    def testcase_18_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch', 'Adding Branch to system with NULL/Empty LoggerStatus.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Config DB Connectivity Function calling

        status = 'Failed'
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

    # Start Test Case No 19-19
    def testcase_19_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch', 'Adding Branch to system with Null/Empty ScheduleType.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Config DB Connectivity Function calling

        status = 'Failed'
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

    # Start Test Case No 19-20
    def testcase_20_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Schedule Type is 1 and interval value empty/NULL.')
        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '1',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    # Start Test Case No 19-21
    def testcase_21_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when Schedule type value is 2 and time value is empty/NULL.')

        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        BranchName = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '2',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    # Start Test Case No 19-22
    def testcase_22_AddBranch(self, TestCasesStatus=True):

        TestCaseID = '19-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Post Method Add Branch',
                      'Adding Branch to system when loggerstatus is 0 disabled.')

        # Calling Input Data File
        ssinputdata = BranchInputData.InputData()
        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'BranchName': '' + BranchName + '',
                      'Email': '' + ssinputdata.BranchEmail + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '0',

                      }
        # Url
        UrlForAddBranch = '/Branch/Add/'
        URL = '' + common.Domain + '' + UrlForAddBranch + ''
        response = requests.post(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

        return BranchName


class test_2_GetBranch(TestCase):
    ssinputdata = BranchInputData.InputData
    UrlForGetAllBranchData = '/Branch/Get'
    UrlForGetSingleBranchData = '/Branch/Get/'

    # Start Test Case No 19-07
    def test_07_GetBranch(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '19-07'

        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Get Method Get Branch', 'Getting all list of Branch exists in the system.')
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user

                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForGetAllBranchData + ''
        response = requests.get(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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
            # Test Case End

    # Start Test Case No 19-08
    def test_08_GetBranch(self, TestCasesStatus=True):

        TestCaseID = '19-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Get Method Get Branch', 'Getting Branch exists in the system By valid Id.')

        # Add Branch Function calling
        BranchName = test_1_AddBranch.testcase_01_AddBranch(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID from Branch WHERE BranchName='" + BranchName + "'")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        branchId = str(vals[0])

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Id': '' + branchId + '',
                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForGetSingleBranchData + branchId + ''
        response = requests.get(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

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
            # Test Case End

    # Start Test Case No 19-09
    def test_09_GetBranch(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '19-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Get Method Get Branch', 'Getting Branch exists in the system By invalid Id.')

        branchId = '123456'
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Id': '' + branchId + '',
                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForGetSingleBranchData + branchId + ''
        response = requests.get(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

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


class test_3_UpdateBranch(TestCase):
    # Calling Input Data File
    ssinputdata = BranchInputData.InputData
    # Url for Update Branch
    UrlForUpdateBranch = '/Branch/Update/'

    # Start Test Case No 19-10
    def test_10_UpdateBranch(self, TestCasesStatus=True):

        TestCaseID = '19-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Update Method Update Branch', 'Updating Branch With invalid ID value.')

        # Generate Simple Character String Limit 10 Characters
        BranchName = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        branchId = '123456'
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': '' + branchId + '',
                      'BranchName': '' + BranchName + '',
                      'Email': '' + common.GenerateEmail() + '',
                      'TransferURLType': '0',
                      'TransferURL': '172.20.0..',
                      'TransferUsername': '' + self.ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + self.ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }

        URL = '' + common.Domain + '' + self.UrlForUpdateBranch + ''
        response = requests.put(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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

    # Start Test Case No 19-11
    def test_11_UpdateBranch(self, TestCasesStatus=True):

        TestCaseID = '19-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Update Method Update Branch', 'Updating Branch with valid data ID.')
        # Add branch function Calling
        BranchName = test_1_AddBranch.testcase_01_AddBranch(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID from Branch WHERE BranchName='" + BranchName + "'")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        branchId = str(vals[0])
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': '' + branchId + '',
                      'BranchName': '' + common.GenrateSimpleStringLimit10() + '',
                      'Email': '' + common.GenerateEmail() + '',
                      'TransferURLType': '0',
                      'TransferURL': '' + self.ssinputdata.BranchTransferURL + '',
                      'TransferUsername': '' + self.ssinputdata.BranchTransferUsername + '',
                      'TransferPassword': '' + self.ssinputdata.BranchTransferPassword + '',
                      'PassiveTransferEnabled': 'False',
                      'SSLEnabledForTransfer': 'False',
                      'ScheduleType': '0',
                      'Interval': '',
                      'Time': '',
                      'LoggerStatus': '1',

                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForUpdateBranch + ''
        response = requests.put(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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
            # Test Case End


class test_4_DeleteBranch(TestCase):
    # Url for Delete Branch
    UrlForDeleteBranch = '/Branch/Delete/'

    # Start Test Case No 19-12
    def test_12_DeleteBranch(self, TestCasesStatus=True):

        TestCaseID = '19-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Delete Method Delete Branch',
                      'Deleting Branch With valid ID when branch is active.')

        # Add branch function Calling
        BranchName = test_1_AddBranch.testcase_04_AddBranch(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID from Branch WHERE BranchName='" + BranchName + "'")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        branchId = str(vals[0])
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + branchId + '',

                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForDeleteBranch + branchId + ''
        response = requests.delete(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

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

    # Start Test Case No 19-13      
    def test_13_DeleteBranch(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '19-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Delete Method Delete Branch', 'Deleting Branch With Invalid ID')

        branchId = '123456'
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + branchId + '',

                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForDeleteBranch + branchId + ''
        response = requests.delete(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 19-23
    def test_23_DeleteBranch(self, TestCasesStatus=True):

        TestCaseID = '19-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Delete Method Delete Branch',
                      'Deleting Branch With valid ID when status is disabled.')

        # Add branch function Calling
        BranchName = test_1_AddBranch.testcase_22_AddBranch(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID from Branch WHERE BranchName='" + BranchName + "'")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        branchId = str(vals[0])
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + branchId + '',

                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForDeleteBranch + branchId + ''
        response = requests.delete(URL, headers=Parameters)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

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
            # Test Case End

    # Start Test Case No 19-24
    def test_24_DeleteBranch(self, TestCasesStatus=True):

        TestCaseID = '19-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Delete Method Delete Branch', 'Deleting Branch that is associated with node.')

        NodeFunction = PBXF.test_1_AddPBXConfiguration()
        OXEName, BranchID = NodeFunction.testcase_09_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + BranchID + '',

                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForDeleteBranch + BranchID + ''
        response = requests.delete(URL, headers=Parameters)
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

    # Start Test Case No 19-25
    def test_25_DeleteBranch(self, TestCasesStatus=True):

        TestCaseID = '19-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Branch', 'Using Delete Method Delete Branch',
                      'Deleting Branch that is associated with packetizer.')

        PacketizerFunction = PFun.test_1_AddPacketizerConfiguration()
        PcktIP, BranchID = PacketizerFunction.testcase_06_AddPacketizerConfiguration(common.PrereqTestCasesStatusUpdate)
        PcktIP = PcktIP

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'id': '' + BranchID + '',

                      }
        # Url
        URL = '' + common.Domain + '' + self.UrlForDeleteBranch + BranchID + ''
        response = requests.delete(URL, headers=Parameters)
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
