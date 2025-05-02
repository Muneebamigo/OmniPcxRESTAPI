'''
Created on Jul 26, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
from Key import config
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
SheetName=	'23-Change password'

class test_1_UpdateChangePassword(TestCase):

    # Url For Update Password

    UrlForChangePassword = '/ChangePassword/Update'


    # Start Test Case No 23-01
    def testcase_01_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update Change Password with valid data for Administration type server.')

        # Header Parameters of Rest API
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@1234'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '0',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

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

    def testcase_11_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update Change Password with valid data for Administration type server with site session key.')

        # Header Parameters of Rest API
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@1234'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '0',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 23-02
    def testcase_02_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update password with valid data for Administration type Site.')

        # Header Parameters of Rest API
        SiteCode = ''
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@1234'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '1',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

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

    def testcase_12_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update password with valid data for Administration type Site.')

        # Header Parameters of Rest API
        SiteCode = ''
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@1234'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '1',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False

    # Start Test Case No 23-03
    def testcase_03_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update Change Password new password same as old password for Administration type Server.')

        # Header Parameters of Rest API
        SiteCode = ''
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@123'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '0',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 23-04
    def testcase_04_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update Change Password with valid data  for Administration type Site when provided Site Code 010001.')

        # Header Parameters of Rest API
        SiteCode='010001'
        OldPassword = 'Admin@1234'
        NewPassword = 'Admin@12345'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '1',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

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

    # Start Test Case No 23-05
    def testcase_05_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update Change Password with in valid or incorrect New Password When Administrator type is Site.')

        # Header Parameters of Rest API
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '1',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 23-06
    def testcase_06_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'update new password same as old password for Administration type Site.')

        # Header Parameters of Rest API
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@123'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '1',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 23-07
    def testcase_07_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update password with incorrect or invalid New Password   When Administrator type is Server.')

        # Header Parameters of Rest API
        OldPassword = 'Admin@123'
        NewPassword = 'Admin'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '0',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 23-08
    def testcase_08_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update Change Password for Administration type Site when provided invalid Site Code 1234567.')

        # Header Parameters of Rest API
        SiteCode='1234567'
        OldPassword = 'Admin@1234'
        NewPassword = 'Admin@12345'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '1',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 23-09
    def testcase_09_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update password with valid data for Administration type Site when same new password as used in last 4 times in password record.')

        # Header Parameters of Rest API
        SiteCode = '010001'
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@123'
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '1',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 23-10
    def testcase_10_UpdateChangePassword(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '23-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Change Password' , 'Update Change Password' , 'Update password with valid data for Administrator type is Server when same new password as used in last 4 times in password record.')

        # Header Parameters of Rest API
        Parameterss = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'OldPassword': 'Admin@123',
                      'NewPassword': 'Admin@123',
                      'Administration': '0',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        requests.put(URL, headers=Parameterss)

        # Header Parameters of Rest API
        OldPassword = 'Admin@123'
        NewPassword = 'Admin@1234'
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'OldPassword': ''+OldPassword+'',
                      'NewPassword': ''+NewPassword+'',
                      'Administration': '0',

                    }
        # Url For Update Password
        URL = ''+common.Domain+''+self.UrlForChangePassword+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
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
            TestCasesStatus=False
            # Test Case End


#         configdb=common.StringDBConnectivity()
#         simpledb=common.DBConnectivity()
#
#         # SQL Queries For Update Config DB Admin password
#         SQLCommand1 = ("Update Users SET Password='admin' where Username = 'admin' ;")
#         configdb.execute(SQLCommand1)
#         configdb.commit()
#         # SQL Queries For delete Last 4 Updated Password Records
#         SQLCommand2 = ("Delete from OPR_UserPasswords ;")
#         configdb.execute(SQLCommand2)
#         configdb.commit()
#
#         # SQL Queries For Update Simple DB Admin password
#         SQLCommand3 = ("Update Users SET Password='admin' where Username = 'admin' ;")
#         simpledb.execute(SQLCommand3)
#         simpledb.commit()
#         # SQL Queries For delete Last 4 Updated Password Records
#         SQLCommand4 = ("Delete from OPR_UserPasswords ;")
#         simpledb.execute(SQLCommand4)
#         simpledb.commit()