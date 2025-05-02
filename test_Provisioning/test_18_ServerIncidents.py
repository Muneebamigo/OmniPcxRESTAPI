'''
Created on Jul 26, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests
from Settings import CommonFunctions as CF
from Key import config
from unittest import TestCase


SheetName=	'18-Server Incidents'

class test_1_Add_Server_Incidents(TestCase):
    
    # Url For Add Server Incident
    URLToAddServerIncidents = '/ServerIncident/Add'
    
    # Start Test Case No 18-01
    def testcase_01_Add_Server_Incidents(self, TestCasesStatus=True):
       
        TestCaseID = '18-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Incidents ' , 'Using Add Server Incident Method' , 'Add Server Incident by Valid DB_ID')
        # Generate Simple Character String Limit 10 Characters
        DbId = common.GenrateSimpleStringLimit10()
        EventId = '5'
        ModuleId='1'
        # Generate Simple Character String Limit 10 Characters
        Message = common.GenrateSimpleStringLimit10()
        DetailsId = 'Recording Turn off' 
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' : ''+DbId+'',
                    'EventID' : ''+EventId+'',
                    'ModuleID' : ''+ModuleId+'',
                    'Message' : ''+Message+'' ,
                    'Detail' : ''+DetailsId+''
                    
                    }
        #Url
        URL = ''+common.Domain+''+self.URLToAddServerIncidents
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
        return DbId
    # Start Test Case No 18-02
    def testcase_02_Add_Server_Incidents_Invalid_Parameter(self, TestCasesStatus=True):
        
        TestCaseID = '18-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Incidents ' , 'Using Add Server Incident Method' , 'Add Server Incident by Invalid/Empty Data EventID')
        # Generate Simple Character String Limit 10 Characters
        DbId = common.GenrateSimpleStringLimit10()
        EventId = ''
        ModuleId='1'
        # Generate Simple Character String Limit 10 Characters
        Message = common.GenrateSimpleStringLimit10()
        DetailsId = 'Recording Turn off' 
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' : ''+DbId+'',
                    'EventID' : ''+EventId+'',
                    'ModuleID' : ''+ModuleId+'',
                    'Message' : ''+Message+'' ,
                    'Detail' : ''+DetailsId+''
                    
                    }
        
        
        #Url
        URL = ''+common.Domain+''+self.URLToAddServerIncidents
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
        return DbId
    
    # Start Test Case No 18-05
    def testcase_05_Add_Server_Incidents(self, TestCasesStatus=True):
       
        TestCaseID = '18-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Incidents ' , 'Using Add Server Incident Method' , 'Add Server Incident by inValid/Empty DB_ID')
        # Generate Simple Character String Limit 10 Characters
        DbId = ''
        EventId = '5'
        ModuleId='1'
        # Generate Simple Character String Limit 10 Characters
        Message = common.GenrateSimpleStringLimit10()
        DetailsId = 'Recording Turn off' 
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' : ''+DbId+'',
                    'EventID' : ''+EventId+'',
                    'ModuleID' : ''+ModuleId+'',
                    'Message' : ''+Message+'' ,
                    'Detail' : ''+DetailsId+''
                    
                    }
        #Url
        URL = ''+common.Domain+''+self.URLToAddServerIncidents
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
    
    # Start Test Case No 18-06
    def testcase_06_Add_Server_Incidents(self, TestCasesStatus=True):
       
        TestCaseID = '18-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Incidents ' , 'Using Add Server Incident Method' , 'Add Server Incident by In Valid/Empty ModuleID')
        # Generate Simple Character String Limit 10 Characters
        DbId = common.GenrateSimpleStringLimit10()
        EventId = '5'
        ModuleId=''
        # Generate Simple Character String Limit 10 Characters
        Message = common.GenrateSimpleStringLimit10()
        DetailsId = 'Recording Turn off' 
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' : ''+DbId+'',
                    'EventID' : ''+EventId+'',
                    'ModuleID' : ''+ModuleId+'',
                    'Message' : ''+Message+'' ,
                    'Detail' : ''+DetailsId+''
                    
                    }
        #Url
        URL = ''+common.Domain+''+self.URLToAddServerIncidents
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
            
    # Start Test Case No 18-07
    def testcase_07_Add_Server_Incidents(self, TestCasesStatus=True):
       
        TestCaseID = '18-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Incidents ' , 'Using Add Server Incident Method' , 'Add Server Incident by In Valid/Empty Message')
        # Generate Simple Character String Limit 10 Characters
        DbId = common.GenrateSimpleStringLimit10()
        EventId = '5'
        ModuleId='1'
        # Generate Simple Character String Limit 10 Characters
        Message = ''
        DetailsId = 'Recording Turn off' 
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' : ''+DbId+'',
                    'EventID' : ''+EventId+'',
                    'ModuleID' : ''+ModuleId+'',
                    'Message' : ''+Message+'' ,
                    'Detail' : ''+DetailsId+''
                    
                    }
        #Url
        URL = ''+common.Domain+''+self.URLToAddServerIncidents
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
            
    # Start Test Case No 18-08
    def testcase_08_Add_Server_Incidents(self, TestCasesStatus=True):
       
        TestCaseID = '18-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Incidents ' , 'Using Add Server Incident Method' , 'Add Server Incident by In Valid/Empty DetailsId')
        # Generate Simple Character String Limit 10 Characters
        DbId = common.GenrateSimpleStringLimit10()
        EventId = '5'
        ModuleId='1'
        # Generate Simple Character String Limit 10 Characters
        Message = common.GenrateSimpleStringLimit10()
        DetailsId = '' 
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' : ''+DbId+'',
                    'EventID' : ''+EventId+'',
                    'ModuleID' : ''+ModuleId+'',
                    'Message' : ''+Message+'' ,
                    'Detail' : ''+DetailsId+''
                    
                    }
        #Url
        URL = ''+common.Domain+''+self.URLToAddServerIncidents
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
    
class test_2_Get_Server_Incidents(TestCase):
    
    # Url For Get Server Incident
    URLToGetServerIncidents = '/ServerIncident/Get'
    
    # Start Test Case No 18-03
    def testcase_03_Get_Server_Incidents(self, TestCasesStatus=True):
        
        TestCaseID = '18-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        # Add Server Incidents Function Calling
        DBRecord_ID = test_1_Add_Server_Incidents()
        brRcId= DBRecord_ID.testcase_01_Add_Server_Incidents(common.PrereqTestCasesStatusUpdate)
        
        common.Header('Server Incidents ' , 'Using Get Server Incident Method' , 'Get Server Incident by Valid ID')
                
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' :brRcId
                    }
        
        #Url
        URL = ''+common.Domain+''+self.URLToGetServerIncidents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
            
         
     
    # Start Test Case No 18-09
    def testcase_09_Get_Server_Incidents(self, TestCasesStatus=True):
        
        TestCaseID = '18-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        
        brRcId= '123456'
        
        common.Header('Server Incidents ' , 'Using Get Server Incident Method' , 'Get Server Incident with invalid or none existing DBRecordID.')
                
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' :brRcId
                    }
        
        #Url
        URL = ''+common.Domain+''+self.URLToGetServerIncidents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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
            
         
    # Start Test Case No 18-04     
    def testcase_04_Get_Server_Incidents(self, TestCasesStatus=True):
        
        TestCaseID = '18-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Server Incidents ' , 'Using Get Server Incident Method' , 'Get Server Incident when DBRecordID more then 250 characters.')
        InValidDBRecord = common.GenrateDesc250()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'DBRecordID' : ''+InValidDBRecord+'',
                    }
        
        
        #Url
        URL = ''+common.Domain+''+self.URLToGetServerIncidents
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        status = 'Failed'
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