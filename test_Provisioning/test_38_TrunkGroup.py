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
from test_Provisioning import test_02_PBXConfiguration as PBXF
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from test_Provisioning import test_03_PacketizerConfiguration as PacketizerFun
from test_Provisioning import test_37_Equipment as EquipmentFun
from Key import config
from Key_User import config as trunkgUser

SheetName=	'38-Trunk Group'

class test_1_AddTrunkGroup(TestCase):
    
    # Start Test Case No 38-01
    def testcase_01_AddTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Post Method to Add Trunk Group' , 'Add Trunk Group with all valid Data.')
        # Add Node/PBX Function calling
        PBXFunctions=PBXF.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '"+OXEName+"' and OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        PBXID=str(val[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser':  config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
    
                    }
        
        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = ''+common.Domain+''+UrlforAddTrunkGroup +''
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
              
        return Name, PBXID
    # Test Case End
    
    # Start Test Case No 38-02
    def testcase_02_AddTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Post Method to Add Trunk Group' , 'Add Trunk Group with Duplicate Trunk name.')
        # Add Trunk Group Function calling
        Name, PBXID = test_1_AddTrunkGroup.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
       
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
    
                    }
        
        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = ''+common.Domain+''+UrlforAddTrunkGroup +''
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
    
    # Start Test Case No 38-03
    def testcase_03_AddTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Post Method to Add Trunk Group' , 'Add Trunk Group with Empty/Null Trunk Group Name.')
        # Add Node/PBX Function calling
        PBXFunctions=PBXF.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '"+OXEName+"' and OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        PBXID=str(val[0])
        cursor.commit()
        
        # Generate Simple Character String Limit 10 Characters
        Name = ''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
    
                    }
        
        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = ''+common.Domain+''+UrlforAddTrunkGroup +''
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
    
    # Start Test Case No 38-04
    def testcase_04_AddTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Post Method to Add Trunk Group' , 'Add Trunk Group with invalid or Non Existing PBXID.')
        
        PBXID='123456'
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
    
                    }
        
        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = ''+common.Domain+''+UrlforAddTrunkGroup +''
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
    
    # Start Test Case No 38-05
    def testcase_05_AddTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Post Method to Add Trunk Group' , 'Add Trunk Group with Empty/Null PBXID.')
        
        PBXID=''
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
    
                    }
        
        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = ''+common.Domain+''+UrlforAddTrunkGroup +''
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
    
    # Start Test Case No 38-06
    def testcase_06_AddTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Post Method to Add Trunk Group' , 'Add Trunk Group When server role configured as secondary.')
        # Add Node/PBX Function calling
        PBXFunctions=PBXF.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '"+OXEName+"' and OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        PBXID=str(val[0])
        cursor.commit()
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
    
                    }
        
        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = ''+common.Domain+''+UrlforAddTrunkGroup +''
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
    
    # Start Test Case No 38-07
    def testcase_07_AddTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Post Method to Add Trunk Group' , 'Add Trunk Group when server role configured as branch recorder.')
        # Add Node/PBX Function calling
        PBXFunctions=PBXF.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select ID From PBXDetail Where OXEName = '"+OXEName+"' and OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        PBXID=str(val[0])
        cursor.commit()
        
        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)
        
        # Generate Simple Character String Limit 10 Characters
        Name = common.GenrateSimpleStringLimit10()
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
    
                    }
        
        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = ''+common.Domain+''+UrlforAddTrunkGroup +''
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
    
