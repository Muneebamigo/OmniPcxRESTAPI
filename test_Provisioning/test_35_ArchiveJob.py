'''
Created on Oct 15, 2018

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
from test_Provisioning import test_01_SystemSettings as SSF
from test_Provisioning import test_51_ArchiveSchedule as ASF
from Key import config

SheetName=	'35-Archive Job'

class test_1_AddArchiveJob(TestCase):
    
    # Start Test Case No 35-01
    def testcase_01_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data.')
        
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
                
        return Title   
                
    # Test Case End
    
    # Start Test Case No 35-02
    def testcase_02_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when TextSearchCriteria is 0/Text starts with.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=common.GenrateSimpleStringLimit10()
        LastName=common.GenrateSimpleStringLimit10()
        Device='1234'
        CalledBy='1234'
        CalledTo='12345'
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '0',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '0',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '0',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '0',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '0',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-03
    def testcase_03_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when TextSearchCriteria is 2/Text Contains.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=common.GenrateSimpleStringLimit10()
        LastName=common.GenrateSimpleStringLimit10()
        Device='1234'
        CalledBy='1234'
        CalledTo='12345'
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '2',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '2',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '2',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '2',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '2',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-04
    def testcase_04_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when CallDirectionCriteria is 0/Inbound.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '0',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-05
    def testcase_05_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when CallDirectionCriteria is 1/Outbound.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '1',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-06
    def testcase_06_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when CallDurationCriteria is 0/LessThan.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=time.strftime("%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '0',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-07
    def testcase_07_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when CallDirectionCriteria is 2/Equals To.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=time.strftime("%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '2',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    
    # Start Test Case No 35-08
    def testcase_08_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid/wrong Time format.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration='123abc'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '2',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-09
    def testcase_09_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when CallDateTimeCriteria is 5/User Specified.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        StartDate='20/01/2019 12:12:13'
        EndDate='21/01/2019 12:12:13'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '5',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-10
    def testcase_10_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with all valid Data when CallDateTimeCriteria is 4/Older Than N Days.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '4',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '2',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-11
    def testcase_11_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid Data when duplicate Title.')
        Title=test_1_AddArchiveJob.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-12
    def testcase_12_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid Data when empty/Null Title.')
        
        # Generate Simple Character String Limit 10 Characters
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': '',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-13
    def testcase_13_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid or non existing SiteCode.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '1234567',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    # Start Test Case No 35-14
    def testcase_14_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid Data when Empty/Null FirstNameCriteria value.')
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '0',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '0',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    
    # Start Test Case No 35-24
    def testcase_15_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with Null ParamNumberOfDays parameter.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '4',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    
    # Start Test Case No 35-25
    def testcase_16_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid/wrong format when CallDateTimeCriteria is 5/User Specified.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        StartDate='59332019 121213'
        EndDate='69972019 121213'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '5',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    
    # Start Test Case No 35-26
    def testcase_17_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid Data date is not older than 24 hours when CallDateTimeCriteria is 5/User Specified.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        StartDate=time.strftime("%d/%m/%Y" "%H:%M:%S")
        EndDate=time.strftime("%d/%m/%Y" "%H:%M:%S")
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '5',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    
    # Start Test Case No 35-27
    def testcase_18_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-27'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job with invalid Data From date is older than To date when CallDateTimeCriteria is 5/User Specified.')
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        StartDate='21/01/2019 12:12:13'
        EndDate='20/01/2019 12:12:13'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '5',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
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
    
    
    # Start Test Case No 35-28
    def testcase_19_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-28'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job when server role configured as secondary.')
        
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
                TestCasesStatus=False 
                
        return Title   
                
    # Test Case End
    
    
    # Start Test Case No 35-29
    def testcase_20_AddArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-29'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Post Method to Add Archive Job' , 'Add Archive Job when server role configured as branch.')
        
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Title = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforAddArchiveJob = '/Job/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
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
                TestCasesStatus=False 
                
        return Title 
                
    # Test Case End
    
 
class test_2_UpdateArchiveJob(TestCase):
    
    # Start Test Case No 35-15
    def testcase_01_UpdateArchiveJob(self, TestCasesStatus=True):
        TestCaseID = '35-15'

        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job', 'Using Put Method to Update Archive Job',
                      'Update Archive Job with valid Data and valid ID.')

        # Retry logic for the AddArchiveJob test case
        retry_attempts = 1  # Number of retry attempts (1 means it will try once again)
        success = False
        while retry_attempts >= 0:
            try:
                # Get Title from the Add Archive Job test case
                Title = test_1_AddArchiveJob.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)
                success = True  # If no exception occurs, we set success to True
                break  # Exit the loop if it works successfully

            except Exception as e:
                print(f"Error executing test_1_AddArchiveJob.testcase_01_AddArchiveJob: {e}")
                retry_attempts -= 1
                if retry_attempts == 0:
                    print("Retry attempts exhausted.")
                    raise  # Re-raise the exception if we have no retry attempts left

                print("Retrying the Add Archive Job...")

        # If the Title was successfully retrieved
        if success:
            # Config DB Connectivity Function calling
            cursor = common.DBConnectivity()

            # SQL Queries for Data Verification
            SQLCommand2 = f"Select JobId From Jobs Where Title = '{Title}';"
            cursor.execute(SQLCommand2)
            vals = cursor.fetchone()
            ID = str(vals[0])
            cursor.commit()

            # Generate Simple Character String Limit 10 Characters
            Description = common.GenrateSimpleStringLimit10()
            FirstName = ''
            LastName = ''
            Device = ''
            CalledBy = ''
            CalledTo = ''
            Duration = ''

            # Test Case Start Time
            starttime = time.process_time()

            # Header Parameters of Rest API
            Parameters = {
                'AuthToken': config.sessionkeysiteUser,
                'AuthUser': config.auth_user,
                'SiteCode': '',
                'ID': ID,
                'Title': Title,
                'Description': Description,
                'FirstName': FirstName,
                'FirstNameCriteria': '4',
                'LastName': LastName,
                'LastNameCriteria': '4',
                'Device': Device,
                'DeviceCriteria': '4',
                'CalledBy': CalledBy,
                'CalledByCriteria': '4',
                'CalledTo': CalledTo,
                'CalledToCriteria': '4',
                'Duration': Duration,
                'CallDurationCriteria': '3',
                'CallDirection': '2',
                'CallDateTimeCriteria': '0',
                'FlagID': '',
                'GroupID': '',
                'StartDate': '',
                'EndDate': '',
                'ParamNumberOfDays': '',
                'ParamNumberOfMinutes': ''
            }

            # URL for Update Archive Job
            UrlforUpdateArchiveJob = '/Job/Update'
            URL = common.Domain + UrlforUpdateArchiveJob

            # Hit API Through Methods
            response = requests.put(URL, headers=Parameters)

            # API Response in JSON Format
            resp = response.json()
            showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus:
                try:
                    if resp['ResponseCode'] == 200:
                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                except Exception as e:
                    print(f"Error: {e}")
                    status = 'Failed'

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
            else:
                TestCasesStatus = False

        return Title

    # Test Case End
    
    # Start Test Case No 35-16
    def testcase_02_UpdateArchiveJob(self, TestCasesStatus=True): 
        
        TestCaseID = '35-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Put Method to Update Archive Job' , 'Update Archive Job with invalid ID.')
        
        ID='123456'
        # Generate Simple Character String Limit 10 Characters
        Title=common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        FirstName=''
        LastName=''
        Device=''
        CalledBy=''
        CalledTo=''
        Duration=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': ''+ID+'',
                      'Title': ''+Title+'',   
                      'Description': ''+Description+'',
                      'FirstName': ''+FirstName+'',
                      'FirstNameCriteria': '4',
                      'LastName': ''+LastName+'',
                      'LastNameCriteria': '4',
                      'Device': ''+Device+'',
                      'DeviceCriteria': '4',
                      'CalledBy': ''+CalledBy+'',
                      'CalledByCriteria': '4',
                      'CalledTo': ''+CalledTo+'',
                      'CalledToCriteria': '4',
                      'Duration': ''+Duration+'',
                      'CallDurationCriteria': '3',
                      'CallDirection': '2',
                      'CallDateTimeCriteria': '0',
                      'FlagID': '',
                      'GroupID': '',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'ParamNumberOfMinutes': ''
    
                    }
        
        # Url For Add Archive Job    
        UrlforUpdateArchiveJob = '/Job/Update'
        URL = ''+common.Domain+''+UrlforUpdateArchiveJob +''
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

class test_3_GetArchiveJob(TestCase):
    
    # Start Test Case No 35-17
    def testcase_01_GetArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Get Method to Get Archive Job' , 'Get all Archive Job with valid ID and data.')
        
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        ID=''
        SiteCode=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforGetArchiveJob = '/Job/Get/'
        URL = ''+common.Domain+''+UrlforGetArchiveJob +''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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
    
    # Start Test Case No 35-18
    def testcase_02_GetArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Get Method to Get Archive Job' , 'Get a single Archive Job with valid ID.')
        Title=test_1_AddArchiveJob.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)
        
        
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        ID=str(vals[0])
        cursor.commit()
        SiteCode=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforGetArchiveJob = '/Job/Get/'
        URL = ''+common.Domain+''+UrlforGetArchiveJob +''+ID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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
    
    # Start Test Case No 35-19
    def testcase_03_GetArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-19'
        # Calling Common Funtions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Get Method to Get Archive Job' , 'Get a single Archive Job with invalid ID or non existing ID.')
        
        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        
        ID='123456'
        SiteCode=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforGetArchiveJob = '/Job/Get/'
        URL = ''+common.Domain+''+UrlforGetArchiveJob +''+ID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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
    
    # Start Test Case No 35-20
    def testcase_04_GetArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-20'
        # Calling Common Funtions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Get Method to Get Archive Job' , 'Get Archive Job with invalid SiteCode or non existing SiteCode.')
        
        ID=''
        SiteCode='123456'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforGetArchiveJob = '/Job/Get/'
        URL = ''+common.Domain+''+UrlforGetArchiveJob +''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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

class test_4_DeleteArchiveJob(TestCase):
    
    # Start Test Case No 35-21
    def testcase_01_DeleteArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Delete Method to Delete Archive Job' , 'Delete a single Archive Job with valid ID.')
        Title=test_1_AddArchiveJob.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)
        
        # Simple DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        ID=str(vals[0])
        cursor.commit()
        SiteCode=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforDeleteArchiveJob = '/Job/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteArchiveJob +''+ID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
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
    
    # Start Test Case No 35-22
    def testcase_02_DeleteArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Delete Method to Delete Archive Job' , 'Delete a single Archive Job with invalid or non existing ID.')
        
        ID='123456'
        SiteCode=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforDeleteArchiveJob = '/Job/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteArchiveJob +''+ID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
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
    
    # Start Test Case No 35-23
    def testcase_03_DeleteArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Delete Method to Delete Archive Job' , 'Delete a single Archive Job with invalid or non existing SiteCode.')
        Title=test_1_AddArchiveJob.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        ID=str(vals[0])
        cursor.commit()
        SiteCode='123456'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforDeleteArchiveJob = '/Job/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteArchiveJob +''+ID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
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
    
    # Start Test Case No 35-30
    def testcase_04_DeleteArchiveJob(self, TestCasesStatus=True):
        
        TestCaseID = '35-30'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Job' , 'Using Delete Method to Delete Archive Job' , 'Delete a single Archive Job when job is associated with job schedule.')
        
        ArchiveScheduleFunction=ASF.test_1_AddArchiveSchedule()
        JobId, Scheduleid = ArchiveScheduleFunction.testcase_01_AddArchiveSchedule(common.PrereqTestCasesStatusUpdate)
        Scheduleid=Scheduleid
        
        ID=JobId
        SiteCode=''
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': ''+SiteCode+'',
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Add Archive Job    
        UrlforDeleteArchiveJob = '/Job/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteArchiveJob +''+ID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
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