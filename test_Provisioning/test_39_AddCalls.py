'''
Created on Aug 3, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed
'''

import time, requests, random
from Settings import CommonFunctions as CF
from openpyxl import load_workbook
from unittest import TestCase
from test_Provisioning import test_04_DeviceConfigurations, test_06_SiteAgentConfiguration
import openpyxl.styles.alignment as XLStyle
from openpyxl.styles import PatternFill
from Key import config
SheetName=	'39-Calls'

class test_1_AddCalls(TestCase):

    # Start Test Case No 39-01
    def testcase_01_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-01'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'add call when Call Direction is All/0.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        PBXID=pbxid
        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080315304020'
        CallDuration='50'
        CallDirection='0'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
        # AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=''
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=PBXID
        RecordingInterface='0'
        CallStatus='5'
        PacketizerIP=''
        Channel='2'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      # 'PacketizerIP': ''+PacketizerIP+'',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-02
    def testcase_02_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-02'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and  Call Direction is Inbound Calls/1.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = (
                    "INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('" + TeamName + "','" + TeamDesc + "',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         # AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='3'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser': config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                       'VideoCall': 'False'
                      # 'PacketizerIP': ''+PacketizerIP+'',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device
            # Test Case End

    # Start Test Case No 39-03
    def testcase_03_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-03'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is DRLink/1 and  Call Direction is Inbound Calls/1..')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_05_Add_TDM_Ext_With_no_ROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Co,nectivity Function calling
        cursor1  = common.DBConnectivity()
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         # AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='1'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel='15'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      # 'PacketizerIP': ''+PacketizerIP+'',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-04
    def testcase_04_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-04'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Attendent/2 and  Call Direction is Inbound Calls/1.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_08_Add_IP_Attendant_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         # AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='2'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      # 'PacketizerIP': ''+PacketizerIP+'',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-05
    def testcase_05_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-05'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is SIP/3 and  Call Direction is Inbound Calls/1.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_09_Add_SIP_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         # AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='3'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken': config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'

                      # 'PacketizerIP': ''+PacketizerIP+'',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-06
    def testcase_06_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-06'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         # AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      # 'PacketizerIP': ''+PacketizerIP+'',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-07
    def testcase_07_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-07'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is SIP Trunk/5 and  Call Direction is Inbound Calls/1.')

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()


        DeviceNo='SIPTrunk'
        devid='2'
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID='2'
        RecordingInterface='5'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      # 'PacketizerIP': ''+PacketizerIP+'',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-08
    def testcase_08_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-08'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is All/6 and  Call Direction is Inbound Calls/1.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)
        # This section is just to add for Agent/User to get User ID that is used in Add Calls parameters.
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand5)
        value=cursor1.fetchone()
        devid=str(value[0])
        cursor1.commit()
        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='1212'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'


                      # 'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-09
    def testcase_09_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-09'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and  Call Direction is OutBound Calls/2.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to add for Agent/User to get User ID that is used in Add Calls parameters.
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand5)
        value=cursor1.fetchone()
        devid=str(value[0])
        cursor1.commit()

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='2'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel='24'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-10
    def testcase_10_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-10'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is DRLink/1 and  Call Direction is OutBound Calls/2.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_05_Add_TDM_Ext_With_no_ROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to add for Agent/User to get User ID that is used in Add Calls parameters.
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand5)
        value=cursor1.fetchone()
        devid=str(value[0])
        cursor1.commit()
        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='2'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='1'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel='29'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-11
    def testcase_11_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-11'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Attendent/2 and  Call Direction is OutBound Calls/2.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_08_Add_IP_Attendant_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to add for Agent/User to get User ID that is used in Add Calls parameters.
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand5)
        value=cursor1.fetchone()
        devid=str(value[0])
        cursor1.commit()

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='2'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='2'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-12
    def testcase_12_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-12'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is SIP/3 and  Call Direction is OutBound Calls/2.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_09_Add_SIP_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to add for Agent/User to get User ID that is used in Add Calls parameters.
        SQLCommand5 = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand5)
        value=cursor1.fetchone()
        devid=str(value[0])
        cursor1.commit()
        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='2'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='3'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-13
    def testcase_13_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-13'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is OutBound Calls/2.')

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()

        DeviceNo='Trunk'
        devid='1'

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)
        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='2'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-14
    def testcase_14_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-14'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is SIP Trunk/5 and  Call Direction is OutBound Calls/2.')



        DeviceNo='SIPTrunk'
        devid='2'
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='2'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID='2'
        RecordingInterface='5'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-15
    def testcase_15_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-15'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Null/Empty.')

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()


        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)
        SQLCommand4 = ("Select Groupid from Groups Where Name = '"+TeamName+"';")
        cursor1.execute(SQLCommand4)
        vals = cursor1.fetchone()
        TeamID = str(vals[0])
        cursor1.commit()

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)


        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)
        # Header Parameters Values
        Device='Trunk'
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface=''
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-16
    def testcase_16_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-16'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But Device value is NULL/Empty.')

        DeviceNo=''
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-17
    def testcase_17_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-17'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But Audio file path value is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
        AudioFilePath=''
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-18
    def testcase_18_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-18'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But GlobalCallID value is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)
        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=''
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-19
    def ztestcase_19_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-19'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But CorrelatorID is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)
        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=''
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-20
    def testcase_20_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-20'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But PBXCallID value is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)
        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=''
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-21
    def testcase_21_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-21'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But invalid Call Date value.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)
        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='00999999081530402012345'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-22
    def testcase_22_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-22'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But invalid Call Duration.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='abc1.29999c'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-23
    def testcase_23_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-23'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But CalledBy value is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)
        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=''
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-24
    def testcase_24_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-24'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But Call Status value is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus=''
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-25
    def testcase_25_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-25'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But PacketizerIP value is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
        AudioFilePath=''
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
        PacketizerIP=''
        Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-26
    def testcase_26_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-26'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But Channel value is NULL/Empty.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel=''
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

    # Start Test Case No 39-27
    def testcase_27_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-27'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and  Call Direction is Inbound Calls/1 and CallStatus is 6.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='6'
        # PacketizerIP=PcktIP
        # Channel='21'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device
            # Test Case End

    # Start Test Case No 39-28
    def testcase_28_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-28'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and  Call Direction is Inbound Calls/1 and CallStatus is 15.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='15'
        # PacketizerIP=PcktIP
        # Channel='18'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device
            # Test Case End

    # Start Test Case No 39-29
    def testcase_29_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-29'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and  Call Direction is Inbound Calls/1 and CallStatus is 19.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='19'
        # PacketizerIP=PcktIP
        # Channel='9'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device
            # Test Case End


    # Start Test Case No 39-30
    def testcase_30_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-30'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But Device value is invalid non existing.')

        DeviceNo='123456'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID='2'
        RecordingInterface='1'
        CallStatus='5'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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
            # Test Case Eend


    # Start Test Case No 39-31
    def testcase_31_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-31'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and CalledBy is "Unknown".')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy='Unknown'
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='27'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device


    # Start Test Case No 39-32
    def testcase_32_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-32'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and CalledTo is "Unknown".')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo="Unknown"
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='13'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'