class test_2_UpdateTrunkGroup(TestCase):
    
    # Start Test Case No 38-08
    def testcase_01_UpdateTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Put Method to Update Trunk Group' , 'Update Trunk Group with valid TrunkGroupID.')
        # Add Trunk Group Function calling
        Name, PBXID = test_1_AddTrunkGroup.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
       
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"' and PBXID = '"+PBXID+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        TrunkGroupID=str(val[0])
        cursor.commit()
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Update Trunk Group
        UrlforUpdateTrunkGroup = '/TrunkGroup/Update'
        URL = ''+common.Domain+''+UrlforUpdateTrunkGroup +''
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
    
    # Start Test Case No 38-09
    def testcase_02_UpdateTrunkGroup(self, TestCasesStatus=True):
        
        TestCaseID = '38-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Put Method to Update Trunk Group' , 'Update Trunk Group with invalid/non existing TrunkGroupID.')
        # Add Trunk Group Function calling
        Name, PBXID = test_1_AddTrunkGroup.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
       
        TrunkGroupID='123456'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': ''+Name+'',
                      'PBXID': ''+PBXID+'',
                      'TrunkGroupID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Update Trunk Group
        UrlforUpdateTrunkGroup = '/TrunkGroup/Update'
        URL = ''+common.Domain+''+UrlforUpdateTrunkGroup +''
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
    
class test_3_GetTrunkGroup(TestCase):
    
    # Start Test Case No 38-10
    def testcase_01_GetTrunkGroupdata(self, TestCasesStatus=True):
        
        TestCaseID = '38-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Get Method to Get Trunk Group data' , 'Get all Trunk Group data with valid inputs.')
       
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': '',
                      
                    }
        
        # Url For Get Trunk Group
        UrlforGetTrunkGroup = '/TrunkGroup/Get/'
        URL = ''+common.Domain+''+UrlforGetTrunkGroup +''
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
    
    # Start Test Case No 38-11
    def testcase_02_GetTrunkGroupData(self, TestCasesStatus=True):
        
        TestCaseID = '38-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Get Method Get Trunk Group data' , 'Get as single Trunk Group data with valid ID.')
        # Add Trunk Group Function calling
        Name, PBXID = test_1_AddTrunkGroup.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
       
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"' and PBXID = '"+PBXID+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        ID=str(val[0])
        cursor.commit()
       
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Get Trunk Group
        UrlforGetTrunkGroup = '/TrunkGroup/Get/'
        URL = ''+common.Domain+''+UrlforGetTrunkGroup +''+ID+''
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
    
    # Start Test Case No 38-12
    def testcase_03_GetTrunkGroupData(self, TestCasesStatus=True):
        
        TestCaseID = '38-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Get Method Get Trunk Group data' , 'Get as single Trunk Group data with invalid/non existing ID.')
        
        ID='123456'       
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Get Trunk Group
        UrlforGetTrunkGroup = '/TrunkGroup/Get/'
        URL = ''+common.Domain+''+UrlforGetTrunkGroup +''+ID+''
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
    
