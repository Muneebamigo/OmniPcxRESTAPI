'''
Created on Jul 4, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time,requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from openpyxl import load_workbook
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from test_Provisioning import test_06_SiteAgentConfiguration as agentfunctions
from Key import config

SheetName=	'5-Teams Configuration'

class Test_1_AddTeamCofiguration(TestCase):
    
    # Url For Add Team
    UrlAddTeam = '/Team/Add'
    
    # Start Test Case No 05-01
    def test_01_AddTeam(self, TestCasesStatus=True):
        
        TestCaseID = '05-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Teams valid name and description')
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': ''+TeamName+'',
                      'Description': ''+TeamDesc+''
                      
                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
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
            TestCasesStatus=False

        return TeamName
        # Test Case End

    # Start Test Case No 05-03
    def test_03_AddTeamwithSpeciaChar(self):

        TestCaseID = '05-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team with Special Char', 'Add Teams')
        # Generate Special Characters
        TeamNameWithSpecial = common.GenerateSpecialChar()
        # Generate Simple Character String Limit 10 Characters
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': ''+TeamNameWithSpecial+'$-test',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        URL = '' + common.Domain + '' + self.UrlAddTeam + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
                    # Test Case End

    # Start Test Case No 05-02
    def test_02_AddTeamwith250Char(self):

        TestCaseID = '05-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team with 251 char', 'Add Teams')

        # Generate Simple Character String Limit 10 Characters
        TeamName = common.GenrateSimpleStringLimit10()
        # Generate Characters Limit 250
        TeamDesc250Char = common.GenrateDesc250()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': ''+TeamName+'',
                      'Description': ''+TeamDesc250Char+''

                     }
        # Url For Add Team
        URL = ''+common.Domain+''+self.UrlAddTeam+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
                    # Test Case End

    # Start Test Case No 05-12
    def test_04_AddTeamWithDuplicateName(self, TestCasesStatus=True):

        TestCaseID = '05-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Teams with duplicate team name')

        TeamName=Test_1_AddTeamCofiguration.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)
        # Generate Simple Character String Limit 10 Characters
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': ''+TeamName+'',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:

            try:
                if resp['ResponseCode'] == 409:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 05-13
    def test_05_AddTeamWithinvalidSiteCode(self, TestCasesStatus=True):

        TestCaseID = '05-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Teams with Invalid Site Code')

        TeamName= common.GenrateSimpleStringLimit10()
        # Generate Simple Character String Limit 10 Characters
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '123456',
                      'Name': ''+TeamName+'',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:

            try:
                if resp['ResponseCode'] == 500:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 05-14
    def test_14_AddTeam(self, TestCasesStatus=True):

        TestCaseID = '05-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Teams with empty team')

        # Generate Simple Character String Limit 10 Characters
        TeamName = ''
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': ''+TeamName+'',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
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
            TestCasesStatus=False

    # Start Test Case No 05-15
    def test_15_AddTeam(self, TestCasesStatus=True):

        TestCaseID = '05-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Teams valid name and description when server role configured as secondary.')

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': ''+TeamName+'',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:

            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus=False
        # Test Case End

    # Start Test Case No 05-16
    def test_16_AddTeam(self, TestCasesStatus=True):

        TestCaseID = '05-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Teams valid name and description when server role configured as branch.')

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': ''+TeamName+'',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:

            try:
                if resp['ResponseCode'] == 403:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus=False
        # Test Case End


    # Start Test Case No 05-17
    def test_17_AddTeam(self, TestCasesStatus=True):

        TestCaseID = '05-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Teams name is contains double quotes.')

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': 'test"team"test',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
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
            TestCasesStatus=False

        # Test Case End
    def test_18_AddTeam(self, TestCasesStatus=True):

        TestCaseID = '05-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Calling Adding Method of Team', 'Add Team in the system with Server Session Key')

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        TeamDesc = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Name': 'test"team"test',
                      'Description': ''+TeamDesc+''

                     }
        # Url For Add Team
        UrlAddTeam = '/Team/Add/'
        URL = ''+common.Domain+''+UrlAddTeam+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:

            try:
                if resp['ResponseCode'] == 401:
                    print(common.SuccessMessage)
                    status ='Passed'

                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus=False

        # Test Case End

class Test_2_UpdateTeamCofiguration(TestCase):

    # Url For Update Team
    UrlUpdateTeam = '/Team/Update/'

    # Start Test Case No 05-04
    def test_04_UpdateTeamConfiguration(self, TestCasesStatus=True):

        TestCaseID = '05-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Calling Update Method', 'Updating Team Configuration with valid ID')
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        TeamName =  common.GenrateSimpleStringLimit10()
        TeamDesc =  common.GenrateSimpleStringLimit10()
        # AddTeamConfiguration Function Calling
        Teamname = Test_1_AddTeamCofiguration.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)

        # SQL Queries for Data Verification
        SQLCommand = ("Select Groupid from Groups Where Name = '"+Teamname+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                          'AuthUser':config.auth_user,
                          'Id':''+TeamID+'',
                          'SiteCode': '',
                          'Name': ''+TeamName+'',
                          'Description': ''+TeamDesc+''
                         }

        # Url For Update Team
        URL = ''+common.Domain+''+self.UrlUpdateTeam+''
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
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        # Test Case End

        else:
            TestCasesStatus=False
            # Test Case End

    # Start Test Case No 05-05
    def test_05_UpdateTeamConfigurationwithInvalidID(self):

        TestCaseID = '05-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Calling Update Method with invalidID', 'Updating Team Configuration')
        # Generate Simple Character String Limit 10 Characters
        TeamName =  common.GenrateSimpleStringLimit10()
        TeamDesc =  common.GenrateSimpleStringLimit10()
        TeamID = '99999'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                          'AuthUser': config.auth_user,
                          'Id':'' + TeamID + '',
                          'SiteCode': '',
                          'Name': '' +TeamName+ '',
                          'Description': '' +TeamDesc+ ''
                         }
        # Url For Update Team
        URL = ''+common.Domain+''+self.UrlUpdateTeam+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
                    # Test Case End
    def test_06_UpdateTeamConfiguration(self, TestCasesStatus=True):

        TestCaseID = '05-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Calling Update Method', 'Update Team in the system with Server Session Key')
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        TeamName =  common.GenrateSimpleStringLimit10()
        TeamDesc =  common.GenrateSimpleStringLimit10()
        # AddTeamConfiguration Function Calling
        Teamname = Test_1_AddTeamCofiguration.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)

        # SQL Queries for Data Verification
        SQLCommand = ("Select Groupid from Groups Where Name = '"+Teamname+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        TeamID = str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser':config.auth_user,
                          'Id':''+TeamID+'',
                          'SiteCode': '',
                          'Name': ''+TeamName+'',
                          'Description': ''+TeamDesc+''
                         }

        # Url For Update Team
        URL = ''+common.Domain+''+self.UrlUpdateTeam+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
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
                        # Test Case End

        else:
            TestCasesStatus=False
            # Test Case End

class Test_3_GetTeamCofiguration(TestCase):

    # Url For Get Team
    UrlGetTeam = '/Team/Get/'
    UrlGetTeamById = '/Team/Get/'

    # Start Test Case No 05-09
    def test_09_GetCofiguration(self):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '05-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Getting', 'Get All Teams')

        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                     }

        # Url For Get Team
        URL = ''+common.Domain+''+self.UrlGetTeam+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
                    # Test Case End

    # Start Test Case No 05-10
    def test_010_GetTeamConfigurationByID(self):

        TestCaseID = '05-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        # Calling Common Functions
        common.Header('Team Module', 'Calling Get Team By Id Method', 'Get By Id Team Configuration')
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # AddTeamConfiguration Function Calling
        TeamIDd = Test_1_AddTeamCofiguration.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)

        # SQL Queries for Data Verification
        SQLCommand = ("Select Groupid from Groups Where Name = '"+TeamIDd+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        TeamID = str(vals[0])

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                          'AuthUser': config.auth_user,
                          'SiteCode': '',
                          'Id': ''+TeamID+'',
                         }
        # Url For Get Team
        URL = ''+common.Domain+''+self.UrlGetTeamById+''+TeamID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
                    # Test Case End

    # Start Test Case No 05-11
    def test_011_GetTeamConfigurationByID(self):

        TestCaseID = '05-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Calling Get Team By Id Method', 'Get By Invalid team ID')

        # Header Parameters of Rest API
        TeamID = '123456'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken': config.sessionkeysite,
                          'AuthUser': config.auth_user,
                          'SiteCode': '',
                          'Id': ''+TeamID+'',
                         }
        # Url For Get Team
        URL = ''+common.Domain+''+self.UrlGetTeamById+''+TeamID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        # Response Code Verification
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
                    # Test Case End
    def test_20_GetCofiguration(self):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '05-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Teams', 'Getting', 'Get Team from the system with Server Session Key')

        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                     }

        # Url For Get Team
        URL = ''+common.Domain+''+self.UrlGetTeam+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        #showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 401:
                print(common.SuccessMessage)
                status ='Passed'

            else:
                status = 'Failed'
                assert False
        # Write Output Result in Excel File       
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
class Test_4_DeleteTeamCofiguration(TestCase):   
    
    # Url For Delete Team
    UrlDeleteTeam = '/Team/Delete/'

    # Start Test Case No 05-06
    def test_06_DeleteTeamConfiguration(self):
        
        TestCaseID = '05-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Deleting', 'Deleting Team with valid id when agents are not associated')     
        # Config DB Connectivity Function calling

        cursor = common.DBConnectivity()
        # AddTeamConfiguration Function Calling
        TeamIDd = Test_1_AddTeamCofiguration.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)
        
        # SQL Queries for Data Verification
        SQLCommand = ("Select Groupid from Groups Where Name = '"+TeamIDd+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        TeamID = str(vals[0])
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'Id': ''+TeamID+'',
                     }
        # Url For Delete Team
        URL = ''+common.Domain+''+self.UrlDeleteTeam+''+TeamID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 200:
                print(common.SuccessMessage) 
                status ='Passed'
                    
            else:
                status  = 'Failed'
                
        # Write Output Result in Excel File
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End

    # Start Test Case No 05-08
    def test_08_InvalidDeleteTeamConfiguration(self):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '05-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Deleting', 'Deleting Team with invalid id')
        # Header Parameters of Rest API
        TeamID = '123456'
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'Id': ''+TeamID+'',
                     }
        # Url For Delete Team
        URL = '' + common.Domain + '' + self.UrlDeleteTeam +''+TeamID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 400:
                        print(common.SuccessMessage)
                        status ='Passed'
                    
            else:
                status  = 'Failed'
        # Write Output Result in Excel File      
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End
            
    # Start Test Case No 05-07
    def test_07_DeleteTeamConfigurationWithAgent(self, TestCasesStatus=True):
        
        TestCaseID = '05-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Deleting team', 'Deleting Team when associated with agents')
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        
        # Agent Function Calling
        AgentFunction = agentfunctions.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid= AgentFunction.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username=username
        ExtVal=ExtVal
        pbxid=pbxid
        
        SQLCommand1 = ("Select Groupid from Groups Where Name = '"+teamname+"';")
        cursor.execute(SQLCommand1)
        teamid = cursor.fetchone()
        TeamID = str(teamid[0]) 
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'id': ''+TeamID+'',
                     }
        # Url For Delete Team
        URL = '' + common.Domain + '' + self.UrlDeleteTeam +''+TeamID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 409:
                    print(common.SuccessMessage) 
                    status ='Passed'
                        
                else:
                    status  = 'Failed'
                    
            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            # Test Case End
            
    def test_21_DeleteTeamConfiguration(self):
        
        TestCaseID = '05-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Team Module', 'Deleting', 'Delete Team in the system with Server Session Key')     
        # Config DB Connectivity Function calling

        cursor = common.DBConnectivity()
        # AddTeamConfiguration Function Calling
        TeamIDd = Test_1_AddTeamCofiguration.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)
        
        # SQL Queries for Data Verification
        SQLCommand = ("Select Groupid from Groups Where Name = '"+TeamIDd+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        TeamID = str(vals[0])
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'Id': ''+TeamID+'',
                     }
        # Url For Delete Team
        URL = ''+common.Domain+''+self.UrlDeleteTeam+''+TeamID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        # Response Code Verification
        try:
            if resp['ResponseCode'] == 401:
                print(common.SuccessMessage) 
                status ='Passed'
                    
            else:
                status  = 'Failed'
                
        # Write Output Result in Excel File
        finally:
            common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                    # Test Case End