'''
Created on Jul 23, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
import test_Provisioning.test_19_Branch as branchFunctions
from test_Provisioning import test_13_SMTPSettings as smtpfunctions
from Key import config
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
SheetName=	'20-Send Branch Email'

class test_1_GetSendBranchEmail(TestCase):
    # Url for Get Branch Email
    UrlForGetBranchEmail = '/Branch/EmailBranchGUID/'
    # Start Test Case No 20-01    
    def testcase_1_GetSendBranchEmail(self, TestCasesStatus=True):
        
        TestCaseID = '20-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Send Branch Email' , 'Send Branch Email' ,'Get the GUID in email associated to the branch with valid ID')
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        #Add Branch Function Calling
        BRANCH_FUNCTION=branchFunctions.test_1_AddBranch()
        name = BRANCH_FUNCTION.testcase_01_AddBranch(common.PrereqTestCasesStatusUpdate)
        # Update SMTP Settings Function Calling
        SMTPFunctions=smtpfunctions.UpdateSMTPSettings()
        SMTPFunctions.testcase_01_UpdateSMTPSettings(common.PrereqTestCasesStatusUpdate)
        # SQL Queries for Data Verification
        SQLCommand = ("Select BranchID From Branch Where BranchName ='"+name+"';")
        cursor.execute(SQLCommand)
        BranchID=cursor.fetchone()
        BranchID=str(BranchID[0])
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'ID': ''+BranchID+'',
        
                    }
        #Url
        URL = ''+common.Domain+''+self.UrlForGetBranchEmail+''+BranchID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
            
    # Start Test Case No 20-02        
    def testcase_2_GetSendBranchEmail(self, TestCasesStatus=True):
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '20-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Send Branch Email' , 'Send Branch Email' ,'Get the GUID in email associated to the branch with Invalid ID')
        
        BranchID='123456'
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'ID': ''+BranchID+'',
        
                    }
        #Url
        URL = ''+common.Domain+''+self.UrlForGetBranchEmail+''+BranchID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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