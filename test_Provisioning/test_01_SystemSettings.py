''' 
Created on Jun 8, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed

----------------pre requisite--------------------------------------
User which is used for system settings is admin.
all inputs which is required is define in InputData.py
all session which get from the token is define in GetAuthToken.py
which will be get through CommonFunction.py file

------------------OutPut----------------------------
This module will be update the system settings ,
All the updated setting will be shown on System module of the server Administration.
second purpose of this module is to get the system setting
which will be available on system page.

Note:Server mode only available when main from recorder and primary from Server role
other wise server mode is not available
'''

import time, requests


from Settings import CommonFunctions as CF
from unittest import TestCase
from InputDataFiles import InputData
from Key import config


SheetName= '1-System Settings'

class test_1_UpdateSystemSettings(TestCase):



    # Calling Input Data File
    ssinputdata = InputData.InputData()
    # Url For Update System Settings
    UrlForUpdateSystemSettings = '/SystemSettings/UpdateSystemSettings/'

    # Start Test Case No 01-01
    def testcase_01_UpdateSystemSettings(self, TestCasesStatus=True):

        TestCaseID = '01-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings for server mode as None/0 and server role as primary, Recorder Type is Main.')
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()



        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '0',
                      'DBName': ''+self.ssinputdata.MainSecondaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainSecondaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainSecondaryDBPassword+'',
                      'ServerMode': '0',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',

                    }

        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])

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

    # Start Test Case No 01-02
    def testcase_02_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings for server mode as Master server role as Primary, Recorder is Main.')
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        ServerRole = 'Primary'
        ServerMode = 'Master'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '0',
                      'DBName': ''+self.ssinputdata.MainSecondaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainSecondaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainSecondaryDBPassword+'',
                      'ServerMode': '1',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select PrimaryServerIP From DefaultSettings Where PrimaryServerIP = '"+self.ssinputdata.MainPrimaryServerIP+"';")
        cursor.execute(SQLCommand1)
        primaryserverip=cursor.fetchone()
        SQLCommand2 = ("Select ServerRole From DefaultSettings where ServerRole = '"+ServerRole+"';")
        cursor.execute(SQLCommand2)
        serverrole=cursor.fetchone()
        SQLCommand3 = ("Select ServerMode From DefaultSettings where ServerMode = '"+ServerMode+"';")
        cursor.execute(SQLCommand3)
        servermode=cursor.fetchone()
        cursor.commit()
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if primaryserverip[0] == self.ssinputdata.MainPrimaryServerIP:
                        print('b')
                        if serverrole[0] == ServerRole:
                            print('c')
                            if servermode[0] == ServerMode:
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
            
    # Start Test Case No 01-03
    def testcase_03_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings for server mode as Satellite and server role as primary, Recorder is Main.')
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        ServerRole = 'Primary'
        ServerMode = 'Satellite'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '0',
                      'DBName': ''+self.ssinputdata.MainSecondaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainSecondaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainSecondaryDBPassword+'',
                      'ServerMode': '2',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select PrimaryServerIP From DefaultSettings Where PrimaryServerIP = '"+self.ssinputdata.MainPrimaryServerIP+"';")
        cursor.execute(SQLCommand1)
        primaryserverip=cursor.fetchone()
        SQLCommand2 = ("Select ServerRole From DefaultSettings where ServerRole = '"+ServerRole+"';")
        cursor.execute(SQLCommand2)
        serverrole=cursor.fetchone()
        SQLCommand3 = ("Select ServerMode From DefaultSettings where ServerMode = '"+ServerMode+"';")
        cursor.execute(SQLCommand3)
        servermode=cursor.fetchone()
        cursor.commit()
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if primaryserverip[0] == self.ssinputdata.MainPrimaryServerIP:
                        print('b')
                        if serverrole[0] == ServerRole:
                            print('c')
                            if servermode[0] == ServerMode:
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
    
    # Start Test Case No 01-04  
    def testcase_04_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings for server mode value Null/empty and server role as primary.')
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '0',
                      'DBName': ''+self.ssinputdata.MainSecondaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainSecondaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainSecondaryDBPassword+'',
                      'ServerMode': '',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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


    # Start Test Case No 01-05
    def testcase_05_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings Server Role as secondary  and Server mode as None/0, Recorder is Main.')
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        ServerRole = 'Secondary'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '1',
                      'DBName': ''+self.ssinputdata.MainPrimaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainPrimaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainPrimaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainPrimaryDBPassword+'',
                      'ServerMode': '0',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select SecondaryServerIP From DefaultSettings Where SecondaryServerIP = '"+self.ssinputdata.MainSecondaryServerIP+"';")
        cursor.execute(SQLCommand1)
        secondaryserverip=cursor.fetchone()
        SQLCommand2 = ("Select ServerRole From DefaultSettings where ServerRole = '"+ServerRole+"';")
        cursor.execute(SQLCommand2)
        serverrole=cursor.fetchone()
        cursor.commit()
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if secondaryserverip[0] == self.ssinputdata.MainSecondaryServerIP:
                        print('b')
                        if serverrole[0] == ServerRole:
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
            
    # Start Test Case No 01-06
    def testcase_06_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings Server Role as secondary  and Server  mode as Master/1, Recorder is Main.')
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        ServerRole = 'Secondary'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '1',
                      'DBName': ''+self.ssinputdata.MainPrimaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainPrimaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainPrimaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainPrimaryDBPassword+'',
                      'ServerMode': '1',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select SecondaryServerIP From DefaultSettings Where SecondaryServerIP = '"+self.ssinputdata.MainSecondaryServerIP+"';")
        cursor.execute(SQLCommand1)
        secondaryserverip=cursor.fetchone()
        SQLCommand2 = ("Select ServerRole From DefaultSettings where ServerRole = '"+ServerRole+"';")
        cursor.execute(SQLCommand2)
        serverrole=cursor.fetchone()
        cursor.commit()
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 200:
                    print('a')
                    if secondaryserverip[0] == self.ssinputdata.MainSecondaryServerIP:
                        print('b')
                        if serverrole[0] == ServerRole:
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

    # Start Test Case No 01-07
    def testcase_07_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the system settings server role as secondary and server mode value is equal to 7.')
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        ServerRole = 'Secondary'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '1',
                      'DBName': ''+self.ssinputdata.MainPrimaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainPrimaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainPrimaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainPrimaryDBPassword+'',
                      'ServerMode': '7',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
        # SQL Queries for Data Verification
        SQLCommand1 = ("Select SecondaryServerIP From DefaultSettings Where SecondaryServerIP = '"+self.ssinputdata.MainSecondaryServerIP+"';")
        cursor.execute(SQLCommand1)
        secondaryserverip=cursor.fetchone()
        SQLCommand2 = ("Select ServerRole From DefaultSettings where ServerRole = '"+ServerRole+"';")
        cursor.execute(SQLCommand2)
        serverrole=cursor.fetchone()
        cursor.commit()
        
        # Response Code Verification
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print('a')
                    if secondaryserverip[0] == self.ssinputdata.MainSecondaryServerIP:
                        print('b')
                        if serverrole[0] == ServerRole:
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

    # Start Test Case No 01-08
    def testcase_08_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the  system settings server role as secondary and server mode value is equal to null/empty.')
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '1',
                      'DBName': ''+self.ssinputdata.MainPrimaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainPrimaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainPrimaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainPrimaryDBPassword+'',
                      'ServerMode': '',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
    
    # Start Test Case No 01-09
    def testcase_09_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the system settings when Recorder is Branch Server Role as primary and server mode as None/0.')
       
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerRole': '0',
                      'ServerName': ''+simplestring+'',
                      'ServerMode': '0',
                      'BranchServerIP': ''+self.ssinputdata.BranchServerIP+'',
                      'OPRID': ''+self.ssinputdata.OPRID+'',
                      'DBServerName': ''+self.ssinputdata.BranchSecondaryDBServerName+'',
                      'DBName': ''+self.ssinputdata.BranchSecondaryDBName+'',
                      'DBUsername': ''+self.ssinputdata.BranchSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.BranchSecondaryDBPassword+'',
                      'Recorder': '1',
                      'BranchRemoteIP': ''+self.ssinputdata.BranchRemoteIP+'',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
          
    # Start Test Case No 01-10
    def testcase_10_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the system Settings when recorder is branch, server role as primary, with server mode Master/1.')
        
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerRole': '0',
                      'ServerName': ''+simplestring+'',
                      'ServerMode': '1',
                      'BranchServerIP': ''+self.ssinputdata.BranchServerIP+'',
                      'OPRID': ''+self.ssinputdata.OPRID+'',
                      'DBServerName': ''+self.ssinputdata.BranchSecondaryDBServerName+'',
                      'DBName': ''+self.ssinputdata.BranchSecondaryDBName+'',
                      'DBUsername': ''+self.ssinputdata.BranchSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.BranchSecondaryDBPassword+'',
                      'Recorder': '1',
                      'BranchRemoteIP': ''+self.ssinputdata.BranchRemoteIP+'',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
    
    # Start Test Case No 01-11  
    def testcase_11_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the system settings when recorder is branch, server role as primary with server mode value is 7.')
       
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerRole': '2',
                      'ServerName': ''+simplestring+'',
                      'ServerMode': '7',
                      'BranchServerIP': ''+self.ssinputdata.BranchServerIP+'',
                      'OPRID': ''+self.ssinputdata.OPRID+'',
                      'DBServerName': '',
                      'DBName': '',
                      'DBUsername': '',
                      'DBPassword': '',
                      'Recorder': '1',
                      'BranchRemoteIP': ''+self.ssinputdata.BranchRemoteIP+'',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            
    # Start Test Case No 01-12             
    def testcase_12_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the system settings when recorder is branch, server role as primary with server mode value is Null/empty.')
       
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerRole': '2',
                      'ServerName': ''+simplestring+'',
                      'ServerMode': '',
                      'BranchServerIP': ''+self.ssinputdata.BranchServerIP+'',
                      'OPRID': ''+self.ssinputdata.OPRID+'',
                      'DBServerName': '',
                      'DBName': '',
                      'DBUsername': '',
                      'DBPassword': '',
                      'Recorder': '1',
                      'BranchRemoteIP': ''+self.ssinputdata.BranchRemoteIP+'',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        status = str('Failed  ResponseCode-'+showcode+'')
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
            
    # Start Test Case No 01-14
    def testcase_14_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the system  settings when recorder is branch, Server Role as secondary and server mode as None/0.')
        
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerRole': '1',
                      'ServerName': ''+simplestring+'',
                      'ServerMode': '0',
                      'BranchServerIP': ''+self.ssinputdata.BranchServerIP+'',
                      'OPRID': ''+self.ssinputdata.OPRID+'',
                      'DBServerName': ''+self.ssinputdata.BranchPrimaryDBServerName+'',
                      'DBName': ''+self.ssinputdata.BranchPrimaryDBName+'',
                      'DBUsername': ''+self.ssinputdata.BranchPrimaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.BranchPrimaryDBPassword+'',
                      'Recorder': '1',
                      'BranchRemoteIP': ''+self.ssinputdata.BranchRemoteIP+'',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            
    # Start Test Case No 01-15
    def testcase_15_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the  system  settings when recorder is branch, Server Role as secondary and server mode as master/1.')
        
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerRole': '1',
                      'ServerName': ''+simplestring+'',
                      'ServerMode': '1',
                      'BranchServerIP': ''+self.ssinputdata.BranchServerIP+'',
                      'OPRID': ''+self.ssinputdata.OPRID+'',
                      'DBServerName': ''+self.ssinputdata.BranchPrimaryDBServerName+'',
                      'DBName': ''+self.ssinputdata.BranchPrimaryDBName+'',
                      'DBUsername': ''+self.ssinputdata.BranchPrimaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.BranchPrimaryDBPassword+'',
                      'Recorder': '1',
                      'BranchRemoteIP': ''+self.ssinputdata.BranchRemoteIP+'',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
    
    # Start Test Case No 01-16
    def testcase_16_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the system  settings when recorder is branch, Server Role as secondary and server mode value is 7.')
        
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerRole': '1',
                      'ServerName': ''+simplestring+'',
                      'ServerMode': '7',
                      'BranchServerIP': ''+self.ssinputdata.BranchServerIP+'',
                      'OPRID': ''+self.ssinputdata.OPRID+'',
                      'DBServerName': ''+self.ssinputdata.BranchPrimaryDBServerName+'',
                      'DBName': ''+self.ssinputdata.BranchPrimaryDBName+'',
                      'DBUsername': ''+self.ssinputdata.BranchPrimaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.BranchPrimaryDBPassword+'',
                      'Recorder': '1',
                      'BranchRemoteIP': ''+self.ssinputdata.BranchRemoteIP+'',
    
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            
            
    # Start Test Case No 01-17
    def testcase_17_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings for server mode as None/0 and server role as primary, and duplicate primary and secondary IP.')
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '0',
                      'DBName': ''+self.ssinputdata.MainSecondaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainSecondaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainSecondaryDBPassword+'',
                      'ServerMode': '0',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url 
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            
            
    # Start Test Case No 01-18
    def testcase_18_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings for server mode as None/0 and server role as primary, and server name parameters contains double quotes.')
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'', #MainPrimaryServerIP
                      'ServerName': ''+""+'', #simplestring
                      'ServerRole': '0',
                      'DBName': ''+self.ssinputdata.MainSecondaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainSecondaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainSecondaryDBPassword+'',
                      'ServerMode': '0',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url 
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
            
    def testcase_19_UpdateSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Put Method System Settings' , 'Configure the System Settings for server mode as None/0 and server role as primary, Site Session key.')
        # Generate Simple Character String Limit 10 Characters
        simplestring=common.GenrateSimpleStringLimit10()
        
        # Test Case Start Time
        starttime = time.process_time()
        
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                      'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                      'ServerName': ''+simplestring+'',
                      'ServerRole': '0',
                      'DBName': ''+self.ssinputdata.MainSecondaryDBName+'',
                      'DBServerName': ''+self.ssinputdata.MainSecondaryDBServerName+'',
                      'DBUsername': ''+self.ssinputdata.MainSecondaryDBUsername+'',
                      'DBPassword': ''+self.ssinputdata.MainSecondaryDBPassword+'',
                      'ServerMode': '0',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',
    
                    }
        
        # Url 
        URL = ''+common.Domain+''+self.UrlForUpdateSystemSettings+''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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

    # Start Test Case No 01-21
    def testcase_21_UpdateSystemSettings(self, TestCasesStatus=True):

        TestCaseID = '01-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings', 'Using Put Method System Settings',
                      'Configure the system settings server role as secondary and server mode value is equal to a.')
        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # Generate Simple Character String Limit 10 Characters
        simplestring = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        ServerRole = 'Secondary'
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': '' + self.ssinputdata.MainPrimaryServerIP + '',
                      'SecondaryServerIP': '' + self.ssinputdata.MainSecondaryServerIP + '',
                      'ServerName': '' + simplestring + '',
                      'ServerRole': '1',
                      'DBName': '' + self.ssinputdata.MainPrimaryDBName + '',
                      'DBServerName': '' + self.ssinputdata.MainPrimaryDBServerName + '',
                      'DBUsername': '' + self.ssinputdata.MainPrimaryDBUsername + '',
                      'DBPassword': '' + self.ssinputdata.MainPrimaryDBPassword + '',
                      'ServerMode': 'a',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',

                      }

        # Url
        URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # SQL Queries for Data Verification
        SQLCommand1 = (
                    "Select SecondaryServerIP From DefaultSettings Where SecondaryServerIP = '" + self.ssinputdata.MainSecondaryServerIP + "';")
        cursor.execute(SQLCommand1)
        secondaryserverip = cursor.fetchone()
        SQLCommand2 = ("Select ServerRole From DefaultSettings where ServerRole = '" + ServerRole + "';")
        cursor.execute(SQLCommand2)
        serverrole = cursor.fetchone()
        cursor.commit()
        status = ""
        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400:


                    # print('a')
                    # if secondaryserverip[0] == self.ssinputdata.MainSecondaryServerIP:
                    #     print('b')
                    #     if serverrole[0] == ServerRole:
                    #         print(common.SuccessMessage)
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
   
            
    
