'''
Created on Oct 17, 2018

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
from test_Provisioning import test_36_Board as BF
from test_Provisioning import test_38_TrunkGroup as TGF
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from Key import config
SheetName=	'37-Equipment'

class test_1_AddEquipment(TestCase):
    
    # Start Test Case No 37-01
    def testcase_01_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with all valid Data.')
        # Add Board Function calling
        BoardFunctions=BF.test_1_AddBoard()
        name=BoardFunctions.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Add Trunk Group Function calling
        TrunkGroupFunctions=TGF.test_1_AddTrunkGroup()
        Name, PBXID=TrunkGroupFunctions.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        TrunkGroupID=str(val[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        EquipmentNumber = str(random.randint(10 , 999))
        
        # Test Case Start Time
        starttime = time.process_time() 
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
              
        return EquipmentNumber, BoardID, TrunkGroupID
                
    # Test Case End
    
    # Start Test Case No 37-02
    def testcase_02_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with Duplicate EquipmentNumber.')
        # Add Equipment Function calling
        EquipmentNumber, BoardID, TrunkGroupID=test_1_AddEquipment.testcase_01_AddEquipment(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
    
    # Start Test Case No 37-03
    def testcase_03_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with Null/Empty EquipmentNumber.')
        # Add Board Function calling
        BoardFunctions=BF.test_1_AddBoard()
        name=BoardFunctions.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Add Trunk Group Function calling
        TrunkGroupFunctions=TGF.test_1_AddTrunkGroup()
        Name, PBXID=TrunkGroupFunctions.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        TrunkGroupID=str(val[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': '',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
    
    # Start Test Case No 37-04
    def testcase_04_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with invalid/Non Existing BoardID.')
       
        # Add Trunk Group Function calling
        TrunkGroupFunctions=TGF.test_1_AddTrunkGroup()
        Name, PBXID=TrunkGroupFunctions.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        TrunkGroupID=str(val[0])
        cursor.commit()
        
        EquipmentNumber=str(random.randint(10 , 999))
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': '12345',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
    
    # Start Test Case No 37-05
    def testcase_05_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with in valid or non existing TrunkGroupID.')
        # Add Board Function calling
        BoardFunctions=BF.test_1_AddBoard()
        name=BoardFunctions.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        TrunkGroupID='123456'
        # Generate Simple Character String Limit 10 Characters
        EquipmentNumber = str(random.randint(10 , 999))
        
        # Test Case Start Time
        starttime = time.process_time() 
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
    
    # Start Test Case No 37-06
    def testcase_06_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with invalid EquipmentNumber.')
        # Add Board Function calling
        BoardFunctions=BF.test_1_AddBoard()
        name=BoardFunctions.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Add Trunk Group Function calling
        TrunkGroupFunctions=TGF.test_1_AddTrunkGroup()
        Name, PBXID=TrunkGroupFunctions.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        TrunkGroupID=str(val[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        EquipmentNumber = 'a12b!@#$%1Zt'
        
        # Test Case Start Time
        starttime = time.process_time() 
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
    
    # Start Test Case No 37-07
    def testcase_07_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with all valid Data when server role configured as secondary.')
        # Add Board Function calling
        BoardFunctions=BF.test_1_AddBoard()
        name=BoardFunctions.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Add Trunk Group Function calling
        TrunkGroupFunctions=TGF.test_1_AddTrunkGroup()
        Name, PBXID=TrunkGroupFunctions.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        TrunkGroupID=str(val[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        EquipmentNumber = str(random.randint(10 , 999))
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
    
    # Start Test Case No 37-08
    def testcase_08_AddEquipment(self, TestCasesStatus=True): 
        
        TestCaseID = '37-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Post Method to Add Equipment' , 'Add Equipment with all valid Data when server role configured as branch recorder.')
        # Add Board Function calling
        BoardFunctions=BF.test_1_AddBoard()
        name=BoardFunctions.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Add Trunk Group Function calling
        TrunkGroupFunctions=TGF.test_1_AddTrunkGroup()
        Name, PBXID=TrunkGroupFunctions.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
        PBXID=PBXID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        TrunkGroupID=str(val[0])
        cursor.commit()
        # Generate Simple Character String Limit 10 Characters
        EquipmentNumber = str(random.randint(10 , 999))
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Add Equipment    
        UrlforAddEquipment = '/Equipment/Add'
        URL = ''+common.Domain+''+UrlforAddEquipment+''
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
    
class test_2_UpdateEquipment(TestCase):
    
    # Start Test Case No 37-09
    def testcase_01_UpdateEquipment(self, TestCasesStatus=True):
        
        TestCaseID = '37-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Put Method to Update Equipment' , 'Update Equipment with valid EquipmentID.')
        # Add Equipment Function calling
        EquipmentNumber, BoardID, TrunkGroupID=test_1_AddEquipment.testcase_01_AddEquipment(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select EquipmentID From Equipment Where EquipmentNumber = '"+EquipmentNumber+"' and BoardID = '"+BoardID+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        EquipmentID=str(val[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'EquipmentID': ''+EquipmentID+'',  
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Update Equipment    
        UrlforUpdateEquipment = '/Equipment/Update'
        URL = ''+common.Domain+''+UrlforUpdateEquipment+''
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
    
    # Start Test Case No 37-10
    def testcase_02_UpdateEquipment(self, TestCasesStatus=True):
        
        TestCaseID = '37-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Put Method to Update Equipment' , 'Update Equipment with invalid/Non Existing EquipmentID.')
        # Add Equipment Function calling
        EquipmentNumber, BoardID, TrunkGroupID=test_1_AddEquipment.testcase_01_AddEquipment(common.PrereqTestCasesStatusUpdate)
        
        EquipmentID='123456'
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'EquipmentID': ''+EquipmentID+'',  
                      'BoardID': ''+BoardID+'',   
                      'EquipmentNumber': ''+EquipmentNumber+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Update Equipment    
        UrlforUpdateEquipment = '/Equipment/Update'
        URL = ''+common.Domain+''+UrlforUpdateEquipment+''
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
    
class test_3_GetEquipment(TestCase):
    
    # Start Test Case No 37-11
    def testcase_01_GetEquipment(self, TestCasesStatus=True):
        
        TestCaseID = '37-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Get Method to Get Equipment data' , 'Get all Equipment list with valid input data.')
        
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': '',
    
                    }
        
        # Url For Get Equipment    
        UrlforGetEquipment = '/Equipment/Get/'
        URL = ''+common.Domain+''+UrlforGetEquipment+''
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
    
    # Start Test Case No 37-12
    def testcase_02_GetEquipment(self, TestCasesStatus=True):
        
        TestCaseID = '37-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Get Method to Get Equipment data' , 'Get a single Equipment data with valid EquipmentID.')
        # Add Equipment Function calling
        EquipmentNumber, BoardID, TrunkGroupID=test_1_AddEquipment.testcase_01_AddEquipment(common.PrereqTestCasesStatusUpdate)
        TrunkGroupID=TrunkGroupID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select EquipmentID From Equipment Where EquipmentNumber = '"+EquipmentNumber+"' and BoardID = '"+BoardID+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        EquipmentID=str(val[0])
        cursor.commit()
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+EquipmentID+'',
    
                    }
        
        # Url For Get Equipment    
        UrlforGetEquipment = '/Equipment/Get/'
        URL = ''+common.Domain+''+UrlforGetEquipment+''+EquipmentID+''
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
    
    # Start Test Case No 37-13
    def testcase_03_GetEquipment(self, TestCasesStatus=True):
        
        TestCaseID = '37-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Get Method to Get Equipment data' , 'Get a single Equipment data with invalid/Non Existing EquipmentID.')
        
        EquipmentID='12345'
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+EquipmentID+'',
    
                    }
        
        # Url For Get Equipment    
        UrlforGetEquipment = '/Equipment/Get/'
        URL = ''+common.Domain+''+UrlforGetEquipment+''+EquipmentID+''
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
    
class test_4_DeleteEquipment(TestCase):
    
    # Start Test Case No 37-14
    def testcase_01_DeleteEquipment(self, TestCasesStatus=True):
        
        TestCaseID = '37-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Delete Method to Delete Equipment data' , 'Delete Equipment data with valid EquipmentID.')
        # Add Equipment Function calling
        EquipmentNumber, BoardID, TrunkGroupID=test_1_AddEquipment.testcase_01_AddEquipment(common.PrereqTestCasesStatusUpdate)
        TrunkGroupID=TrunkGroupID
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select EquipmentID From Equipment Where EquipmentNumber = '"+EquipmentNumber+"' and BoardID = '"+BoardID+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        EquipmentID=str(val[0])
        cursor.commit()
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+EquipmentID+'',
    
                    }
        
        # Url For Delete Equipment    
        UrlforDeleteEquipment = '/Equipment/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteEquipment+''+EquipmentID+''
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
    
    # Start Test Case No 37-15
    def testcase_02_DeleteEquipment(self, TestCasesStatus=True):
        
        TestCaseID = '37-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Equipment' , 'Using Delete Method to Delete Equipment data' , 'Delete Equipment data with invalid/Non Existing EquipmentID.')
        
        EquipmentID='12345'
        # Test Case Start Time
        starttime = time.process_time()  
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+EquipmentID+'',
    
                    }
        
        # Url For Delete Equipment    
        UrlforDeleteEquipment = '/Equipment/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteEquipment+''+EquipmentID+''
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