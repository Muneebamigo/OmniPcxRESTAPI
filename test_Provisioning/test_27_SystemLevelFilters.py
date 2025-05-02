'''
Created on Jul 27, 2018

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
from test_Provisioning import test_01_SystemSettings as SS
from Key import config

SheetName=	'27-System Level Filter'
class Test_1_AddSLF(TestCase):
    
    # Start Test Case No 27-01
    def testcase_01_AddSLF(self, TestCaseStatus = True):
        
        TestCaseID = '27-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when Recording Call Direction Both and Day/Time not required')
        
        # System Settings Function calling
        SystemSettings=SS.test_1_UpdateSystemSettings()
        SystemSettings.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        SLFName=common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
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
    
        return SLFName
    # Test Case End

    # Start Test Case No 27-02
    def testcase_02_AddSLF(self, TestCaseStatus = True):
        
        TestCaseID = '27-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when Duplicate SLF Name')
        
        # Add SLF Function calling
        SLFName = Test_1_AddSLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Description=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # API Response in JSon Format
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    # Test Case End
    
    # Start Test Case No 27-03
    def testcase_03_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with invalid data when system with null name/recordingCallDirection')
    
        SLFName = ''
        # Generate Simple Character String Limit 10 Characters
        Description=common.GenrateSimpleStringLimit10()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    # Test Case End
    
    # Start Test Case No 27-04
    def testcase_04_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with invalid data when schedule 1 and start/end time null')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '1',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    # Test Case End
    
    # Start Test Case No 27-05
    def testcase_05_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with invalid data when schedule 2 and day with null')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '2',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    # Test Case End
    
    # Start Test Case No 27-06
    def testcase_06_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with invalid data when schedule 3 and start/end date null')
    
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '3',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    # Test Case End
    
    # Start Test Case No 27-07
    def testcase_07_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when schedule 1 and start/end time and RecordingCallDirection is both')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        StartTime='21:59:00'
        EndTime='23:59:00'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '1',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': ''+StartTime+'',
                      'EndTime': ''+EndTime+'',
                      'TeamID': '',
                     }
        
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
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
    # Test Case End
    
    # Start Test Case No 27-08
    def testcase_08_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when schedule 2 and start/end time and RecordingCallDirection is both')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        StartTime='21:59:00'
        EndTime='23:59:00'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '2',
                      'Day': '1',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': ''+StartTime+'',
                      'EndTime': ''+EndTime+'',
                      'TeamID': '',
                     }
        
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
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
    # Test Case End
    
    # Start Test Case No 27-09
    def testcase_09_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when schedule 3 and start/end time and RecordingCallDirection is both')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        StartTime='21:59:00'
        EndTime='23:59:00'
        StartDate=time.strftime("%d/%m/%Y")
        EndDate='11/11/2025'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '3',
                      'Day': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'StartTime': ''+StartTime+'',
                      'EndTime': ''+EndTime+'',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
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
    # Test Case End
    
    # Start Test Case No 27-10
    def testcase_10_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when schedule 0  RecordingCallDirection is inbound')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        StartTime=''
        EndTime=''
        StartDate=''
        EndDate=''
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '1',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'StartTime': ''+StartTime+'',
                      'EndTime': ''+EndTime+'',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
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
    # Test Case End
    
    # Start Test Case No 27-11
    def testcase_11_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when schedule 0  RecordingCallDirection is outbound')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        StartTime=''
        EndTime=''
        StartDate=''
        EndDate=''
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '2',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'StartTime': ''+StartTime+'',
                      'EndTime': ''+EndTime+'',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
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
    # Test Case End
    
    # Start Test Case No 27-19
    def testcase_19_AddSLF(self, TestCaseStatus = True):
        
        TestCaseID = '27-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with invalid site code.')
        
        # System Settings Function calling
        SystemSettings=SS.test_1_UpdateSystemSettings()
        SystemSettings.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        SLFName=common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'1234567',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
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
            TestCaseStatus = False
            
            
    # Start Test Case No 27-20
    def testcase_20_AddSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Post Method', 'Add Simple SLF with valid data when schedule 3 but startdate is less then Enddate')
        
        # Generate Simple Character String Limit 10 Characters
        SLFName = common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        StartTime='21:59:00'
        EndTime='23:59:00'
        StartDate='12/12/2025'
        EndDate=time.strftime("%d/%m/%Y")
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '3',
                      'Day': '',
                      'StartDate': ''+StartDate+'',
                      'EndDate': ''+EndDate+'',
                      'StartTime': ''+StartTime+'',
                      'EndTime': ''+EndTime+'',
                      'TeamID': '',
                     }
        
        # Url For Add SLF
        UrlForAddSLF='/SystemLevelFilter/Add/'
        URL = ''+common.Domain+''+UrlForAddSLF+''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    # Test Case End
    
    
class Test_2_UpdateSLF(TestCase):
    
    # Start Test Case No 27-12
    def testcase_12_UpdateSLF(self, TestCaseStatus = True):
        
        TestCaseID = '27-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Put Method', 'Update Simple SLF with valid data Input ID')
        
        # Add SLF Function calling
        name = Test_1_AddSLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Generate Simple Character String Limit 10 Characters
        SLFName=common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'ID': ''+SLFID+'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Update SLF
        UrlForUpdateSLF='/SystemLevelFilter/Update/'
        URL = ''+common.Domain+''+UrlForUpdateSLF+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # SQL Queries for Data Verification
        SQLCommand = ("Select Name From RecordingFilters Where Name = '"+SLFName+"' LIMIT 1")
        cursor.execute(SQLCommand)
        Name = cursor.fetchone()
        
        # Response Code Verification
        status='Failed'
        if TestCaseStatus == True:
            try:
                    if resp['ResponseCode'] == 200:
                        if Name[0] == SLFName:
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
    # Test Case End
    
    # Start Test Case No 27-13
    def testcase_13_UpdateSLF(self, TestCaseStatus = True):
    
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Put Method', 'Update Simple SLF with Invalid data Input ID')
        
        SLFID = '123456'
        
        # Generate Simple Character String Limit 10 Characters
        SLFName=common.GenrateSimpleStringLimit10()
        Description=common.GenrateSimpleStringLimit10()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'ID': ''+SLFID+'',
                      'Name': ''+SLFName+'',
                      'Description': ''+Description+'',
                      'RecordingCallDirection': '0',
                      'Schedule': '0',
                      'Day': '',
                      'StartDate': '',
                      'EndDate': '',
                      'StartTime': '',
                      'EndTime': '',
                      'TeamID': '',
                     }
        
        # Url For Update SLF
        UrlForUpdateSLF='/SystemLevelFilter/Update/'
        URL = ''+common.Domain+''+UrlForUpdateSLF+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
    
        return SLFName
    # Test Case End

class Test_3_GetSLF(TestCase):
    
    # Start Test Case No 27-14
    def testcase_14_GetSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling GET Method', 'Get all list of SLF with valid data')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'Id': '',
                     }
        
        # Url For Get SLF
        UrlForGetSLF='/SystemLevelFilter/Get/'
        URL = ''+common.Domain+''+UrlForGetSLF+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        status='Failed'
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
    # Test Case End
    
    # Start Test Case No 27-15
    def testcase_15_GetSLF(self, TestCaseStatus = True):
        
        TestCaseID = '27-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Get Method', 'Get a single SLF with valid data Input ID')
        
        # Add SLF Function calling
        name = Test_1_AddSLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Id': ''+SLFID+'',
                     }
        
        # Url For Get SLF
        UrlForGetSLF='/SystemLevelFilter/Get/'
        URL = ''+common.Domain+''+UrlForGetSLF+''+SLFID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
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
    # Test Case End
    
    # Start Test Case No 27-16
    def testcase_16_UpdateSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Get Method', 'Get a single SLF with valid data inInput ID')
        
        SLFID = '123456'
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Id': ''+SLFID+'',
                     }
        
        # Url For Get SLF
        UrlForGetSLF='/SystemLevelFilter/Get/'
        URL = ''+common.Domain+''+UrlForGetSLF+''+SLFID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False
           
    # Test Case End 
    
class Test_4_DeleteSLF(TestCase):
    
    # Start Test Case No 27-17
    def testcase_17_DeleteSLF(self, TestCaseStatus = True):
        
        TestCaseID = '27-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Delete Method', 'Delete a SLF with valid ID')
        
        # Add SLF Function calling
        name = Test_1_AddSLF.testcase_01_AddSLF(common.PrereqTestCasesStatusUpdate)
        
        # Tenant DB Connectivity Function calling
        cursor=common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select RecordingFilterId From RecordingFilters Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        SLFID = str(vals[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Id': ''+SLFID+'',
                     }
        
        # Url For Delete SLF
        UrlForDeleteSLF='/SystemLevelFilter/Delete/'
        URL = ''+common.Domain+''+UrlForDeleteSLF+''+SLFID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
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
    # Test Case End
    
    # Start Test Case No 27-18
    def testcase_18_DeleteSLF(self, TestCaseStatus = True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '27-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('SLF', 'Calling Delete Method', 'Delete a SLF with Invalid ID')
       
        SLFID = '123456'
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Id': ''+SLFID+'',
                     }
        # Url For Delete SLF
        UrlForDeleteSLF='/SystemLevelFilter/Delete/'
        URL = ''+common.Domain+''+UrlForDeleteSLF+''+SLFID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCaseStatus == True:
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
            TestCaseStatus = False