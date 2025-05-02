'''
Created on Jul 11, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed


----------------pre requisite--------------------------------------
System setting must be configured
Node or Pbx must be added other wise device can not added
packetizer is optional

------------------OutPut----------------------------
This moudle is shown on site Administration as "Extension"
This module will be ada/update/get/Delete the Extension ,
All the Extensions which will be added  will be shown on Extensions page of the site Administration.
All the Extensions which will be Updated  will be shown on Extensions page of the site Administration.
All the Extensions which  will be delete , remove Extensions page of the site Administration.
 '''
 
import time, requests, random
from Settings import CommonFunctions as CF

from unittest import TestCase
from test_Provisioning import test_02_PBXConfiguration as pbxfunctions
from test_Provisioning import test_06_SiteAgentConfiguration as agentfunctions
from test_Provisioning import test_03_PacketizerConfiguration as packetizerfunctions
import test_Provisioning.test_01_SystemSettings as systemsettingsFunctions
from Key import config


SheetName=    '4-Device Configuration'
class test_1_AddDeviceConfiguration(TestCase):
    
    # Start Test Case No 04-01
    def testcase_01_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add device')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP
        
        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))
        
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()
        
        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'
        
        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'
        
                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal, pbxid
        # Test Case End

    # Start Test Case No 04-09
    def testcase_09_Add_SIP_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))


        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        HandsetType='4'
        RecordingInterface = '3'
        Recording_Enabled = 'True'
        ValidMacAdd= common.GenrateValidMac()
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+HandsetType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+ValidMacAdd+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal , pbxid
        # Test Case End

    # Start Test Case No 04-02
    def testcase_02_Add_IPDR_Ext_WithRODEnabled_RFN(self, TestCasesStatus=True):

        TestCaseID = '04-02'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName
        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal, pbxid
        # Test Case End

    # Start Test Case No 04-03
    def testcase_03_Add_IPDR_Ext_WithRODEnabled_REC(self, TestCasesStatus=True):

        TestCaseID = '04-03'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '2'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC':'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-04
    def testcase_04_Add_IPDR_Ext_With_EXT_Type(self, TestCasesStatus=True):

        TestCaseID = '04-04'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-05
    def testcase_05_Add_TDM_Ext_With_no_ROD(self, TestCasesStatus=True):

        TestCaseID = '04-05'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))


        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '1'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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
        return ExtVal,pbxid
        # Test Case End

    # Start Test Case No 04-06
    def testcase_06_Add_TDM_Ext_With_ROD_RFN(self, TestCasesStatus=True):

        TestCaseID = '04-06'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '1'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-07
    def testcase_07_Add_TDM_Ext_With_ROD_REC(self, TestCasesStatus=True):

        TestCaseID = '04-07'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName =OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '1'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '2'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-08
    def testcase_08_Add_IP_Attendant_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-08'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName,ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '2'
        Recording_Enabled = 'True'
        ValidMacAdd= common.GenrateValidMac()
        IsStaticLicense = 'True'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+ValidMacAdd+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0',
                    "DataEnrichmentEnabled":"False"

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal,pbxid
            # Test Case End

    # Start Test Case No 04-20
    def testcase_09_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add duplicate device')
        #Calling methods from testcase 1
        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_02_Add_IPDR_Ext_WithRODEnabled_RFN(common.PrereqTestCasesStatusUpdate)

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        status = 'Failed'
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

    # Start Test Case No 04-21
    def testcase_10_Add_IP_Attendant_Ext_WithInvalidMac(self, TestCasesStatus=True):

        TestCaseID = '04-21'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '2'
        Recording_Enabled = 'True'
        ValidMacAdd= 'a1299999abc9999013c'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+ValidMacAdd+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal,pbxid
            # Test Case End

    # Start Test Case No 04-22
    def testcase_11_Add_IPDR_Ext_WithRecordOnDemandOptionsNull(self, TestCasesStatus=True):

        TestCaseID = '04-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method when RecordOnDemandOptions null/empty')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName
        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = ''
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-23
    def testcase_12_Add_IPDR_Ext_WithRecordingInterface2andStaticLicenseEnabledTrue(self, TestCasesStatus=True):

        TestCaseID = '04-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method with RecordingInterface 2  and StaticLicenseEnabled True')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName
        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '2'
        Recording_Enabled = 'True'
        IsStaticLicense = 'True'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-24
    def testcase_13_Add_IPDR_Ext_withRecordingInterface2andHandsetTypeisnull(self, TestCasesStatus=True):

        TestCaseID = '04-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method with RecordingInterface 2  and HandsetType is null/empty')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName
        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType=''
        RecordingInterface = '2'
        Recording_Enabled = 'True'
        IsStaticLicense = 'True'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-26
    def testcase_26_Add_SIP_Ext_WithInvalidMAC(self, TestCasesStatus=True):

        TestCaseID = '04-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        OXEName = OXEName

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEIP = '"+ValidIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        pbxid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        HandsetType='4'
        RecordingInterface = '3'
        Recording_Enabled = 'True'
        ValidMacAdd= '123:1:12.125.9872:ab'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+HandsetType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+ValidMacAdd+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-27
    def testcase_27_Add_SIP_Ext_WithInvalidPBXID(self, TestCasesStatus=True):

        TestCaseID = '04-27'
        # Calling Common Functions
        common = CF.CommonFunctions()

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        pbxid='1234567'

        # Header Parameters of Rest API
        HandsetType='4'
        RecordingInterface = '3'
        Recording_Enabled = 'True'
        ValidMacAdd= common.GenrateValidMac()
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+HandsetType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+ValidMacAdd+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-28
    def testcase_28_Add_IP_Attendant_Ext_WithInvalidPBXNodeID(self, TestCasesStatus=True):

        TestCaseID = '04-28'
        # Calling Common Functions
        common = CF.CommonFunctions()

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        pbxid='1234567'

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '2'
        Recording_Enabled = 'True'
        ValidMacAdd= common.GenrateValidMac()
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+ValidMacAdd+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-29
    def testcase_29_Add_IPDR_Ext_WithInvalidPBXNodeID(self, TestCasesStatus=True):

        TestCaseID = '04-29'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add device when invalid pbx node id.')

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))
        pbxid='1234567'
        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-30
    def testcase_30_Add_IP_Attendant_Ext_WhenDuplicateMac(self, TestCasesStatus=True):

        TestCaseID = '04-30'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal,pbxid = test_1_AddDeviceConfiguration.testcase_08_Add_IP_Attendant_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        #Generate Random Integers
        NewExtVal= str(random.randint(1000 , 99999 ))
        # Config DB Connectivity Function calling
        cursor  = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select MAC from Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand2)
        Macval=cursor.fetchone()
        ValidMacAdd=str(Macval[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '2'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+NewExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+ValidMacAdd+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        status = 'Failed'
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

    # Start Test Case No 04-31
    def testcase_31_Add_IPDR_Ext_WithInvalidSiteCode(self, TestCasesStatus=True):

        TestCaseID = '04-31'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add device with invalid site code.')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '1234567',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        status = 'Failed'
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

    # Start Test Case No 04-33
    def testcase_33_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-33'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add device when server role configured as secondary.')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()
        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_05_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal, pbxid
        # Test Case End

    # Start Test Case No 04-34
    def testcase_34_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-34'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add device when server role configured as Branch.')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        #System Settings Configuration Functions Calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_09_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal, pbxid
        # Test Case End


    # Start Test Case No 04-35
    def testcase_35_Add_VirtualDevice(self, TestCasesStatus=True):

        TestCaseID = '04-35'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add virtual device', 'Adding virtual Devices with valid data', 'through post method add virtual device when device is an integers.')

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))
        # Header Parameters of Rest API
        RecordingInterface = '7'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': '7',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': '0',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal
        # Test Case End


    # Start Test Case No 04-36
    def testcase_36_Add_VirtualDevice(self, TestCasesStatus=True):

        TestCaseID = '04-36'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add virtual device', 'Adding virtual Devices with valid data', 'through post method add virtual device when device is an proper email address.')

        #Generate Random Integers
        ExtVal= common.GenerateEmail()
        # Header Parameters of Rest API
        RecordingInterface = '7'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': '7',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': '0',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal
        # Test Case End


    # Start Test Case No 04-37
    def testcase_37_Add_VirtualDevice(self, TestCasesStatus=True):

        TestCaseID = '04-37'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add virtual device', 'Adding virtual Devices with invalid data', 'through post method add duplicate virtual device when device is an proper email address.')

        #Generate Random Integers
        ExtVal= test_1_AddDeviceConfiguration.testcase_36_Add_VirtualDevice(self, common.PrereqTestCasesStatusUpdate)
        # Header Parameters of Rest API
        RecordingInterface = '7'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': '7',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': '0',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        status = 'Failed'
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

        return ExtVal
        # Test Case End


    # Start Test Case No 04-38
    def testcase_38_Add_VirtualDevice(self, TestCasesStatus=True):

        TestCaseID = '04-38'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add virtual device', 'Adding virtual Devices with invalid data', 'through post method add virtual device when device is an special characters # and !.')

        # System Settings Function calling
        SystemSettingsFunction = systemsettingsFunctions.test_1_UpdateSystemSettings()
        SystemSettingsFunction.testcase_01_UpdateSystemSettings(common.PrereqTestCasesStatusUpdate)

        #Generate Random Integers
        ExtVal= '12!34#'
        # Header Parameters of Rest API
        RecordingInterface = '7'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': '7',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': '0',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal
        # Test Case End


    # Start Test Case No 04-39
    def testcase_39_Add_TDM_Ext_With_ROD_RFN(self, TestCasesStatus=True):

        TestCaseID = '04-39'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PacketizerFunctions = packetizerfunctions.test_1_AddPacketizerConfiguration()
        PcktIP, PBXID = PacketizerFunctions.testcase_01_AddPacketizerConfiguration(common.PrereqTestCasesStatusUpdate)

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from BlueBox Where IP = '"+PcktIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        Packid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '1'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+PBXID+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': ''+Packid+'',
                    'AllowFailOverEnabled': 'True',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal, PcktIP, PBXID
        # Test Case End


    # Start Test Case No 04-40
    def testcase_40_Add_TDM_Ext_With_ROD_RFN(self, TestCasesStatus=True):

        TestCaseID = '04-40'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PacketizerFunctions = packetizerfunctions.test_1_AddPacketizerConfiguration()
        PcktIP, PBXID = PacketizerFunctions.testcase_01_AddPacketizerConfiguration(common.PrereqTestCasesStatusUpdate)

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from BlueBox Where IP = '"+PcktIP+"';")
        cursor.execute(SQLCommand2)
        pbxid1=cursor.fetchone()
        Packid=str(pbxid1[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '1'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken': config.sessionkeysite,
                    'AuthUser': config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+PBXID+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': ''+Packid+'',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal, PcktIP, PBXID
        # Test Case End


    # Start Test Case No 04-41
    def testcase_41_Add_TDM_Ext_With_ROD_RFN(self, TestCasesStatus=True):

        TestCaseID = '04-41'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Calling PBX Configuration Function
        PacketizerFunctions = packetizerfunctions.test_1_AddPacketizerConfiguration()
        PcktIP, PBXID = PacketizerFunctions.testcase_01_AddPacketizerConfiguration(common.PrereqTestCasesStatusUpdate)
        PcktIP=PcktIP
        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999 ))

        Packid=''

        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '1'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+PBXID+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': ''+Packid+'',
                    'AllowFailOverEnabled': 'True',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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
    # Start Test Case No 04-01
    def testcase_42_Add_CCDAgent_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-42'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding CCD Agent Devices with valid data', 'through post method add device')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='9'
        RecordingInterface = '9'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'1'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal, pbxid

    def testcase_45_Add_CCDAgent_Ext_WithHandsetTypeOtherthan9(self, TestCasesStatus=True):

        TestCaseID = '04-45'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding CCD Agent Devices with invalid data', 'through post method add device')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '9'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'1'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    def testcase_46_Add_CCDAgent_Ext_WithRecordingInterfaceOtherthan9(self, TestCasesStatus=True):

        TestCaseID = '04-46'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding CCD Agent Devices with invalid data', 'through post method add device')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='9'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'1'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-48
    def testcase_48_Add_SIPREC_Ext_WithNoROD_DiableRecording(self, TestCasesStatus=True):

        TestCaseID = '04-48'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding SIPREC Device with valid data', 'through post method add device')
        # Calling PBX Configuration Function

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))



        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '8'
        Recording_Enabled = 'False'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

        return ExtVal

    # Start Test Case No 04-49
    def testcase_49_Add_SIPREC_Ext_WithRFN_EnableRecording(self, TestCasesStatus=True):

        TestCaseID = '04-49'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding SIPREC Device with valid data', 'through post method add device')
        # Calling PBX Configuration Function

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))



        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '8'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-50
    def testcase_50_Add_SIPREC_Ext_WithREC_EnableRecording(self, TestCasesStatus=True):

        TestCaseID = '04-50'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding SIPREC Device with valid data', 'through post method add device')
        # Calling PBX Configuration Function

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))



        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '8'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '2'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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


    def testcase_53_Add_SIPREC_Ext_WithNoROD_EnableRecording(self, TestCasesStatus=True):

        TestCaseID = '04-53'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding SIPREC Device with valid data', 'through post method add device')
        # Calling PBX Configuration Function

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))



        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '8'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    def testcase_54_Add_SIPREC_Ext_WithNoROD_AsAnalogue(self, TestCasesStatus=True):

        TestCaseID = '04-54'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding SIPREC Device with valid data', 'through post method add device')
        # Calling PBX Configuration Function

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))



        # Header Parameters of Rest API
        ExtType='1'
        RecordingInterface = '8'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    def testcase_55_Add_SIPREC_Ext_WithNoROD_AsDigital(self, TestCasesStatus=True):

        TestCaseID = '04-55'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding SIPREC Device with valid data', 'through post method add device')
        # Calling PBX Configuration Function

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))



        # Header Parameters of Rest API
        ExtType='2'
        RecordingInterface = '8'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    def testcase_56_Add_SIPREC_Ext_WithNoROD_AsSIPOnDRLink(self, TestCasesStatus=True):

        TestCaseID = '04-56'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding SIPREC Device with valid data', 'through post method add device')
        # Calling PBX Configuration Function

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))



        # Header Parameters of Rest API
        ExtType='3'
        RecordingInterface = '8'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    def testcase_57_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus=True):

        TestCaseID = '04-57'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'But using sever session key')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP=PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        #Generate Random Integers
        ExtVal= str(random.randint(1000 , 99999  ))

        # Config DB Connectivity Function calling
        cursor  = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '"+OXEName+"';")
        cursor.execute(SQLCommand2)
        vals=cursor.fetchone()
        pbxid=str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType='0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Extension': ''+ExtVal+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingInterface': ''+RecordingInterface+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'Type':'0'

                    }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = ''+common.Domain+''+UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-59
    def testcase_59_Add_IPDR_Ext_With_authkey_server(self, TestCasesStatus=True):

        TestCaseID = '04-59'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add device with server auth key')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP = PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        # Generate Random Integers
        ExtVal = str(random.randint(1000, 99999))

        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '" + OXEName + "';")
        cursor.execute(SQLCommand2)
        vals = cursor.fetchone()
        pbxid = str(vals[0])
        cursor.commit()

        # Header Parameters of Rest API
        ExtType = '0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'Extension': '' + ExtVal + '',
                      'HandsetType': '' + ExtType + '',
                      'RecordingInterface': '' + RecordingInterface + '',
                      'RecordingEnabled': '' + Recording_Enabled + '',
                      'MAC': '',
                      'PBXID': '' + pbxid + '',
                      'StaticLicenseEnabled': '' + IsStaticLicense + '',
                      'RecordOnDemandOptions': '' + ROD + '',
                      'RTPRedirectEnabled': '' + RTP_Redirect + '',
                      'SIPVideoEnabled': '' + Sip_Video_Enabled + '',
                      'Packetizer': '',
                      'AllowFailOverEnabled': 'False',
                      'Type': '0'

                      }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = '' + common.Domain + '' + UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])
        status = 'Failed'
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

        return ExtVal, pbxid
        # Test Case End

    # Start Test Case No 04-60
    def testcase_60_Add_IPDR_Ext_WithInvalidPBX(self, TestCasesStatus=True):

        TestCaseID = '04-60'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add device', 'Adding Devices with valid data', 'through post method add device with invalid PBX')
        # Calling PBX Configuration Function
        PBXConfigurationFunctions = pbxfunctions.test_1_AddPBXConfiguration()

        OXEName, ValidIP = PBXConfigurationFunctions.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
        ValidIP = ValidIP

        # Generate Random Integers
        ExtVal = str(random.randint(1000, 99999))

        # Config DB Connectivity Function calling
        cursor = common.StringDBConnectivity()
        # SQL Queries for Data Verification
        # # SQLCommand2 = ("Select ID from PBXDetail Where OXEName = '" + OXEName + "';")
        # # cursor.execute(SQLCommand2)
        # # vals = cursor.fetchone()
        # pbxid = str(vals[0])
        # cursor.commit()
        pbxid = "12345"

        # Header Parameters of Rest API
        ExtType = '0'
        RecordingInterface = '0'
        Recording_Enabled = 'True'
        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'Extension': '' + ExtVal + '',
                      'HandsetType': '' + ExtType + '',
                      'RecordingInterface': '' + RecordingInterface + '',
                      'RecordingEnabled': '' + Recording_Enabled + '',
                      'MAC': '',
                      'PBXID': '' + pbxid + '',
                      'StaticLicenseEnabled': '' + IsStaticLicense + '',
                      'RecordOnDemandOptions': '' + ROD + '',
                      'RTPRedirectEnabled': '' + RTP_Redirect + '',
                      'SIPVideoEnabled': '' + Sip_Video_Enabled + '',
                      'Packetizer': '',
                      'AllowFailOverEnabled': 'False',
                      'Type': '0'

                      }
        # Url For Add Device
        UrlForAddingDevice = '/Device/Add'
        URL = '' + common.Domain + '' + UrlForAddingDevice
        # Hit API Through Methods
        response = requests.post(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])
        status = 'Failed'
        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False

        return ExtVal, pbxid
        # Test Case End

