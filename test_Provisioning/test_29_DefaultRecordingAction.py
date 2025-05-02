'''
Created on Jul 27, 2018

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
from test_Provisioning import test_01_SystemSettings
from Key import config
SheetName=	'29-Default Recording Actions'

class test_1_DefaultRecordingAction(TestCase):
    
    # Start Test Case No 29-01
    def testcase_01_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        TestCaseID = '29-01' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Record' , 'DefaultRecording Direction= Both')

        # System Settings Function calling
        SSF=test_01_SystemSettings.test_1_UpdateSystemSettings()
        SSF.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '0',
                      'DefaultRecordingDirection': '0',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
    
    # Start Test Case No 29-02            
    def testcase_02_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        TestCaseID = '29-02' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Record' , 'DefaultRecording Direction= Inbound')
        
        # System Settings Function calling
        SSF=test_01_SystemSettings.test_1_UpdateSystemSettings()
        SSF.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '0',
                      'DefaultRecordingDirection': '1',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions   
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
                
                
    # Start Test Case No 29-03            
    def testcase_03_DefaultRecordingAction (self, TestCasesStatus=True): 
         
        TestCaseID = '29-03' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Record' , 'DefaultRecording Direction= OutBound')
        
        # System Settings Function calling
        SSF=test_01_SystemSettings.test_1_UpdateSystemSettings()
        SSF.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)     
        
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '0',
                      'DefaultRecordingDirection': '2',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions    
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
                
    # Start Test Case No 29-04      
    def testcase_04_DefaultRecordingAction (self, TestCasesStatus=True): 
         
        TestCaseID = '29-04' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Ignore' , 'DefaultRecording Direction= Both')

        # System Settings Function calling
        SSF=test_01_SystemSettings.test_1_UpdateSystemSettings()
        SSF.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '1',
                      'DefaultRecordingDirection': '0',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions    
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
           
    # Start Test Case No 29-05           
    def testcase_05_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        TestCaseID = '29-05' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Ignore' , 'DefaultRecording Direction= InBound')
        
        # System Settings Function calling
        SSF=test_01_SystemSettings.test_1_UpdateSystemSettings()
        SSF.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API     
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '1',
                      'DefaultRecordingDirection': '1',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions    
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
            
        status = 'Failed'
        
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
                
           
    # Start Test Case No 29-06            
    def testcase_06_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '29-06' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Ignore' , 'DefaultRecording Direction= OutBound')

        
        # Header Parameters of Rest API 
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '1',
                      'DefaultRecordingDirection': '2',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions    
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
                
    # Start Test Case No 29-07            
    def testcase_07_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '29-07' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= null' , 'DefaultRecording Direction= Both')

        # Header Parameters of Rest API     
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '',
                      'DefaultRecordingDirection': '0',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions    
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
           
    # Start Test Case No 29-08           
    def testcase_08_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '29-08' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Record' , 'DefaultRecording Direction= Null')

        # Header Parameters of Rest API    
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '0',
                      'DefaultRecordingDirection': '',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions   
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
           
    # Start Test Case No 29-09            
    def testcase_09_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '29-09' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Ignore' , 'DefaultRecording Direction= Null')

        # Header Parameters of Rest API     
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '1',
                      'DefaultRecordingDirection': '',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions   
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
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
                
    # Start Test Case No 29-10
    def testcase_10_DefaultRecordingAction (self, TestCasesStatus=True):

        TestCaseID = '29-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Record and server role as branch' , 'DefaultRecording Direction= Both and server role as branch')

        # System Settings Function calling
        SSF=test_01_SystemSettings.test_1_UpdateSystemSettings()
        SSF.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '0',
                      'DefaultRecordingDirection': '0',
                      'SiteCode': '',

                        }

        # Url for Update Default Recording Actions
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])

        status = 'Failed'
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
    
    # Start Test Case No 29-11
    def testcase_11_DefaultRecordingAction (self, TestCasesStatus=True): 
        
        TestCaseID = '29-11' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('DefaultRecordingAction , Put Method Update Default Recording Action' , 'Update when DefaultRecordingAction= Record and server role as branch' , 'DefaultRecording Direction= Both and server role as secondary configured.')

        # System Settings Function calling
        SSF=test_01_SystemSettings.test_1_UpdateSystemSettings()
        SSF.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'DefaultRecordingAction': '0',
                      'DefaultRecordingDirection': '0',
                      'SiteCode': '',

                        }
        
        # Url for Update Default Recording Actions
        UrlforUpdateDefaultRecordingActions= '/SiteSettings/UpdateDefaultRecordingActions'
        URL = ''+common.Domain+''+UrlforUpdateDefaultRecordingActions+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        time.sleep(1)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
            
        status = 'Failed'
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