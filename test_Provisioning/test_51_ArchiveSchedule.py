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
from test_Provisioning import test_35_ArchiveJob as ArchiveJobFuntions
from test_Provisioning import test_01_SystemSettings as SSF
from Key import config

SheetName=	'51-Archive Schedule'

class test_1_AddArchiveSchedule(TestCase):

    # Start Test Case No 51-01
    def testcase_01_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with all valid Data and Type is 0/Daily.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        JobId=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=JobId
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType' : '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # SQL Queries for Data Verification
        SQLCommand2 = ("Select Scheduleid From JobSchedule Where Jobid = '"+JobId+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        Scheduleid=str(vals[0])
        cursor.commit()

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

        return JobId, Scheduleid
    # Test Case End


    # Start Test Case No 51-02
    def testcase_02_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with invalid date format and Type is 0/Daily.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time='123456'
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-03
    def testcase_03_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with all valid Data and Type is 1/After Every and IntervalCriteria is 0.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = '1'
        IntervalCriteria='0'
        Type='1'
        Time=''
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType' : '0',


                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-04
    def testcase_04_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with all valid Data and Type is 1/After Every and IntervalCriteria is 1.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = '1'
        IntervalCriteria='1'
        Type='1'
        Time=''
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-05
    def testcase_05_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with all valid Data and Type is 2/Weekly.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='2'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay='0'
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-06
    def testcase_06_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with all valid Data and Type is 3/Monthly.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='3'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay='1'
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-07
    def testcase_07_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with all valid Data and Type is 4/Once.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='4'
        Time=time.strftime("%H:%M:%S")
        StartDate= time.strftime("%d/%m/%Y")
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-08
    def testcase_08_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with invalid Data and Type is 4/Once and date format is wrong.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='4'
        Time=time.strftime("%H:%M:%S")
        StartDate= '123456'
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-09
    def testcase_09_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with Null Schedule time Data and Type is 0/Daily.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=''
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-10
    def testcase_10_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with Null JobId Data and Type is 0/Daily.')

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-11
    def testcase_11_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with invalid or non existing JobId Data and Type is 0/Daily.')

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job='123456'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-12
    def testcase_12_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with Null interval and Type is 1/After Every and IntervalCriteria is 0.')

        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='0'
        Type='1'
        Time=''
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-13
    def testcase_13_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with Schedule Day is Null and Type is 2/Weekly.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='2'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-14
    def testcase_14_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with Null Schedule Day and Type is 3/Monthly.')

        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='3'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-15
    def testcase_15_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with NULL Schedule Date and Type is 4/Once.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='4'
        Time=time.strftime("%H:%M:%S")
        StartDate= ''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


    # Start Test Case No 51-16
    def testcase_16_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule when server role configured as secondary.')

        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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

    # Test Case End


    # Start Test Case No 51-17
    def testcase_17_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule when server role configured as branch.')

        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        SystemSettingsFunctions=SSF.test_1_UpdateSystemSettings()
        SystemSettingsFunctions.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        title=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=title
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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

    # Test Case End


    # Start Test Case No 51-26
    def testcase_26_AddArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Post Method to Add Archive Schedule' , 'Add Archive Schedule with all valid Data and Site code is invalid or non existing.')
        ArchiveJobFuntion=ArchiveJobFuntions.test_1_AddArchiveJob()
        Title = ArchiveJobFuntion.testcase_01_AddArchiveJob(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select JobId From Jobs Where Title = '"+Title+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        JobId=str(vals[0])
        cursor.commit()

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=JobId
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '123456',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Add Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Add'
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


class test_2_UpdateArchiveSchedule(TestCase):

    # Start Test Case No 51-18
    def testcase_18_UpdateArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Put Method to Update Archive Schedule' , 'Update Archive Schedule with all valid Data.')

        JobId, Scheduleid = test_1_AddArchiveSchedule.testcase_01_AddArchiveSchedule(common.PrereqTestCasesStatusUpdate)

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=JobId
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': ''+Scheduleid+'',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Update Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Update'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
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


    # Start Test Case No 51-19
    def testcase_19_UpdateArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Put Method to Update Archive Schedule' , 'Update Archive Schedule with invalid Scheduleid.')

        JobId, Scheduleid = test_1_AddArchiveSchedule.testcase_01_AddArchiveSchedule(common.PrereqTestCasesStatusUpdate)
        Scheduleid=Scheduleid

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=JobId
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': '123456',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Update Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Update'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
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


    # Start Test Case No 51-20
    def testcase_20_UpdateArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Put Method to Update Archive Schedule' , 'Update Archive Schedule with NULL Scheduleid.')

        JobId, Scheduleid = test_1_AddArchiveSchedule.testcase_01_AddArchiveSchedule(common.PrereqTestCasesStatusUpdate)
        Scheduleid=Scheduleid

        Interval = ''
        IntervalCriteria='2'
        Type='0'
        Time=time.strftime("%H:%M:%S")
        StartDate=''
        WeekDay=''
        MonthDay=''
        Job=JobId
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': '',
                      'Interval': ''+Interval+'',
                      'IntervalCriteria': ''+IntervalCriteria+'',
                      'Type': ''+Type+'',
                      'Time': ''+Time+'',
                      'StartDate': ''+StartDate+'',
                      'WeekDay': ''+WeekDay+'',
                      'MonthDay': ''+MonthDay+'',
                      'Job': ''+Job+'',
                      'SchedulerType': '0'

                    }

        # Url For Update Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Update'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
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


class test_3_GetArchiveSchedule(TestCase):

    # Start Test Case No 51-21
    def testcase_21_GetArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Get Method to Get Archive Schedule' , 'Get all configured Archive Schedule with all valid Data.')

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': '',

                    }

        # Url For Get Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Get'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
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


    # Start Test Case No 51-22
    def testcase_22_UpdateArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Get Method to Get Archive Schedule' , 'Get a single Archive Schedule data with valid id.')

        JobId, Scheduleid = test_1_AddArchiveSchedule.testcase_01_AddArchiveSchedule(common.PrereqTestCasesStatusUpdate)
        JobId=JobId

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': ''+Scheduleid+'',

                    }

        # Url For Get Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Get/'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''
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


    # Start Test Case No 51-23
    def testcase_23_UpdateArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Get Method to Get Archive Schedule' , 'Get a single Archive Schedule data with invalid or non existing id.')

        ID = '123456'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': ''+ID+'',

                    }

        # Url For Get Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Get/'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''+ID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus==True:
            try:
                # now the release 2.5.0.15 this case is result respoonse code is 400 before the show 200 in 2.5.0.4
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


class test_4_DeleteArchiveSchedule(TestCase):

    # Start Test Case No 51-24
    def testcase_24_DeleteArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'To Delete Archive Schedule' , 'Delete configured Archive Schedule with valid Id.')

        JobId, Scheduleid = test_1_AddArchiveSchedule.testcase_01_AddArchiveSchedule(common.PrereqTestCasesStatusUpdate)
        JobId=JobId

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': ''+Scheduleid+'',

                    }

        # Url For Delete Archive Schedule
        UrlforAddArchiveJob = '/JobSchedule/Delete/'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''+Scheduleid+''
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


    # Start Test Case No 51-25
    def testcase_25_UpdateArchiveSchedule(self, TestCasesStatus=True):

        TestCaseID = '51-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Archive Schedule' , 'Using Delete Method to Delete Archive Schedule' , 'Delete Archive Schedule data with invalid id.')

        Scheduleid = '123456'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode': '',
                      'ID': ''+Scheduleid+'',
                      
                    }
        
        # Url For Delete Archive Schedule    
        UrlforAddArchiveJob = '/JobSchedule/Delete/'
        URL = ''+common.Domain+''+UrlforAddArchiveJob +''+Scheduleid+''
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