'''
Created on Sep 4, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from openpyxl import load_workbook
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config

SheetName = '50-Speech Analytics'


class test_1_UpdateSpeechAnalytics(TestCase):
    # Url For UpdateSMTP Settings 
    UrlForUpdateSpeechAnalytics = '/SpeechAnalytics/Update'

    # Start Test Case No 50-01
    def testcase_01_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics With valid input when Speech Type is 0 and FrequencyType 0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        SpeechType = '0'
        MinRange = '1'
        MaxRange = '10'
        FrequencyPercent = '30'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-02
    def testcase_02_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics With invalid/Non Existing Site Code.')

        SpeechType = '0'
        MinRange = '0'
        MaxRange = '10'
        FrequencyPercent = '30'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '123456',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 500:
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

    # Start Test Case No 50-03
    def testcase_03_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics With valid input when Speech Type is 1 and FrequencyType 0.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        SpeechType = '1'
        MinRange = '11'
        MaxRange = '20'
        FrequencyPercent = '10'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-04
    def testcase_04_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics With valid input when Speech Type is 2 and FrequencyType 0.')

        SpeechType = '2'
        MinRange = '21'
        MaxRange = '30'
        FrequencyPercent = '15'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-05
    def testcase_05_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics With valid input when Speech Type is 3 and FrequencyType 0.')

        SpeechType = '3'
        MinRange = '31'
        MaxRange = '40'
        FrequencyPercent = '10'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-06
    def testcase_06_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics With valid input when Speech Type is 0 and FrequencyType 1.')

        SpeechType = '0'
        MinRange = '41'
        MaxRange = '50'
        FrequencyPercent = '15'
        FrequencyChunks = '5'
        FrequencyType = '1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-07
    def testcase_07_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics With valid input when Speech Type is 2 and FrequencyType 1.')

        SpeechType = '2'
        MinRange = '51'
        MaxRange = '99'
        FrequencyPercent = '4'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-08
    def testcase_08_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics when MaxRange is Null/Empty.')

        SpeechType = '3'
        MinRange = '31'
        MaxRange = ''
        FrequencyPercent = '10'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-09
    def testcase_09_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics When MinRange is greater then MaxRange.')

        SpeechType = '4'
        MinRange = '99'
        MaxRange = '10'
        FrequencyPercent = '15'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-10
    def testcase_10_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics When SpeechType is 3 and FrequencyType value is 1.')

        SpeechType = '3'
        MinRange = '51'
        MaxRange = '99'
        FrequencyPercent = '4'
        FrequencyChunks = '5'
        FrequencyType = '1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-11
    def testcase_11_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics When Isenabled value is Null.')

        SpeechType = '3'
        MinRange = '31'
        MaxRange = '40'
        FrequencyPercent = '10'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': '',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-12
    def testcase_12_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics with FrequencyPercentage greater then 100.')

        SpeechType = '4'
        MinRange = '41'
        MaxRange = '50'
        FrequencyPercent = '200'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-13
    def testcase_13_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics when speech type value is Null.')

        SpeechType = ''
        MinRange = '51'
        MaxRange = '99'
        FrequencyPercent = '4'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
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

    # Start Test Case No 50-14
    def testcase_14_UpdateSpeechAnalytics(self, TestCasesStatus=True):

        TestCaseID = '50-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Update Speech Analytics', 'Update Speech Analytics Through Put Method',
                      'Update Speech Analytics when server role as branch configured.')
        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        SpeechType = '0'
        MinRange = '1'
        MaxRange = '10'
        FrequencyPercent = '30'
        FrequencyChunks = '5'
        FrequencyType = '0'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'SpeechType': '' + SpeechType + '',
                      'MinRange': '' + MinRange + '',
                      'MaxRange': '' + MaxRange + '',
                      'FrequencyPercent': '' + FrequencyPercent + '',
                      'FrequencyChunks': '' + FrequencyChunks + '',
                      'FrequencyType': '' + FrequencyType + '',
                      'IsEnabled': 'True',

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForUpdateSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
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


class test_2_GetSpeechAnalytics(TestCase):
    # Url For UpdateSMTP Settings
    UrlForGetSpeechAnalytics = '/SpeechAnalytics/Get'

    # Start Test Case No 50-15
    def testcase_01_GetSpeechAnalytics(self, TestCasesStatus=True):
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '50-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Get Speech Analytics', 'Get Speech Analytics Through Get Method',
                      'Get Speech Analytics With valid input.')

        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,

                      }

        # URL
        URL = '' + common.Domain + '' + self.UrlForGetSpeechAnalytics + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
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