#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device


    # Start Test Case No 39-33
    def testcase_33_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-33'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and CalledTo is Apostrophe.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo="Unknow'n"
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='19'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device


    # Start Test Case No 39-34
    def testcase_34_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-34'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and CalledBy is Apostrophe.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy="Unknow'n"
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='16'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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

        return GlobalCallID, CorrelatorID, PBXCallID, Device


    # Start Test Case No 39-35
    def testcase_35_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-35'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and GlobalCallID more then 50 characters.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=common.GenrateDesc250()
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='26'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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


    # Start Test Case No 39-36
    def testcase_36_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-36'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and CorrelatorID more then 50 characters.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=common.GenrateDesc250()
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='7'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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


    # Start Test Case No 39-37
    def testcase_37_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-37'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and PBXCallID more then 50 characters.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=common.GenrateDesc250()
        PBXID=pbxid
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='28'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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


    # Start Test Case No 39-38
    def testcase_38_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-38'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is IPDR/0 and PBXID invalid or non existing.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo,pbxid=device.testcase_01_Add_IPDR_Ext_WithNoROD(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        time.sleep(3)
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # crystal = str(random.randint(10 , 99))
        # coupler = str(random.randint(10 , 99))
        # port= str(random.randint(9000 , 9999))
        # Parameters = {'AuthToken':config.sessionkeysiteUser,
        #               'AuthUser':config.auth_user,
        #               'RecorderType': '0',
        #               'PBXID': ''+pbxid+'',
        #               'Crystal': ''+crystal+'',
        #               'Coupler': ''+coupler+'',
        #               'IPAddress': ''+PcktIP+'',
        #               'Port': ''+port+'',
        #               'BranchID': '',
        #
        #             }
        # # Url for Add Packetizer
        # UrlForAddPacketizer = '/Packetizer/Add/'
        # URL = ''+common.Domain+''+UrlForAddPacketizer+''
        # requests.post(URL, headers=Parameters)
        # time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=common.GenrateDesc250()
        PBXID='123456'
        RecordingInterface='0'
        CallStatus='1'
        # PacketizerIP=PcktIP
        # Channel='4'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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


    # Start Test Case No 39-39
    def testcase_39_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-39'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But Call Status value is invalid or non existing.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='12345'