class test_4_DeleteTrunkGroup(TestCase):
    
    # Start Test Case No 38-13
    def testcase_01_DeleteTrunkGroupData(self, TestCasesStatus=True):
        
        TestCaseID = '38-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Delete Method Delete Trunk Group data' , 'Delete Trunk Group data with valid ID.')
        # Add Trunk Group Function calling
        Name, PBXID = test_1_AddTrunkGroup.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)
       
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select TrunkGroupID From TrunkGroup Where Name = '"+Name+"' and PBXID = '"+PBXID+"';")
        cursor.execute(SQLCommand)
        val=cursor.fetchone()
        ID=str(val[0])
        cursor.commit()
       
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Delete Trunk Group
        UrlforDeleteTrunkGroup = '/TrunkGroup/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteTrunkGroup +''+ID+''
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
    
    # Start Test Case No 38-14
    def testcase_02_DeleteTrunkGroupData(self, TestCasesStatus=True):
        
        TestCaseID = '38-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Delete Method to Delete Trunk Group data' , 'Delete Trunk Group data with invalid/non existing ID.')
        
        ID='123456'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': ''+ID+'',
    
                    }
        
        # Url For Delete Trunk Group
        UrlforDeleteTrunkGroup = '/TrunkGroup/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteTrunkGroup +''+ID+''
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
    
    
    # Start Test Case No 38-15
    def testcase_03_DeleteTrunkGroupData(self, TestCasesStatus=True):
        
        TestCaseID = '38-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Delete Method Delete Trunk Group data' , 'Delete Trunk Group data with valid ID that is Trunk Group associated with Trunk Packetizer.')
        
        # Add Packetizer Function calling
        PacketizerFunctions= PacketizerFun.test_1_AddPacketizerConfiguration()
        PcktIP,BoardID,TrunkGroupID = PacketizerFunctions.testcase_22_AddPacketizerConfiguration(common.PrereqTestCasesStatusUpdate)
        PcktIP=PcktIP
        BoardID=BoardID
       
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Delete Trunk Group
        UrlforDeleteTrunkGroup = '/TrunkGroup/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteTrunkGroup +''+TrunkGroupID+''
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
    
    
    # Start Test Case No 38-16
    def testcase_04_DeleteTrunkGroupData(self, TestCasesStatus=True):
        
        TestCaseID = '38-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group' , 'Using Delete Method Delete Trunk Group data' , 'Delete Trunk Group data with valid ID that is Trunk Group associated with Equipment Number.')
        
        # Add Equipment Function calling
        EquipmentFunctions= EquipmentFun.test_1_AddEquipment()
        EquipmentNumber, BoardID, TrunkGroupID = EquipmentFunctions.testcase_01_AddEquipment(common.PrereqTestCasesStatusUpdate)
        EquipmentNumber=EquipmentNumber
        BoardID=BoardID
        
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': ''+TrunkGroupID+'',
    
                    }
        
        # Url For Delete Trunk Group
        UrlforDeleteTrunkGroup = '/TrunkGroup/Delete/'
        URL = ''+common.Domain+''+UrlforDeleteTrunkGroup +''+TrunkGroupID+''
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
class test_5_TrunkGroupErrorCodes(TestCase):

    # Start Test Case No 38-25
    def testcase_01_GetTrunkGroupData(self, TestCasesStatus=True):

        TestCaseID = '38-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group', 'Using Get Method Get Trunk Group data',
                      'Get as single Trunk Group data with invalid/non existing ID.')

        ID = '123456'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': '' + ID + '',

                      }

        # Url For Get Trunk Group
        UrlforGetTrunkGroup = '/TrunkGroup/Get/'
        URL = '' + common.Domain + '' + UrlforGetTrunkGroup + '' + ID + ''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400 and resp['InternalErrorCode'] == 'OPRTrunkGroup06':
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




    # Start Test Case No 38-26
    def testcase_02_AddTrunkGroup(self, TestCasesStatus=True):

            TestCaseID = '38-26'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('Trunk Group', 'Using Post Method to Add Trunk Group',
                          'Add Trunk Group with invalid or Non Existing PBXID.')

            PBXID = '123456'
            # Generate Simple Character String Limit 10 Characters
            Name = common.GenrateSimpleStringLimit10()
            # Test Case Start Time
            starttime = time.process_time()
            # Header Parameters of Rest API
            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'Name': '' + Name + '',
                          'PBXID': '' + PBXID + '',

                          }

            # Url For Add Trunk Group
            UrlforAddTrunkGroup = '/TrunkGroup/Add'
            URL = '' + common.Domain + '' + UrlforAddTrunkGroup + ''
            # Hit API Through Methods
            response = requests.post(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp['InternalErrorCode'] == 'OPRTrunkGroup07':
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

    # Start Test Case No 38-27
    def testcase_03_AddTrunkGroup(self, TestCasesStatus=True):

        TestCaseID = '38-27'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group', 'Using Post Method to Add Trunk Group',
                      'Add Trunk Group with Duplicate Trunk name.')
        # Add Trunk Group Function calling
        Name, PBXID = test_1_AddTrunkGroup.testcase_01_AddTrunkGroup(common.PrereqTestCasesStatusUpdate)

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'Name': '' + Name + '',
                      'PBXID': '' + PBXID + '',

                      }

        # Url For Add Trunk Group
        UrlforAddTrunkGroup = '/TrunkGroup/Add'
        URL = '' + common.Domain + '' + UrlforAddTrunkGroup + ''
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 409 and resp['InternalErrorCode'] == 'OPRTrunkGroup08':
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

    # Start Test Case No 38-28
    def testcase_04_DeleteTrunkGroupData(self, TestCasesStatus=True):

            TestCaseID = '38-28'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('Trunk Group', 'Using Delete Method Delete Trunk Group data',
                          'Delete Trunk Group data with valid ID that is Trunk Group associated with Equipment Number.')

            # Add Equipment Function calling
            EquipmentFunctions = EquipmentFun.test_1_AddEquipment()
            EquipmentNumber, BoardID, TrunkGroupID = EquipmentFunctions.testcase_01_AddEquipment(
                common.PrereqTestCasesStatusUpdate)
            EquipmentNumber = EquipmentNumber
            BoardID = BoardID

            # Test Case Start Time
            starttime = time.process_time()
            # Header Parameters of Rest API
            Parameters = {'AuthToken': config.sessionkey,
                          'AuthUser': config.auth_user,
                          'ID': '' + TrunkGroupID + '',

                          }

            # Url For Delete Trunk Group
            UrlforDeleteTrunkGroup = '/TrunkGroup/Delete/'
            URL = '' + common.Domain + '' + UrlforDeleteTrunkGroup + '' + TrunkGroupID + ''
            # Hit API Through Methods
            response = requests.delete(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 409 and resp['InternalErrorCode'] == 'OPRTrunkGroup09' :
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

    # Start Test Case No 38-29
    def testcase_05_DeleteTrunkGroupData(self, TestCasesStatus=True):

        TestCaseID = '38-29'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Trunk Group', 'Using Delete Method Delete Trunk Group data',
                      'Delete Trunk Group data with valid ID that is Trunk Group associated with Trunk Packetizer.')

        # Add Packetizer Function calling
        PacketizerFunctions = PacketizerFun.test_1_AddPacketizerConfiguration()
        PcktIP, BoardID, TrunkGroupID = PacketizerFunctions.testcase_22_AddPacketizerConfiguration(
            common.PrereqTestCasesStatusUpdate)
        PcktIP = PcktIP
        BoardID = BoardID

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'ID': '' + TrunkGroupID + '',

                      }

        # Url For Delete Trunk Group
        UrlforDeleteTrunkGroup = '/TrunkGroup/Delete/'
        URL = '' + common.Domain + '' + UrlforDeleteTrunkGroup + '' + TrunkGroupID + ''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        # Response Code Verification
        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 409 and resp['InternalErrorCode'] == 'OPRTrunkGroup11':
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


    # Start Test Case No 38-30
    def testcase_30_AddTrunkGroup(self, TestCasesStatus=True):

            TestCaseID = '38-30'
            # Calling Common Functions
            common = CF.CommonFunctions()
            common.Header('Trunk Group', 'Using Post Method to Add Trunk Group', 'Add Trunk Group with all valid Data.')
            # Add Node/PBX Function calling
            PBXFunctions = PBXF.test_1_AddPBXConfiguration()
            OXEName, ValidIP = PBXFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)

            # Config DB Connectivity Function calling
            cursor = common.StringDBConnectivity()
            # SQL Queries for Data Verification
            SQLCommand = ("Select ID From PBXDetail Where OXEName = '" + OXEName + "' and OXEIP = '" + ValidIP + "';")
            cursor.execute(SQLCommand)
            val = cursor.fetchone()
            PBXID = str(val[0])
            cursor.commit()

            # Generate Simple Character String Limit 10 Characters
            Name = common.GenrateSimpleStringLimit10()
            # Test Case Start Time
            starttime = time.process_time()
            # Header Parameters of Rest API
            Parameters = {'AuthToken': trunkgUser.sessionkey,
                          'AuthUser': trunkgUser.auth_user,
                          'Name': '' + Name + '',
                          'PBXID': '' + PBXID + '',

                          }

            # Url For Add Trunk Group
            UrlforAddTrunkGroup = '/TrunkGroup/Add'
            URL = '' + common.Domain + '' + UrlforAddTrunkGroup + ''
            # Hit API Through Methods
            response = requests.post(URL, headers=Parameters)
            # API Response in JSon Format
            resp = response.json()
            showcode = str(resp['ResponseCode'])

            # Response Code Verification
            if TestCasesStatus == True:
                try:
                    if resp['ResponseCode'] == 400 and resp['InternalErrorCode'] == 'OPRTrunkGroup02':
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

            return Name, PBXID
    # Test Case End