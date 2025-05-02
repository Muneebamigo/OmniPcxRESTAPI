'''
Created on Jul 20, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests, random
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config
SheetName=	'26-Traces Configuration'

class test_1_UpdateTraces_Configuration (TestCase):
    
    # Start Test Case No 26-01
    def testcase_01_UpdateTraces_Configuration (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '26-01' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces Configuration' , 'Using Put Method Update Traces Configuration' , 'Update  when traces type is Restricted')
        
        # Generate random Integer
        MaxFileSize = str(random.randint(1000 , 99999))
        NoOfFiles = str(random.randint(10, 99))
        
        # Header Parameters of Rest API    
        Parameters = {'AuthToken':config.sessionkey,
                          'AuthUser':config.auth_user,
                          'MaxFileSize': ''+MaxFileSize+'',
                          'NoOfFiles': ''+NoOfFiles+'',
                          'BackupLogEnabled': 'False',
                          'BackUpLogPath': '',
                          'TracesGrowthType': '0',
                          'TracesPath': r"C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\Logs"
    
                        }
        
        # URL for Update Traces   OPRTRC14
        UrlforUpdateTraces = '/Traces/Update'
        URL = ''+common.Domain+''+UrlforUpdateTraces+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification    
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
               
    # Start Test Case No 26-03
    def testcase_02_UpdateTraces_Configuration (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '26-03' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces Configuration' , 'Using Put Method Update Traces Configuration' , 'Update  when traces type is Un-Restricted')
    
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TracesGrowthType': '1',
                      'MaxFileSize': '',
                      'NoOfFiles': '',
                      'BackupLogEnabled': 'True',
                      'BackUpLogPath': '\\172.20.0.2\Share Data\Ali Ibrahim\OPR Calls on Networkk',
                      'TracesPath': "C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\Logs"
    
                        }
        
        # URL for Update Traces  
        UrlforUpdateTraces = '/Traces/Update'
        URL = ''+common.Domain+''+UrlforUpdateTraces+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification   
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
    
    # Start Test Case No 26-02
    def testcase_03_UpdateTraces_Configuration (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '26-02' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces Configuration' , 'Using Put Method Update Traces Configuration with MaxFileSize null' , 'Update  when traces type is Restricted')
        
        # Generate random Integers 
        NoOfFiles = str(random.randint(10, 99))
        
        # Header Parameters of Rest API    
        Parameters = {'AuthToken':config.sessionkey,
                          'AuthUser':config.auth_user,
                          'TracesGrowthType': '0',
                          'MaxFileSize': "",
                          'NoOfFiles': ''+NoOfFiles+'',
                          'BackupLogEnabled': 'False',
                          'BackUpLogPath': '',
                          'TracesPath': "C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\Logs"
    
                        }
        
        # URL for Update Traces    
        UrlforUpdateTraces = '/Traces/Update'
        URL = ''+common.Domain+''+UrlforUpdateTraces+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification  
        status = 'Failed'
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
    
    # Start Test Case No 26-05
    def testcase_04_UpdateTraces_Configuration (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '26-05' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces Configuration' , 'Using Put Method Update Traces Configuration with BackUpLogPath null' , 'Update  when traces type is Restricted')
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                          'AuthUser':config.auth_user,
                          'TracesGrowthType': '1',
                          'MaxFileSize': "",
                          'NoOfFiles': "",
                          'BackupLogEnabled': 'True',
                          'BackUpLogPath': '',
                          'TracesPath': "C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\Logs"
    
                        }
        
        # URL for Update Traces   
        UrlforUpdateTraces = '/Traces/Update'
        URL = ''+common.Domain+''+UrlforUpdateTraces+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification    
        status = 'Failed'
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
    
    # Start Test Case No 26-06
    def testcase_05_UpdateTraces_Configuration (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '26-06' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces Configuration' , 'Using Put Method Update Traces Configuration with Null NoOfFiles' , 'Update  when traces type is Restricted/0')
        
        # Generate random Integers 
        NoOfFiles = ''
        
        # Header Parameters of Rest API    
        Parameters = {'AuthToken':config.sessionkey,
                          'AuthUser':config.auth_user,
                          'TracesGrowthType': '0',
                          'MaxFileSize': "100",
                          'NoOfFiles': ''+NoOfFiles+'',
                          'BackupLogEnabled': 'False',
                          'BackUpLogPath': '',
                          'TracesPath': "C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\Logs"
    
                        }
        
        # URL for Update Traces    
        UrlforUpdateTraces = '/Traces/Update'
        URL = ''+common.Domain+''+UrlforUpdateTraces+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification  
        status = 'Failed'
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
                
    # Start Test Case No 26-07
    def testcase_06_UpdateTraces_Configuration (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '26-07' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces Configuration' , 'Using Put Method Update Traces Configuration' , 'Update  when traces type is Un-Restricted and BackUpLogsEnabled is Null')
    
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TracesGrowthType': '1',
                      'MaxFileSize': '',
                      'NoOfFiles': '',
                      'BackupLogEnabled': '',
                      'BackUpLogPath': '\\172.20.0.2\Share Data\Ali Ibrahim\OPR Calls on Network',
                      'TracesPath': "C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\Logs"
    
                        }
        
        # URL for Update Traces  
        UrlforUpdateTraces = '/Traces/Update'
        URL = ''+common.Domain+''+UrlforUpdateTraces+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification   
        status = 'Failed'
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
                
    # Start Test Case No 26-08
    def testcase_07_UpdateTraces_Configuration (self, TestCasesStatus=True): 
        
        # Test Case Start Time
        starttime = time.process_time()   
        TestCaseID = '26-08' 
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces Configuration' , 'Using Put Method Update Traces Configuration' , 'Update  when traces type is Un-Restricted and BackUpLogPath us Null.')
    
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'TracesGrowthType': '1',
                      'MaxFileSize': '',
                      'NoOfFiles': '',
                      'BackupLogEnabled': 'True',
                      'BackUpLogPath': '',
                      'TracesPath': "C:\Program Files (x86)\Alcatel-Lucent Enterprise\OmniPCXRecord Suite\Logs"
    
                        }
        
        # URL for Update Traces  
        UrlforUpdateTraces = '/Traces/Update'
        URL = ''+common.Domain+''+UrlforUpdateTraces+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification   
        status = 'Failed'
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
    
class test_2_GETTraces_Configuration(TestCase):
    
    # URL for Update Traces
    UrlForGetAllTracesData = '/Traces/Get'
    
    # Start Test Case No 26-04
    def testcase_01_GETTraces_Configuration(self, TestCasesStatus=True):
        
        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '26-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Traces' , 'Using Get Method Get TracesConfiguration Data' , 'Get all Data of TracesConfiguration.')
        
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
    
                    }
        # URL for Update Traces
        URL = ''+common.Domain+''+self.UrlForGetAllTracesData+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                    status = 'Failed''Failed'
             
            # Write Output Result in Excel File       
            finally:
                    common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            # Test Case End