class test_2_GetSystemSettings(TestCase):

    # Calling Input Data File
    ssinputdata = InputData.InputData()
    # Url for Get System Settings
    UrlForGetSystemSettings = '/SystemSettings/Get/'
    UrlForGetSystemSettings_GetNotificationSettings = '/SystemSettings/GetNotificationSettings/'
    
    # Start Test Case No 01-13
    def testcase_13_GetSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Get Method System Settings' , 'Get all Data of System Settings.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForGetSystemSettings+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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
    
    def testcase_20_GetSystemSettings(self, TestCasesStatus=True):
        
        TestCaseID = '01-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings' , 'Using Get Method System Settings' , 'Get all Data of System Settings with site session key.')
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      
                    }
        
        # Url
        URL = ''+common.Domain+''+self.UrlForGetSystemSettings+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        
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

    # Start Test Case No 01-22
    def testcase_22_GetSystemSettings(self, TestCasesStatus=True):

        TestCaseID = '01-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings', 'Using Get Method System Settings', 'Get all Data of System Settings with Invalid AuthUser.')

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': 'Abc-user',

                      }

        # Url
        URL = '' + common.Domain + '' + self.UrlForGetSystemSettings + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End
            
            
    # def testcase_21_GetSystemSettings_NotificationSettings(self, TestCasesStatus=True):
    #
    #     TestCaseID = '01-21'
    #     # Calling Common Functions
    #     common = CF.CommonFunctions()
    #     common.Header('System Settings' , 'Using Get Method System notification Settings' , 'Get System Notification Settings with valid data')
    #
    #     # Test Case Start Time
    #     starttime = time.process_time()
    #     # Header Parameters of Rest API
    #     Parameters = {'AuthToken':''+common.authkey_server()+'',
    #                   'AuthUser':''+common.authuser+'',
    #
    #                 }
    #
    #     # Url
    #     URL = ''+common.Domain+''+self.UrlForGetSystemSettings_GetNotificationSettings+''
    #     # Hit API Through Methods
    #     response = requests.get(URL, headers=Parameters)
    #     # API Response in JSon Format
    #     resp=response.json()
    #     #print(resp)
    #     #showcode = str(resp['ResponseCode'])
    #
    #     # Response Code Verification
    #     if TestCasesStatus==True:
    #         try:
    #             if resp['ResponseCode'] == 200:
    #                 print(common.SuccessMessage)
    #                 status = 'Passed'
    #             else:
    #                 status = 'Failed'
    #                 assert False
    #
    #         # Write Output Result in Excel File
    #         finally:
    #             print(" ")
    #             common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
    #     else:
    #         TestCasesStatus=False
    #         # Test Case End
    #
            
            