#         PacketizerIP=PcktIP
#         Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      #                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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


    # Start Test Case No 39-40
    def testcase_40_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-40'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But PacketizerIP value is invalid format.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
        AudioFilePath=''
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
        # PacketizerIP='abc123abc123'
        # Channel=str(random.randint(1 , 23))
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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


    # Start Test Case No 39-41
    def testcase_41_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-41'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Trunk/4 and  Call Direction is Inbound Calls/1 But Channel value is invalid or non existing.')

        DeviceNo='Trunk'
        devid='1'

        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # # Adding Packetizer in system
        # PcktIP=common.GenrateValidIPString()
        # port= str(random.randint(9000 , 9999))
        # cursor1  = common.StringDBConnectivity()
        # SQLCommand5 = ("INSERT INTO BlueBox (IP,Port,CreatedBy,IsTrunk) VALUES ('"+PcktIP+"','"+port+"',1,1);;")
        # cursor1.execute(SQLCommand5)
        # cursor1.commit()
        # time.sleep(3)

        # Header Parameters Values
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
#         AudioFilePath='Dummy Path'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        PBXID=''
        RecordingInterface='4'
        CallStatus='5'
        # PacketizerIP=PcktIP
        # Channel='12345'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+DeviceNo+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': ''+PBXID+'',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