class test_2_GetDeviceConfiguration(TestCase):

    # Start Test Case No 04-12
    def testcase_01_Get_All_Ext(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '04-12'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user
                    }
        # Url For Get Device
        UrlForGettingDevice = '/Device/Get'

        URL = ''+common.Domain+''+UrlForGettingDevice
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-15
    def testcase_02_Get_Ext_By_Invalid_ID(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '04-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        InvalidId = '12345'
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'Id': ''+InvalidId+''
                    }
        # Url For Get Device
        UrlForGettingDevice = '/Device/Get/'

        URL = ''+common.Domain+''+UrlForGettingDevice+''+InvalidId+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])

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


    # Start Test Case No 04-13
    def testcase_03_Get_Ext_byId(self, TestCasesStatus=True):

        TestCaseID = '04-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user
                    }
        # Url For Get Device
        UrlForGettingDevice = '/Device/Get/'

        URL = ''+common.Domain+''+UrlForGettingDevice+''+DevID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-14
    def testcase_04_Get_Ext_by_Ext_Value(self, TestCasesStatus=True):

        TestCaseID = '04-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus)
        pbxid=pbxid

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    }
        # Url For Get Device
        UrlForGettingDevice = '/Device/Get/'

        URL = ''+common.Domain+''+UrlForGettingDevice+'?Extension='+ExtVal+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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
    def testcase_44_GetCCD_Ext_byId(self, TestCasesStatus=True):

        TestCaseID = '04-44'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_42_Add_CCDAgent_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        pbxid=pbxid
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user
                    }
        # Url For Get Device
        UrlForGettingDevice = '/Device/Get/'

        URL = ''+common.Domain+''+UrlForGettingDevice+''+DevID+''
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    def testcase_58_Get_All_Ext(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '04-58'
        # Calling Common Functions
        common = CF.CommonFunctions()

        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkey,
                    'AuthUser':config.auth_user
                    }
        # Url For Get Device
        UrlForGettingDevice = '/Device/Get'

        URL = ''+common.Domain+''+UrlForGettingDevice
        # Hit API Through Methods
        response = requests.get(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

class test_3_DeleteDeviceConfiguration(TestCase):

    # Start Test Case No 04-11
    def testcase_01_Delete_Ext_byId(self, TestCasesStatus=True):

        TestCaseID = '04-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus)
        pbxid=pbxid
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user
                    }
        # Url For Delete Device
        UrlForGettingDevice = '/Device/Delete/'

        URL = ''+common.Domain+''+UrlForGettingDevice+''+DevID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-16
    def testcase_02_Delete_Ext_byInvalidId(self, TestCasesStatus=True):

        # Test Case Start Time
        starttime = time.process_time()
        TestCaseID = '04-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        #Extension=test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus)
        InvalidId = '12345'

        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user
                    }
        # Url For Delete Device
        UrlForGettingDevice = '/Device/Delete/'

        URL = ''+common.Domain+''+UrlForGettingDevice+''+InvalidId+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-32
    def testcase_03_Delete_Ext_ThatAssosiatedToAgent(self, TestCasesStatus=True):

        TestCaseID = '04-32'
        # Calling Common Functions
        common = CF.CommonFunctions()
        AgentFunctions = agentfunctions.test_1_AddSiteAgentConfigurations()
        username,teamname,ExtVal,pbxid=AgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username=username
        teamname=teamname
        pbxid=pbxid
        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user
                    }
        # Url For Delete Device
        UrlForGettingDevice = '/Device/Delete/'

        URL = ''+common.Domain+''+UrlForGettingDevice+''+DevID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
        status = 'Failed'
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

    # Start Test Case No 04-11
    def testcase_04_Delete_SIPRECExt_byId(self, TestCasesStatus=True):

        TestCaseID = '04-51'
        # Calling Common Functions
        common = CF.CommonFunctions()
        ExtVal=test_1_AddDeviceConfiguration.testcase_48_Add_SIPREC_Ext_WithNoROD_DiableRecording(self, TestCasesStatus)

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user
                    }
        # Url For Delete Device
        UrlForGettingDevice = '/Device/Delete/'

        URL = ''+common.Domain+''+UrlForGettingDevice+''+DevID+''
        # Hit API Through Methods
        response = requests.delete(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

class test_4_UpdateDeviceConfiguration(TestCase):

    # Start Test Case No 04-10
    def testcase_01_Update_Ext_IPDR_License(self, TestCasesStatus=True): #assigning static license to an IPDR extension

        TestCaseID = '04-10'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus)

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        ExtType='0'

        Recording_Enabled = 'True'

        IsStaticLicense = 'True'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'AllowFailOverLoggerEnabled' : 'False',
                    'Logger' : ''

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
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

    # Start Test Case No 04-17
    def testcase_02_Update_Ext_IPDR_ROD(self, TestCasesStatus=True): #assigning static license to an IPDR extension

        TestCaseID = '04-17'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        ExtType='0'

        Recording_Enabled = 'True'

        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'AllowFailOverLoggerEnabled': 'False',
                      'Logger': ''

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-18
    def testcase_03_Update_Ext_TDM_HandSetType(self, TestCasesStatus=True): # changing the extension type of TDM Ext

        TestCaseID = '04-18'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal,pbxid=test_1_AddDeviceConfiguration.testcase_05_Add_TDM_Ext_With_no_ROD(self, TestCasesStatus)

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        ExtType='1'

        Recording_Enabled = 'True'

        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                      'AllowFailOverLoggerEnabled': 'False',
                      'Logger': ''

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-19
    def testcase_04_Update_Ext_SIP_Enable_Video(self, TestCasesStatus=True): # enabling the extension video on SIP

        TestCaseID = '04-19'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal , pbxid =test_1_AddDeviceConfiguration.testcase_09_Add_SIP_Ext_WithNoROD(self, TestCasesStatus)

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()
        SQLCommand = ("Select MAC From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        MAC=str(vals[0])
        cursor.commit()

        ExtType='4'

        Recording_Enabled = 'True'

        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'True'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': ''+MAC+'',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'AllowFailOverLoggerEnabled': 'False',
                    'Logger': ''

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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

    # Start Test Case No 04-25
    def testcase_05_Update_Ext_IPDR_License(self, TestCasesStatus=True): #assigning static license to an IPDR extension

        TestCaseID = '04-25'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(self, TestCasesStatus)
        ExtVal=ExtVal
        DevID='12345'

        ExtType='0'

        Recording_Enabled = 'True'

        IsStaticLicense = 'True'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False'

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
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

        # Start Test Case No 04-43
    def testcase_43_Update_CCD_Agent_DisableRecording(self, TestCasesStatus=True): #assigning static license to an IPDR extension

        TestCaseID = '04-43'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_42_Add_CCDAgent_Ext_WithNoROD(self, TestCasesStatus)
        ExtVal=ExtVal

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()


        ExtType='9'

        Recording_Enabled = 'False'

        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                    'AllowFailOverLoggerEnabled': 'False',
                      'Logger': ''

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
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

    def testcase_47_Update_CCD_Agent_WithExtTypeOtherthan9(self, TestCasesStatus=True): #assigning static license to an IPDR extension

        TestCaseID = '04-47'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal, pbxid=test_1_AddDeviceConfiguration.testcase_42_Add_CCDAgent_Ext_WithNoROD(self, TestCasesStatus)
        ExtVal=ExtVal

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()


        ExtType='0'

        Recording_Enabled = 'False'

        IsStaticLicense = 'False'
        ROD = '0'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': ''+pbxid+'',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False'

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
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

        # Start Test Case No 04-61

    def testcase_61_Update_Ext_IPDR_ROD_withInvalid_ExtType(self, TestCasesStatus=True):  # assigning static license to an IPDR extension

        TestCaseID = '04-61'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal, pbxid = test_1_AddDeviceConfiguration.testcase_01_Add_IPDR_Ext_WithNoROD(
            common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '" + ExtVal + "';")
        cursor.execute(SQLCommand)
        vals = cursor.fetchone()
        DevID = str(vals[0])
        cursor.commit()

        ExtType = 'abc'

        Recording_Enabled = 'True'

        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': '',
                      'Id': '' + DevID + '',
                      'HandsetType': '' + ExtType + '',
                      'RecordingEnabled': '' + Recording_Enabled + '',
                      'MAC': '',
                      'PBXID': '' + pbxid + '',
                      'StaticLicenseEnabled': '' + IsStaticLicense + '',
                      'RecordOnDemandOptions': '' + ROD + '',
                      'RTPRedirectEnabled': '' + RTP_Redirect + '',
                      'SIPVideoEnabled': '' + Sip_Video_Enabled + '',
                      'Packetizer': '',
                      'AllowFailOverEnabled': 'False'

                      }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = '' + common.Domain + '' + UrlForUpdatingDevice
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp = response.json()
        # showcode = str(resp['ResponseCode'])
        status = 'Failed'

        # Response Code Verification
        if TestCasesStatus == True:
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
            TestCasesStatus = False
            # Test Case End




    # Start Test Case No 04-52
    def testcase_52_Update_Ext_SIPREC_ROD(self, TestCasesStatus=True): #assigning static license to an IPDR extension

        TestCaseID = '04-52'
        # Calling Common Functions
        common = CF.CommonFunctions()

        ExtVal=test_1_AddDeviceConfiguration.testcase_48_Add_SIPREC_Ext_WithNoROD_DiableRecording(common.PrereqTestCasesStatusUpdate)

        # Config DB Connectivity Function calling
        cursor = common.DBConnectivity()
        # SQL Queries for Data Verification
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+ExtVal+"';")
        cursor.execute(SQLCommand)
        vals=cursor.fetchone()
        DevID=str(vals[0])
        cursor.commit()

        ExtType='0'

        Recording_Enabled = 'True'

        IsStaticLicense = 'False'
        ROD = '1'
        RTP_Redirect = 'False'
        Sip_Video_Enabled = 'False'

        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysite,
                    'AuthUser':config.auth_user,
                    'SiteCode': '',
                    'Id' :''+DevID+'',
                    'HandsetType': ''+ExtType+'',
                    'RecordingEnabled': ''+Recording_Enabled+'',
                    'MAC': '',
                    'PBXID': '',
                    'StaticLicenseEnabled': ''+IsStaticLicense+'',
                    'RecordOnDemandOptions': ''+ROD+'',
                    'RTPRedirectEnabled': ''+RTP_Redirect+'',
                    'SIPVideoEnabled': ''+Sip_Video_Enabled+'',
                    'Packetizer': '',
                    'AllowFailOverEnabled': 'False',
                      'AllowFailOverLoggerEnabled': 'False',
                      'Logger': ''

                    }
        # Url For Update Device
        UrlForUpdatingDevice = '/Device/Update'
        URL = ''+common.Domain+''+UrlForUpdatingDevice
        # Hit API Through Methods
        response = requests.put(URL, headers=Parameters)
        # API Response in JSon Format
        resp=response.json()
        #showcode = str(resp['ResponseCode'])
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