class test_3_NegitiveSystemSettings(TestCase):
    # Calling Input Data File
    ssinputdata = InputData.InputData()
    # Url for Get System Settings
    UrlForGetSystemSettings = '/SystemSettings/Get/'
    UrlForGetSystemSettings_GetNotificationSettings = '/SystemSettings/GetNotificationSettings/'
    # Url For Update System Settings
    UrlForUpdateSystemSettings = '/SystemSettings/UpdateSystemSettings/'

    # Start Test Case No 01-23
    def testcase_01_GetSystemSettings(self, TestCasesStatus=True):

        TestCaseID = '01-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings', 'Using Get Method System Settings', 'Get all Data of System Settings with invalid token to verify the internal error code is give in the response.')

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {
            'AuthToken': "InvalidToken_@123456",  # Invalid token
            'AuthUser': config.auth_user
        }

        # Url
        URL = '' + common.Domain + '' + self.UrlForGetSystemSettings + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 401 and resp.get('InternalErrorCode'):
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(
                    SheetName,
                    TestCaseID,
                    URL,
                    Parameters,
                    status,
                    starttime,
                    resp,
                    TestDescription="Negative case: invalid AuthToken used; expecting 401 Unauthorized presence of InternalErrorCode.",
                    Methods="GET Method",
                    Steps="Send request with invalid AuthToken and check 401 status and presence of InternalErrorCode.",
                    ExpectedResult="401 Unauthorized with a valid InternalErrorCode",
                    ExpectedProcessingTime=2,
                    ExpectedResponseJSON={
                        'ResponseCode': 401,
                        'ResponseDescription': 'BAD REQUEST',
                        'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                        "list": "null",
                        'TotalRecords': 0
                    },
                    ExpectedCode=401
                )
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 01-24
    def testcase_02_GetSystemSettings(self, TestCasesStatus=True):

            TestCaseID = '01-24'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Get Method System Settings',
                          'Get all Data of System Settings with invalid user to verify the internal error code is give in the response.')

            # Test Case Start Time
            starttime = time.process_time()
            # Header Parameters of Rest API
            Parameters = {
                'AuthToken': config.sessionkey,
                'AuthUser': "InvalidUser123"
            }

            # Url
            URL = '' + common.Domain + '' + self.UrlForGetSystemSettings + ''
            # Hit API Through Methods
            response = requests.get(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 401 and resp.get('InternalErrorCode'):
                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: invalid AuthUser used; expecting 401 Unauthorized and InternalErrorCode present.",
                        Methods="GET Method",
                        Steps="Send request with invalid AuthUser and valid AuthToken, check 401 status and presence of InternalErrorCode.",
                        ExpectedResult="401 Unauthorized with a valid InternalErrorCode",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 401,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 0
                        },
                        ExpectedCode=401
                    )
            else:
                TestCasesStatus = False
                # Test Case End

    # Start Test Case No 01-25
    def testcase_03_GetSystemSettings(self, TestCasesStatus=True):

            TestCaseID = '01-25'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Get Method System Settings',
                          'Get all Data of System Settings with empty AuthToken to verify if unauthorized response with InternalErrorCode is returned.')

            # Test Case Start Time
            starttime = time.process_time()
            # Header Parameters of Rest API
            Parameters = {
                'AuthToken': '',
                'AuthUser': "InvalidUser123"
            }

            # Url
            URL = '' + common.Domain + '' + self.UrlForGetSystemSettings + ''
            # Hit API Through Methods
            response = requests.get(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):
                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: empty AuthToken used; expecting 401 Unauthorized and InternalErrorCode present.",
                        Methods="GET Method",
                        Steps="Send request with empty AuthToken and valid AuthUser, verify 401 Unauthorized and check InternalErrorCode presence.",
                        ExpectedResult="400 Unauthorized with a valid InternalErrorCode",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 400,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 0
                        },
                        ExpectedCode=400
                    )
            else:
                TestCasesStatus = False
                # Test Case End


    # Start Test Case No 01-26
    def testcase_04_GetSystemSettings(self, TestCasesStatus=True):

        TestCaseID = '01-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings', 'Using Get Method System Settings',
                      'Get all Data of System Settings with empty AuthUser to verify if unauthorized response with InternalErrorCode is returned.')

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {
            'AuthToken': config.sessionkey,
            'AuthUser': ""
        }

        # Url
        URL = '' + common.Domain + '' + self.UrlForGetSystemSettings + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(
                    SheetName,
                    TestCaseID,
                    URL,
                    Parameters,
                    status,
                    starttime,
                    resp,
                    TestDescription="Negative case: empty AuthUser used; expecting 401 Unauthorized and InternalErrorCode present.",
                    Methods="GET Method",
                    Steps="Send request with valid AuthToken and empty AuthUser, verify 401 Unauthorized and check InternalErrorCode presence.",
                    ExpectedResult="400 Unauthorized with a valid InternalErrorCode",
                    ExpectedProcessingTime=2,
                    ExpectedResponseJSON={
                        'ResponseCode': 400,
                        'ResponseDescription': 'BAD REQUEST',
                        'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                        "list": "null",
                        'TotalRecords': 0
                    },
                    ExpectedCode=400
                )
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 01-27
    def testcase_05_UpdateSystemSettings(self, TestCasesStatus=True):



            TestCaseID = '01-27'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Put Method System Settings',
                          'Negative case: Configure the System Settings with invalid PrimaryServerIP ')
            # Generate Simple Character String Limit 10 Characters
            simplestring = common.GenrateSimpleStringLimit10()

            # Test Case Start Time
            starttime = time.process_time()

            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'PrimaryServerIP': '999.999.999.999',  # Invalid IP address
                          'SecondaryServerIP': '' + self.ssinputdata.MainSecondaryServerIP + '',
                          'ServerName': '' + simplestring + '',
                          'ServerRole': '0',
                          'DBName': '' + self.ssinputdata.MainSecondaryDBName + '',
                          'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                          'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                          'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                          'ServerMode': '0',
                          'BranchServerIP': '',
                          'OPRID': '',
                          'Recorder': '0',
                          'BranchRemoteIP': '',

                          }

            # Url
            URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
            # Hit API Through Methods
            response = requests.put(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: Invalid PrimaryServerIP format (e.g., 999.999.999.999); expecting 400 Bad Request with InternalErrorCode.",
                        Methods="Put Method",
                        Steps="Send request with invalid PrimaryServerIP and observe if the system rejects with 400 and InternalErrorCode.",
                        ExpectedResult="400 Bad Request with a valid InternalErrorCode indicating invalid IP format.",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 400,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 400
                        },
                        ExpectedCode=400
                    )
            else:
                TestCasesStatus = False
                # Test Case End


    # Start Test Case No 01-28
    def testcase_06_UpdateSystemSettings(self, TestCasesStatus=True):



            TestCaseID = '01-28'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Put Method System Settings',
                          'Negative case: Configure the System Settings with invalid SecondaryServerIP ')
            # Generate Simple Character String Limit 10 Characters
            simplestring = common.GenrateSimpleStringLimit10()

            # Test Case Start Time
            starttime = time.process_time()

            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                          'SecondaryServerIP': '999.999.999.999',  # Invalid IP address
                          'ServerName': '' + simplestring + '',
                          'ServerRole': '0',
                          'DBName': '' + self.ssinputdata.MainSecondaryDBName + '',
                          'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                          'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                          'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                          'ServerMode': '0',
                          'BranchServerIP': '',
                          'OPRID': '',
                          'Recorder': '0',
                          'BranchRemoteIP': '',

                          }

            # Url
            URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
            # Hit API Through Methods
            response = requests.put(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: Invalid SecondaryServerIP format (e.g., 999.999.999.999); expecting 400 Bad Request with InternalErrorCode.",
                        Methods="Put Method",
                        Steps="Send request with invalid SecondaryServerIP and observe if the system rejects with 400 and InternalErrorCode.",
                        ExpectedResult="400 Bad Request with a valid InternalErrorCode indicating invalid IP format.",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 400,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 400
                        },
                        ExpectedCode=400
                    )
            else:
                TestCasesStatus = False
                # Test Case End


    # Start Test Case No 01-29
    def testcase_07_UpdateSystemSettings(self, TestCasesStatus=True):

        TestCaseID = '01-29'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings', 'Using Put Method System Settings',
                      'Negative case: Configure the System Settings with invalid PrimaryServerIP & SecondaryServerIP ')
        # Generate Simple Character String Limit 10 Characters
        simplestring = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()

        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': '999.999.999.999',  # Invalid IP address
                      'SecondaryServerIP': '999.999.999.999',  # Invalid IP address
                      'ServerName': '' + simplestring + '',
                      'ServerRole': '0',
                      'DBName': '' + self.ssinputdata.MainSecondaryDBName + '',
                      'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                      'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                      'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                      'ServerMode': '0',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',

                      }

        # Url
        URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(
                    SheetName,
                    TestCaseID,
                    URL,
                    Parameters,
                    status,
                    starttime,
                    resp,
                    TestDescription="Negative case: Invalid PrimaryServerIP & SecondaryServerIP format (e.g., 999.999.999.999); expecting 400 Bad Request with InternalErrorCode.",
                    Methods="Put Method",
                    Steps="Send request with invalid PrimaryServerIP & SecondaryServerIP and observe if the system rejects with 400 and InternalErrorCode.",
                    ExpectedResult="400 Bad Request with a valid InternalErrorCode indicating invalid IP format.",
                    ExpectedProcessingTime=2,
                    ExpectedResponseJSON={
                        'ResponseCode': 400,
                        'ResponseDescription': 'BAD REQUEST',
                        'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                        "list": "null",
                        'TotalRecords': 400
                    },
                    ExpectedCode=400
                )
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 01-30
    def testcase_08_UpdateSystemSettings(self, TestCasesStatus=True):

            TestCaseID = '01-30'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Put Method System Settings',
                          'Negative case: Configure the System Settings with empty ServerRole')

            # Generate Simple Character String Limit 10 Characters
            simplestring = common.GenrateSimpleStringLimit10()

            # Test Case Start Time
            starttime = time.process_time()

            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                          'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                          'ServerName': '' + simplestring + '',
                          'ServerRole': '',  # Empty value (negative test)
                          'DBName': '' + self.ssinputdata.MainSecondaryDBName + '',
                          'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                          'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                          'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                          'ServerMode': '0',
                          'BranchServerIP': '',
                          'OPRID': '',
                          'Recorder': '0',
                          'BranchRemoteIP': '',

                          }

            # Url
            URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
            # Hit API Through Methods
            response = requests.put(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: Empty ServerRole field; expecting 400 Bad Request with InternalErrorCode.",
                        Methods="PUT Method",
                        Steps="Send request with empty ServerRole and verify that the system responds with proper error.",
                        ExpectedResult="400 Bad Request with a valid InternalErrorCode indicating missing or invalid ServerRole.",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 400,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 400
                        },
                        ExpectedCode=400
                    )
            else:
                TestCasesStatus = False
                # Test Case End


    # Start Test Case No 01-31
    def testcase_09_UpdateSystemSettings(self, TestCasesStatus=True):

            TestCaseID = '01-31'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Put Method System Settings',
                          'Negative case: Configure the System Settings with missing ServerRole header')

            # Generate Simple Character String Limit 10 Characters
            simplestring = common.GenrateSimpleStringLimit10()

            # Test Case Start Time
            starttime = time.process_time()

            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'PrimaryServerIP': ''+self.ssinputdata.MainPrimaryServerIP+'',
                          'SecondaryServerIP': ''+self.ssinputdata.MainSecondaryServerIP+'',
                          'ServerName': '' + simplestring + '',
                          # without ServerRole Header
                          'DBName': '' + self.ssinputdata.MainSecondaryDBName + '',
                          'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                          'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                          'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                          'ServerMode': '0',
                          'BranchServerIP': '',
                          'OPRID': '',
                          'Recorder': '0',
                          'BranchRemoteIP': '',

                          }

            # Url
            URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
            # Hit API Through Methods
            response = requests.put(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: missing ServerRole header; expecting 400 Bad Request with InternalErrorCode.",
                        Methods="PUT Method",
                        Steps="Send request with missing ServerRole header and verify that the system responds with proper error.",
                        ExpectedResult="400 Bad Request with a valid InternalErrorCode indicating missing or invalid ServerRole.",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 400,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 400
                        },
                        ExpectedCode=400
                    )
            else:
                TestCasesStatus = False
                # Test Case End


    # Start Test Case No 01-32
    def testcase_10_UpdateSystemSettings(self, TestCasesStatus=True):

        TestCaseID = '01-32'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('System Settings', 'Using Put Method System Settings',
                      'Negative case: Configure the System Settings with invalid ServerRole (e.g., "abc!@#")')

        # Generate Simple Character String Limit 10 Characters
        simplestring = common.GenrateSimpleStringLimit10()

        # Test Case Start Time
        starttime = time.process_time()

        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'PrimaryServerIP': '' + self.ssinputdata.MainPrimaryServerIP + '',
                      'SecondaryServerIP': '' + self.ssinputdata.MainSecondaryServerIP + '',
                      'ServerName': '' + simplestring + '',
                      'ServerRole': 'abc!@#',  # Invalid ServerRole
                      'DBName': '' + self.ssinputdata.MainSecondaryDBName + '',
                      'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                      'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                      'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                      'ServerMode': '0',
                      'BranchServerIP': '',
                      'OPRID': '',
                      'Recorder': '0',
                      'BranchRemoteIP': '',

                      }

        # Url
        URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            # Write Output Result in Excel File
            finally:
                common.UpdateExcelTestCase(
                    SheetName,
                    TestCaseID,
                    URL,
                    Parameters,
                    status,
                    starttime,
                    resp,
                    TestDescription="Negative case: Invalid ServerRole (e.g., 'abc!@#'); expecting 400 Bad Request with InternalErrorCode.",
                    Methods="PUT Method",
                    Steps="Send request with ServerRole value as 'abc!@#' and verify the response indicates invalid role format.",
                    ExpectedResult="400 Bad Request with an InternalErrorCode indicating invalid ServerRole input.",
                    ExpectedProcessingTime=2,
                    ExpectedResponseJSON={
                        'ResponseCode': 400,
                        'ResponseDescription': 'BAD REQUEST',
                        'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                        "list": "null",
                        'TotalRecords': 400
                    },
                    ExpectedCode=400
                )
        else:
            TestCasesStatus = False
            # Test Case End

    # Start Test Case No 01-33
    def testcase_11_UpdateSystemSettings(self, TestCasesStatus=True):

            TestCaseID = '01-33'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Put Method System Settings',
                          'Negative case: Configure the System Settings with incorrect DBName')

            # Generate Simple Character String Limit 10 Characters
            simplestring = common.GenrateSimpleStringLimit10()

            # Test Case Start Time
            starttime = time.process_time()

            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'PrimaryServerIP': '' + self.ssinputdata.MainPrimaryServerIP + '',
                          'SecondaryServerIP': '' + self.ssinputdata.MainSecondaryServerIP + '',
                          'ServerName': '' + simplestring + '',
                          'ServerRole': '0',
                          'DBName': 'Wrong_DB_Name_XYZ@@#',  # Invalid DB name
                          'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                          'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                          'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                          'ServerMode': '0',
                          'BranchServerIP': '',
                          'OPRID': '',
                          'Recorder': '0',
                          'BranchRemoteIP': '',

                          }

            # Url
            URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
            # Hit API Through Methods
            response = requests.put(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: Invalid DBName provided; expecting 400 Bad Request due to database connection failure or invalid configuration with InternalErrorCode",
                        Methods="PUT Method",
                        Steps="Send request with a deliberately incorrect DBName and verify the API returns an appropriate error.",
                        ExpectedResult="400 Bad Request with an InternalErrorCode indicating DB name is invalid or unreachable.",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 400,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 400
                        },
                        ExpectedCode=400
                    )
            else:
                TestCasesStatus = False
                # Test Case End


    # Start Test Case No 01-34
    def testcase_12_UpdateSystemSettings(self, TestCasesStatus=True):

            TestCaseID = '01-34'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('System Settings', 'Using Put Method System Settings',
                          'Negative case: Configure the System Settings with missing DBName Header')

            # Generate Simple Character String Limit 10 Characters
            simplestring = common.GenrateSimpleStringLimit10()

            # Test Case Start Time
            starttime = time.process_time()

            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'PrimaryServerIP': '' + self.ssinputdata.MainPrimaryServerIP + '',
                          'SecondaryServerIP': '' + self.ssinputdata.MainSecondaryServerIP + '',
                          'ServerName': '' + simplestring + '',
                          'ServerRole': '0',
                           # with missing DBName Header
                          'DBServerName': '' + self.ssinputdata.MainSecondaryDBServerName + '',
                          'DBUsername': '' + self.ssinputdata.MainSecondaryDBUsername + '',
                          'DBPassword': '' + self.ssinputdata.MainSecondaryDBPassword + '',
                          'ServerMode': '0',
                          'BranchServerIP': '',
                          'OPRID': '',
                          'Recorder': '0',
                          'BranchRemoteIP': '',

                          }

            # Url
            URL = '' + common.Domain + '' + self.UrlForUpdateSystemSettings + ''
            # Hit API Through Methods
            response = requests.put(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            # showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp.get('InternalErrorCode'):

                        print(common.SuccessMessage)
                        status = 'Passed'
                    else:
                        status = 'Failed'
                        assert False

                # Write Output Result in Excel File
                finally:
                    common.UpdateExcelTestCase(
                        SheetName,
                        TestCaseID,
                        URL,
                        Parameters,
                        status,
                        starttime,
                        resp,
                        TestDescription="Negative case: with missing DBName Header; expecting 400 Bad Request due to database connection failure or invalid configuration with InternalErrorCode",
                        Methods="PUT Method",
                        Steps="Send request with a deliberately with missing DBName Header and verify the API returns an appropriate error.",
                        ExpectedResult="400 Bad Request with an InternalErrorCode indicating with missing DBName Header or unreachable.",
                        ExpectedProcessingTime=2,
                        ExpectedResponseJSON={
                            'ResponseCode': 400,
                            'ResponseDescription': 'BAD REQUEST',
                            'InternalErrorCode': 'SomeErrorCode',  # generic placeholder
                            "list": "null",
                            'TotalRecords': 400
                        },
                        ExpectedCode=400
                    )
            else:
                TestCasesStatus = False
                # Test Case End