#                       'PacketizerIP': ''+PacketizerIP+'',
#                       'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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


    # Start Test Case No 39-42
    def testcase_42_AddCalls(self, TestCasesStatus=True):

        TestCaseID = '39-42'
        # Calling Common Functions
        common = CF.CommonFunctions()
        common.Header('Add Calls' , 'Using Post Method Add Calls' , 'Add Calls when RecordingInterface is Virtual/7 and  Call Direction is Inbound Calls/1.')

        # Devices/Extension Function Calling
        device=test_04_DeviceConfigurations.test_1_AddDeviceConfiguration()
        DeviceNo=device.testcase_35_Add_VirtualDevice(common.PrereqTestCasesStatusUpdate)
        # Tenant DB Connectivity Function calling
        cursor1  = common.DBConnectivity()
        SQLCommand = ("Select DeviceId From Devices Where Extension = '"+DeviceNo+"';")
        cursor1.execute(SQLCommand)
        deviceid=cursor1.fetchone()
        devid=str(deviceid[0])
        cursor1.commit()

        # This section is just to Add for Team to use the Team ID in Add Agent Section
        TeamName = common.GenrateSimpleStringLimit10()
        TeamDesc = common.GenrateSimpleStringLimit10()
        SQLCommand1 = ("INSERT INTO Groups (Name,Description,CreatedBy) VALUES ('"+TeamName+"','"+TeamDesc+"',1 );")
        cursor1.execute(SQLCommand1)
        cursor1.commit()
        time.sleep(3)

        # This section is just to Add for Agent/User to use the agent User Name
        SiteAgentFunctions = test_06_SiteAgentConfiguration.test_1_AddSiteAgentConfigurations()
        username, teamname, ExtVal, pbxid = SiteAgentFunctions.testcase_01_AddAgent(common.PrereqTestCasesStatusUpdate)
        username = username

        # Now, username contains the correct string value
        SQLCommand = ("Select UserId from Users where Username = '" + username + "';")
        cursor1.execute(SQLCommand)
        vals = cursor1.fetchone()
        UserId = str(vals[0])
        cursor1.commit()
        time.sleep(3)

        cursor1.execute("INSERT INTO UserDevices (UserId,DeviceId) VALUES ('" + UserId + "','" + devid + "')")
        cursor1.commit()
        time.sleep(3)

        # Header Parameters Values
        Device=str(DeviceNo)
        CallsDate='2018080815304020'
        CallDuration='50'
        CallDirection='1'
        # Generate Simple Character String Limit 10 Characters
        CalledBy=str(random.randint(90 , 9999))
        # Generate Simple Character String Limit 10 Characters
        CalledTo=str(random.randint(90 , 9999))
        # AudioFilePath='E:\Automation\Automation\RESTAPI\conv_S_RIVIER_07-06-2022_11_00_15.mp4'
        # Generate Simple Character String Limit 10 Characters
        GlobalCallID=str(random.randint(90 , 9999))
        UserID=UserId
        # Generate Simple Character String Limit 10 Characters
        CorrelatorID=str(random.randint(90 , 9999))
        AgentHangup='False'
        # Generate Simple Character String Limit 10 Characters
        PBXCallID=str(random.randint(90 , 9999))
        RecordingInterface='7'
        CallStatus='5'
        # Channel='-1'
        # Test Case Start Time
        starttime = time.process_time()
        # Header Parameters of Rest API
        Parameters = {'AuthToken':config.sessionkeysiteUser,
                      'AuthUser':config.auth_user,
                      'SiteCode':'',
                      'Device': ''+Device+'',
                      'CallsDate': ''+CallsDate+'',
                      'CallDuration': ''+CallDuration+'',
                      'CallDirection': ''+CallDirection+'',
                      'CalledBy': ''+CalledBy+'',
                      'CalledTo': ''+CalledTo+'',
                      'AudioFilePath': config.audio_file_path,
                      'GlobalCallID': ''+GlobalCallID+'',
                      'UserID': ''+UserID+'',
                      'CorrelatorID': ''+CorrelatorID+'',
                      'AgentHangup': ''+AgentHangup+'',
                      'PBXCallID': ''+PBXCallID+'',
                      'PBXID': '',
                      'RecordingInterface': ''+RecordingInterface+'',
                      'CallStatus': ''+CallStatus+'',
                      'VideoCall': 'False'
                      # 'PacketizerIP': '',
                      # 'Channel': ''+Channel+'',

                    }

        # Url For Add Calls
        UrlForAddCalls='/Calls/Add'
        URL = ''+common.Domain+''+UrlForAddCalls+''
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
        return GlobalCallID, CorrelatorID, PBXCallID, Device
            # Test Case End