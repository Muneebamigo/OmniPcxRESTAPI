'''
Created on Oct 17, 2018

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
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from test_Provisioning import test_37_Equipment as EquipmentFun
from test_Provisioning import test_03_PacketizerConfiguration as PacketizerFun
from Key import config
from Key_User import config as boardUser

SheetName=	'36-Board'

class test_1_AddBoard(TestCase):
    
    # Start Test Case No 36-01
    def testcase_01_AddBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Post Method to Add Board' , 'Add Board with all valid Data.')
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Add Board    
        UrlforAddBoard = '/Board/Add'
        URL = ''+common.Domain+''+UrlforAddBoard +''
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
              
        return Name
    # Test Case End
    
    # Start Test Case No 36-02
    def testcase_02_AddBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Post Method to Add Board' , 'Add Board with Duplicate Board Name.')
        # Add Board Function calling
        Name = test_1_AddBoard.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Add Board    
        UrlforAddBoard = '/Board/Add'
        URL = ''+common.Domain+''+UrlforAddBoard +''
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
    
    # Start Test Case No 36-03
    def testcase_03_AddBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Post Method to Add Board' , 'Add Board When Board name character more then 250.')
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateDesc250()
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
                      
                    }
        
        # Url For Add Board   
        UrlforAddBoard = '/Board/Add'
        URL = ''+common.Domain+''+UrlforAddBoard +''
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
    
    # Start Test Case No 36-04
    def testcase_04_AddBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Post Method to Add Board' , 'Add Board When Board name Empty/Null.')
        
        # Generate Simple Character String Limit 10 Characters
        Name = ''
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Add Board    
        UrlforAddBoard = '/Board/Add'
        URL = ''+common.Domain+''+UrlforAddBoard +''
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
    
    # Start Test Case No 36-05
    def testcase_05_AddBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Post Method to Add Board' , 'Add Board When Logicalname more then 250 characters.')
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName=common.GenrateDesc250()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Add Board  
        UrlforAddBoard = '/Board/Add'
        URL = ''+common.Domain+''+UrlforAddBoard +''
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
    
    # Start Test Case No 36-06
    def testcase_06_AddBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Post Method to Add Board' , 'Add Board with all valid Data when server role configured as secondary.')
       
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Add Board    
        UrlforAddBoard = '/Board/Add'
        URL = ''+common.Domain+''+UrlforAddBoard +''
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
    
    # Start Test Case No 36-14
    def testcase_07_AddBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Post Method to Add Board' , 'Add Board with all valid Data. when server role configured as branch recorder.')
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Add Board    
        UrlforAddBoard = '/Board/Add'
        URL = ''+common.Domain+''+UrlforAddBoard +''
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
    
class test_2_UpdateBoard(TestCase):
    
    # Start Test Case No 36-07
    def testcase_01_UpdateBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Put Method to Update Board' , 'Update Board with valid BoardID.')
        # Add Board Function calling
        name = test_1_AddBoard.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Update Board   
        UrlforUpdateBoard = '/Board/Update'
        URL = ''+common.Domain+''+UrlforUpdateBoard +''
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
    
    # Start Test Case No 36-08
    def testcase_02_UpdateBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Put Method to Update Board' , 'Update Board with invalid/Non Existing BoardID.')
        
        BoardID='12345'
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName=common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'BoardID': ''+BoardID+'',
                      'Name': ''+Name+'',   
                      'LogicalName': ''+LogicalName+'',
    
                    }
        
        # Url For Update Board    
        UrlforUpdateBoard = '/Board/Update'
        URL = ''+common.Domain+''+UrlforUpdateBoard +''
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
    
class test_3_GetBoard(TestCase):
    
    # Start Test Case No 36-09
    def testcase_01_GetBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Get Method to Get Board data' , 'Get all Board data with valid input data.')
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': '',
    
                    }
        
        # Url For Get Board   
        UrlforGetBoard = '/Board/Get/'
        URL = ''+common.Domain+''+UrlforGetBoard +''
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
    
    # Start Test Case No 36-10
    def testcase_02_UpdateBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Get Method to Get Board data' , 'Get a single Board data with valid ID.')
        # Add Board Function calling
        Name = test_1_AddBoard.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+BoardID+'',
    
                    }
        
        # Url For Get Board    
        UrlforGetBoard = '/Board/Get/'
        URL = ''+common.Domain+''+UrlforGetBoard+''+BoardID+''
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
    
    # Start Test Case No 36-11
    def testcase_03_UpdateBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Get Method to Get Board data' , 'Get a single Board data with invalid/Non Existing ID.')
        
        BoardID='12345'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+BoardID+'',
    
                    }
        
        # Url For Get Board    
        UrlforGetBoard = '/Board/Get/'
        URL = ''+common.Domain+''+UrlforGetBoard+''+BoardID+''
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
    
class test_4_DeleteBoard(TestCase):
    
    # Start Test Case No 36-12
    def testcase_01_DeleteBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Delete Method to Delete Board data' , 'Delete a single Board data with valid ID.')
        # Add Board Function calling
        Name = test_1_AddBoard.testcase_01_AddBoard(common.PrereqTestCasesStatusUpdate)
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select BoardID From Board Where Name = '"+Name+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        BoardID=str(val[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+BoardID+'',
    
                    }
        
        # Url For Delete Board    
        UrlforDeleteBoard = '/Board/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteBoard+''+BoardID+''
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
    
    # Start Test Case No 36-13
    def testcase_02_DeleteBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Delete Method to Delete Board data' , 'Delete a single Board data with invalid/Non Existing ID.')
        
        BoardID='12345'
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+BoardID+'',
    
                    }
        
        # Url For Delete Board    
        UrlforDeleteBoard = '/Board/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteBoard+''+BoardID+''
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
    
    
    # Start Test Case No 36-15
    def testcase_03_DeleteBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Delete Method to Delete Board data' , 'Delete a single Board data with valid ID that is associated with equipment.')
        
        # Add Equipment Function calling
        EquipmentFunctions= EquipmentFun.test_1_AddEquipment()
        EquipmentNumber, BoardID, TrunkGroupID = EquipmentFunctions.testcase_01_AddEquipment(common.PrereqTestCasesStatusUpdate)
        TrunkGroupID=TrunkGroupID
        EquipmentNumber=EquipmentNumber
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+BoardID+'',
    
                    }
        
        # Url For Delete Board    
        UrlforDeleteBoard = '/Board/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteBoard+''+BoardID+''
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
    
    
    # Start Test Case No 36-16
    def testcase_04_DeleteBoard(self, TestCasesStatus=True): 
        
        TestCaseID = '36-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board' , 'Using Delete Method to Delete Board data' , 'Delete a single Board data with valid ID that is associated with Packetizer.')
        
        # Add Packetizer Function calling
        PacketizerFunctions= PacketizerFun.test_1_AddPacketizerConfiguration()
        PcktIP,BoardID,TrunkGroupID = PacketizerFunctions.testcase_22_AddPacketizerConfiguration(common.PrereqTestCasesStatusUpdate)
        PcktIP=PcktIP
        TrunkGroupID=TrunkGroupID
        
        # Test Case Start Time
        starttime = time.process_time()   
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                      'AuthUser':config.auth_user,
                      'ID': ''+BoardID+'',
    
                    }
        
        # Url For Delete Board    
        UrlforDeleteBoard = '/Board/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteBoard+''+BoardID+''
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

# This class cases added by muneeb.ahmed in release 2.5.0.17
class test_5_BoardErrorCodes(TestCase):

    # Start Test Case No 36-21
    def testcase_01_AddBoard(self, TestCasesStatus=True):

        TestCaseID = '36-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board', 'Using Post Method to Add Board', 'Add Board When Board name character more then 250.')
        # System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateDesc250()
        LogicalName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': '' + Name + '',
                      'LogicalName': '' + LogicalName + '',

                      }

        # Url For Add Board
        UrlforAddBoard = '/Board/Add'
        URL = '' + common.Domain + '' + UrlforAddBoard + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400 and resp['InternalErrorCode'] == 'OPRBd06':
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

        # Start Test Case No 36-01

    # Start Test Case No 36-22
    def testcase_02_AddBoard(self, TestCasesStatus=True):

        TestCaseID = '36-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board', 'Using Post Method to Add Board', 'Add Board with all valid Data.')
        # System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName = common.GenrateDesc250()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': '' + Name + '',
                      'LogicalName': '' + LogicalName + '',

                      }

        # Url For Add Board
        UrlforAddBoard = '/Board/Add'
        URL = '' + common.Domain + '' + UrlforAddBoard + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400 and resp['InternalErrorCode'] == 'OPRBd07':
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

        return Name
    # Test Case End

    # Start Test Case No 36-23
    def testcase_03_UpdateBoard(self, TestCasesStatus=True):

            TestCaseID = '36-33'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('Board', 'Using Get Method to Get Board data',
                          'Get a single Board data with invalid/Non Existing ID.')

            BoardID = '123455'
            # Test Case Start Time
            starttime = time.process_time()
            # Header Parameters of Rest API
            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'ID': '' + BoardID + '',

                          }

            # Url For Get Board
            UrlforGetBoard = '/Board/Get/'
            URL = '' + common.Domain + '' + UrlforGetBoard + '' + BoardID + ''
            # Hit API Through Methods
            response = requests.get(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp['InternalErrorCode'] == 'OPRBd08':
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

    # Start Test Case No 36-24
    def testcase_04_DeleteBoard(self, TestCasesStatus=True):

        TestCaseID = '36-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board', 'Using Delete Method to Delete Board data',
                      'Delete a single Board data with valid ID that is associated with equipment.')

        # Add Equipment Function calling
        EquipmentFunctions = EquipmentFun.test_1_AddEquipment()
        EquipmentNumber, BoardID, TrunkGroupID = EquipmentFunctions.testcase_01_AddEquipment(
            common.PrereqTestCasesStatusUpdate)
        TrunkGroupID = TrunkGroupID
        EquipmentNumber = EquipmentNumber

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': '' + BoardID + '',

                      }

        # Url For Delete Board
        UrlforDeleteBoard = '/Board/Delete/'
        URL = '' + common.Domain + '' + UrlforDeleteBoard + '' + BoardID + ''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 409 and resp['InternalErrorCode'] == 'OPRBd11':
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

    # Start Test Case No 36-25
    def testcase_05_DeleteBoard(self, TestCasesStatus=True):

            TestCaseID = '36-25'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('Board', 'Using Delete Method to Delete Board data',
                          'Delete a single Board data with valid ID that is associated with Packetizer.')

            # Add Packetizer Function calling
            PacketizerFunctions = PacketizerFun.test_1_AddPacketizerConfiguration()
            PcktIP, BoardID, TrunkGroupID = PacketizerFunctions.testcase_22_AddPacketizerConfiguration(
                common.PrereqTestCasesStatusUpdate)
            PcktIP = PcktIP
            TrunkGroupID = TrunkGroupID

            # Test Case Start Time
            starttime = time.process_time()
            # Header Parameters of Rest API
            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'ID': '' + BoardID + '',

                          }

            # Url For Delete Board
            UrlforDeleteBoard = '/Board/Delete/'
            URL = '' + common.Domain + '' + UrlforDeleteBoard + '' + BoardID + ''
            # Hit API Through Methods
            response = requests.delete(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 409 and resp['InternalErrorCode'] == 'OPRBd14':
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

    # Start Test Case No 36-26
    def testcase_06_AddBoard(self, TestCasesStatus=True):

        TestCaseID = '36-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Board', 'Using Post Method to Add Board', 'Add Board with all valid Data. Without user rights to board')
        # System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        LogicalName = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': boardUser.sessionkey,
                      'AuthUser': boardUser.auth_user,
                      'Name': '' + Name + '',
                      'LogicalName': '' + LogicalName + '',

                      }

        # Url For Add Board
        UrlforAddBoard = '/Board/Add'
        URL = '' + common.Domain + '' + UrlforAddBoard + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 403 and resp['InternalErrorCode'] == 'OPRBd12':
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

        return Name
    # Test Case End