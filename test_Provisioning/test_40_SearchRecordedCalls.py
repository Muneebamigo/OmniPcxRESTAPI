'''
Created on Aug 2, 2018

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
from test_Provisioning import test_05_TeamConfigurations
from Key import config

SheetName=	'40-Search Recorded calls'
class test_1_Search_RecordedCalls(TestCase):
    
    UrlForGetRecorderCalls = '/Calls/Search'
    
    def testcase_01_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-01'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes':'19'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_02_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-02'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with CallDateSearchCriteria 7.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"7",
                      'StartDate':"18-07-2018 00:00:00",
                      'EndDate':"20-07-2020 00:00:00",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_03_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-03'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with CallDateSearchCriteria 7 and invalid/null date.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"7",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '8'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_04_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-04'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with CallDateSearchCriteria 6.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"6",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"9",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '8'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_05_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-05'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with CallDateSearchCriteria 6 and invalid/null ParamNumberOfDays.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"6",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '8'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_06_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-06'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with CallDurationCriteria 4.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"0",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"0.5-1",
                      'CallDurationCriteria':"4",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '8'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_07_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-07'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with CallDurationCriteria 4 and CallDuration is null.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"0",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"4",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '8'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_08_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-08'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with PrimaryPBXIPCriteria = 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"5",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"3",
                      'PrimaryPBXIP':"172.20.1.214",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '8'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_09_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-09'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with PrimaryPBXIPCriteria = 2 and PrimaryPBXIP null.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"5",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"2",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_10_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-10'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'ServerRoleCriteria is 2 and server role 0 .')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"5",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"2",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
                
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_11_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-11'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'ServerRoleCriteria is 2 and server role null .')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"5",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"2",    
                      'ServerID':"",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    def testcase_12_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-12'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when  EncryptedCallsCriteria is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'0',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_13_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-13'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when  EncryptedCallsCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'1',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_14_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-14'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when  GroupSearchOption is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'0',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'1',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_15_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-15'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when  GroupSearchOption is 1.')
        # Add Teams Function calling
        teamfunction=test_05_TeamConfigurations.Test_1_AddTeamCofiguration()
        TeamName=teamfunction.test_01_AddTeam(common.PrereqTestCasesStatusUpdate)
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':''+TeamName+'',
                      'GroupSearchOption':'1',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'1',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'1',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    
    def testcase_16_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-16'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when  AssociateAgentCriteria is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'1',
                      'AssociatedAgentCriteria':'0',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_17_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-17'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when  AssociateAgentCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'1',
                      'AssociatedAgentCriteria':'1',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_18_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-18'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDateSearchCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'1',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    
    def testcase_19_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-19'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDateSearchCriteria is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'2',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_20_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-20'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDateSearchCriteria is 3.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'3',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_21_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-21'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallTypeSearchCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"1",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_22_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-22'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallTypeSearchCriteria is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"2",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    
    def testcase_23_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-23'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when DeviceHangUpCriteria is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"0",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_24_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-24'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when DeviceHangUpCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"1",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_25_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-25'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDirectionCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'1',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
     
    def testcase_26_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-26'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDirectionCriteria is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'2',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_27_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-27'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDirectionCriteria is invalid input.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'2231',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_28_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-28'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDurationCriteria is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"50",
                      'CallDurationCriteria':'0',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
             
             
    def testcase_29_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-29'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when CallDurationCriteria is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"50",
                      'CallDurationCriteria':'2',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
             
            
    def testcase_30_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-30'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ScreenCaptureCallsCriteria is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"0",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
     
    def testcase_31_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-31'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ScreenCaptureCallsCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"1",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
      
    def testcase_32_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-32'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ArchivedCallsCriteria is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'0',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
    
    
    def testcase_33_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-33'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ArchivedCallsCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'1',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
    
    
    def testcase_34_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-34'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ArchivedCallsCriteria is invalid.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'22350',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_35_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-35'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when RecordingInterface is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"0",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
     
    def testcase_36_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-36'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when RecordingInterface is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"1",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_37_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-37'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when RecordingInterface is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"2",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
     
    def testcase_38_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-38'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when RecordingInterface is 3.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"3",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
     
    def testcase_39_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-39'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when RecordingInterface is 4.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"4",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
     
    def testcase_40_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-40'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when RecordingInterface is 5.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"5",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
     
    def testcase_41_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-41'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ServerRole is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"1",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
    
    
    def testcase_42_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-42'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ServerRole is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"2",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
    
        
    def testcase_43_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-43'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when DeviceSearchCriteria is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"1212",
                      'DeviceSearchCriteria':"0",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
        
           
    def testcase_44_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-44'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when DeviceSearchCriteria is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"2131",
                      'DeviceSearchCriteria':"2",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
        
    
    def testcase_45_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-45'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when DeviceSearchCriteria is 3.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"1212",
                      'DeviceSearchCriteria':"3",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
        
    def testcase_46_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-46'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when SortDirection is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"1",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_48_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-48'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when ScoredCallOption is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"1",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_47_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-47'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when  ScoredCallOption is 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"0",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_49_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-49'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when RegionValue is 13.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'13',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
     
    def testcase_50_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-50'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with PrimaryPBXIPCriteria = 0.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"",     
                      'FirstNameCriteria':"8",
                      'LastName':"",
                      'LastNameCriteria':"8",
                      'GroupName':"",
                      'GroupSearchOption':"2",
                      'CalledBy':"",
                      'CalledByCriteria':"8",
                      'CalledTo':"",
                      'CalledToCriteria':"8",
                      'EncryptedCallsCriteria':"2",
                      'AssociatedAgentCriteria':"2",
                      'CallDateSearchCriteria':"5",
                      'StartDate':"",
                      'EndDate':"",
                      'ParamNumberOfDays':"",
                      'CallDuration':"",
                      'CallDurationCriteria':"3",
                      'CallDirectionCriteria':"0",
                      'ArchivedCallsCriteria':"2",
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':"5",
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"0",
                      'PrimaryPBXIP':"172.20.1.214",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"0",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"true",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"8",    
                      'ServerID':"0",    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'',
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False  
      
    def testcase_51_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-51'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when SpeechAnalyticsCriteria is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'1',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False   
     
    def testcase_52_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-52'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when SpeechAnalyticsCriteria is 2.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'2',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_53_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-53'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when SpeechAnalyticsCriteria is 3.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'3',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_54_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-54'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when SpeechAnalyticsCriteria is 4.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'4',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_55_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-55'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with SpeechAnalyticsCriteria value is invalid/non existing.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'123456',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_56_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-56'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls with SpeechAnalyticsCriteria value is Null/Empty.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_57_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-57'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when callstatus is 1.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'1',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_58_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-58'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls  when callstatus is 6.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'6',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
        else:
            TestCasesStatus=False
            
    def testcase_59_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-59'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when callstatus is 15.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'15',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
    def testcase_60_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-60'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when callstatus is 60.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',     
                      'FirstNameCriteria':'8',
                      'LastName':'',
                      'LastNameCriteria':'8',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'19',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",
                      'CustomField2_Value':"",
                      'CustomField2_Criteria':"8",
                      'CustomField3_Value':"",
                      'CustomField3_Criteria':"8",
                      'CustomField4_Value':"",
                      'CustomField4_Criteria':"8",
                      'CustomField5_Value':"",
                      'CustomField5_Criteria':"8",
                      'CustomField6_Value':"",
                      'CustomField6_Criteria':"8",
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",
                      'CustomField10_Value':"",
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
    
    
    def testcase_61_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-61'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls by enter First Name and last name single quote and TextSearchCriteria 3 Text is exactly..')
               
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':"'",
                      'FirstNameCriteria':'3',
                      'LastName':"'",
                      'LastNameCriteria':'3',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
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
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False
            
            
    def testcase_62_Search_RecordedCalls(self, TestCasesStatus=True):
        
        starttime = time.process_time()
        TestCaseID = '40-62'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call' , 'Using Get Method to Search Recorded Call' , 'Get Recorded calls when empyt first name last name.')
        
        Parameters = {'AuthToken':config.sessionkeysite,
                      'AuthUser':config.auth_user,
                      'SiteCode':"",
                      'FirstName':'',
                      'FirstNameCriteria':'2',
                      'LastName':'',
                      'LastNameCriteria':'2',
                      'GroupName':'',
                      'GroupSearchOption':'2',
                      'CalledBy':'',
                      'CalledByCriteria':'8',
                      'CalledTo':'',
                      'CalledToCriteria':'8',
                      'EncryptedCallsCriteria':'2',
                      'AssociatedAgentCriteria':'2',
                      'CallDateSearchCriteria':'5',
                      'StartDate':'',
                      'EndDate':'',
                      'ParamNumberOfDays':'',
                      'CallDuration':"",
                      'CallDurationCriteria':'3',
                      'CallDirectionCriteria':'0',
                      'ArchivedCallsCriteria':'2',
                      'ScreenCaptureCallsCriteria':"2",
                      'DeviceHangUpCriteria':"2",
                      'GlobalCallID':"",
                      'GlobalCallIDSearchCriteria':"8",
                      'CorrelatorID':"",
                      'CorrelatorIDSearchCriteria':"4",
                      'Device':"",
                      'DeviceSearchCriteria':"5",
                      'FlagSearchCriteria':"all",
                      'Notes':"",
                      'NotesSearchCriteria':"8",
                      'CallStatus':'5',
                      'CallTypeSearchCriteria':"0",
                      'RecordingInterface':"6",
                      'SortExpression':"0",
                      'SortDirection':"0",
                      'ScoredCallOption':"2",
                      'PrimaryPBXIPCriteria':"4",
                      'PrimaryPBXIP':"",
                      'SecondaryPBXIPCriteria':"4",
                      'SecondaryPBXIP':"",
                      'ServerRoleCriteria':"8",    
                      'ServerRole':"0",    
                      'IncludeExternalArchivedCall':"True",    
                      'TotalCallShow':"100",    
                      'ServerIDCriteria':"0",    
                      'ServerID':'0',    
                      'PageNumber':"1",    
                      'CallsPerPage':"50",    
                      'CustomField1_Value':"",    
                      'CustomField1_Criteria':"8",    
                      'CustomField2_Value':"",    
                      'CustomField2_Criteria':"8",    
                      'CustomField3_Value':"",    
                      'CustomField3_Criteria':"8",    
                      'CustomField4_Value':"",    
                      'CustomField4_Criteria':"8",    
                      'CustomField5_Value':"",    
                      'CustomField5_Criteria':"8",    
                      'CustomField6_Value':"",    
                      'CustomField6_Criteria':"8",    
                      'CustomField7_Value':"",    
                      'CustomField7_Criteria':"8",    
                      'CustomField8_Value':"",    
                      'CustomField8_Criteria':"8",    
                      'CustomField9_Value':"",    
                      'CustomField9_Criteria':"8",    
                      'CustomField10_Value':"",    
                      'CustomField10_Criteria':"8",    
                      'SIPTrunkDDI':"",   
                      'RuleID':'', 
                      'RegionValue':'0',
                      'SpeechAnalyticsCriteria':'0',
                      'BoardID':'',
                      'TrunkGroupID':'',
                      'Channel':'',
                      'ProACD':'',
                      'ProACDSearchCriteria':'5',
                      'CallingPartyName':'',
                      'CallingPartyNameSearchCriteria':'8',
                      'GroupID':'',
                      'ParamNumberOfMinutes': '10'

                     }
        
        URL = ''+common.Domain+''+self.UrlForGetRecorderCalls+''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp=response.json()
        showcode = str(resp['ResponseCode'])
        
        if TestCasesStatus==True:
            try:
                if resp['ResponseCode'] == 400:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                     status = 'Failed'
                     assert False
                    
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)
                        
        else:
            TestCasesStatus=False

    def testcase_63_Search_RecordedCalls(self, TestCasesStatus=True):

        starttime = time.process_time()
        TestCaseID = '40-63'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call', 'Using Get Method to Search Recorded Call', 'Get Recorded calls using server session .')

        Parameters = {'AuthToken': config.sessionkey,
                      'AuthUser': config.auth_user,
                      'SiteCode': "",
                      'FirstName': '',
                      'FirstNameCriteria': '8',
                      'LastName': '',
                      'LastNameCriteria': '8',
                      'GroupName': '',
                      'GroupSearchOption': '2',
                      'CalledBy': '',
                      'CalledByCriteria': '8',
                      'CalledTo': '',
                      'CalledToCriteria': '8',
                      'EncryptedCallsCriteria': '2',
                      'AssociatedAgentCriteria': '2',
                      'CallDateSearchCriteria': '5',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'CallDuration': "",
                      'CallDurationCriteria': '3',
                      'CallDirectionCriteria': '0',
                      'ArchivedCallsCriteria': '2',
                      'ScreenCaptureCallsCriteria': "2",
                      'DeviceHangUpCriteria': "2",
                      'GlobalCallID': "",
                      'GlobalCallIDSearchCriteria': "8",
                      'CorrelatorID': "",
                      'CorrelatorIDSearchCriteria': "4",
                      'Device': "",
                      'DeviceSearchCriteria': "5",
                      'FlagSearchCriteria': "all",
                      'Notes': "",
                      'NotesSearchCriteria': "8",
                      'CallStatus': '5',
                      'CallTypeSearchCriteria': "0",
                      'RecordingInterface': "6",
                      'SortExpression': "0",
                      'SortDirection': "0",
                      'ScoredCallOption': "2",
                      'PrimaryPBXIPCriteria': "4",
                      'PrimaryPBXIP': "",
                      'SecondaryPBXIPCriteria': "4",
                      'SecondaryPBXIP': "",
                      'ServerRoleCriteria': "8",
                      'ServerRole': "0",
                      'IncludeExternalArchivedCall': "True",
                      'TotalCallShow': "100",
                      'ServerIDCriteria': "0",
                      'ServerID': '0',
                      'PageNumber': "1",
                      'CallsPerPage': "50",
                      'CustomField1_Value': "",
                      'CustomField1_Criteria': "8",
                      'CustomField2_Value': "",
                      'CustomField2_Criteria': "8",
                      'CustomField3_Value': "",
                      'CustomField3_Criteria': "8",
                      'CustomField4_Value': "",
                      'CustomField4_Criteria': "8",
                      'CustomField5_Value': "",
                      'CustomField5_Criteria': "8",
                      'CustomField6_Value': "",
                      'CustomField6_Criteria': "8",
                      'CustomField7_Value': "",
                      'CustomField7_Criteria': "8",
                      'CustomField8_Value': "",
                      'CustomField8_Criteria': "8",
                      'CustomField9_Value': "",
                      'CustomField9_Criteria': "8",
                      'CustomField10_Value': "",
                      'CustomField10_Criteria': "8",
                      'SIPTrunkDDI': "",
                      'RuleID': '',
                      'RegionValue': '0',
                      'SpeechAnalyticsCriteria': '0',
                      'BoardID': '',
                      'TrunkGroupID': '',
                      'Channel': '',
                      'ProACD': '',
                      'ProACDSearchCriteria': '5',
                      'CallingPartyName': '',
                      'CallingPartyNameSearchCriteria': '8',
                      'GroupID': '',
                      'ParamNumberOfMinutes': '10'

                      }

        URL = '' + common.Domain + '' + self.UrlForGetRecorderCalls + ''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 401:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus = False

    def testcase_64_Search_RecordedCalls(self, TestCasesStatus=True):

        starttime = time.process_time()
        TestCaseID = '40-64'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call', 'Using Get Method to Search Recorded Call', 'Get Recorded calls when CallDateSearchCriteria is 8 and ParamNumberOfMinutes is 10 .')

        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': "",
                      'FirstName': '',
                      'FirstNameCriteria': '8',
                      'LastName': '',
                      'LastNameCriteria': '8',
                      'GroupName': '',
                      'GroupSearchOption': '2',
                      'CalledBy': '',
                      'CalledByCriteria': '8',
                      'CalledTo': '',
                      'CalledToCriteria': '8',
                      'EncryptedCallsCriteria': '2',
                      'AssociatedAgentCriteria': '2',
                      'CallDateSearchCriteria': '5',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'CallDuration': "",
                      'CallDurationCriteria': '3',
                      'CallDirectionCriteria': '0',
                      'ArchivedCallsCriteria': '2',
                      'ScreenCaptureCallsCriteria': "2",
                      'DeviceHangUpCriteria': "2",
                      'GlobalCallID': "",
                      'GlobalCallIDSearchCriteria': "8",
                      'CorrelatorID': "",
                      'CorrelatorIDSearchCriteria': "4",
                      'Device': "",
                      'DeviceSearchCriteria': "5",
                      'FlagSearchCriteria': "all",
                      'Notes': "",
                      'NotesSearchCriteria': "8",
                      'CallStatus': '5',
                      'CallTypeSearchCriteria': "0",
                      'RecordingInterface': "6",
                      'SortExpression': "0",
                      'SortDirection': "0",
                      'ScoredCallOption': "2",
                      'PrimaryPBXIPCriteria': "4",
                      'PrimaryPBXIP': "",
                      'SecondaryPBXIPCriteria': "4",
                      'SecondaryPBXIP': "",
                      'ServerRoleCriteria': "8",
                      'ServerRole': "0",
                      'IncludeExternalArchivedCall': "True",
                      'TotalCallShow': "100",
                      'ServerIDCriteria': "0",
                      'ServerID': '0',
                      'PageNumber': "1",
                      'CallsPerPage': "50",
                      'CustomField1_Value': "",
                      'CustomField1_Criteria': "8",
                      'CustomField2_Value': "",
                      'CustomField2_Criteria': "8",
                      'CustomField3_Value': "",
                      'CustomField3_Criteria': "8",
                      'CustomField4_Value': "",
                      'CustomField4_Criteria': "8",
                      'CustomField5_Value': "",
                      'CustomField5_Criteria': "8",
                      'CustomField6_Value': "",
                      'CustomField6_Criteria': "8",
                      'CustomField7_Value': "",
                      'CustomField7_Criteria': "8",
                      'CustomField8_Value': "",
                      'CustomField8_Criteria': "8",
                      'CustomField9_Value': "",
                      'CustomField9_Criteria': "8",
                      'CustomField10_Value': "",
                      'CustomField10_Criteria': "8",
                      'SIPTrunkDDI': "",
                      'RuleID': '',
                      'RegionValue': '0',
                      'SpeechAnalyticsCriteria': '0',
                      'BoardID': '',
                      'TrunkGroupID': '',
                      'Channel': '',
                      'ProACD': '',
                      'ProACDSearchCriteria': '5',
                      'CallingPartyName': '',
                      'CallingPartyNameSearchCriteria': '8',
                      'GroupID': '',
                      'ParamNumberOfMinutes': '10'

                      }

        URL = '' + common.Domain + '' + self.UrlForGetRecorderCalls + ''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 200:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus = False

    def testcase_65_Search_RecordedCalls(self, TestCasesStatus=True):

        starttime = time.process_time()
        TestCaseID = '40-65'
        common = CF.CommonFunctions()
        common.Header('Search Recorded Call', 'Using Get Method to Search Recorded Call',
                      'Get Recorded calls when CallDateSearchCriteria is 8 and ParamNumberOfMinutes is empty .')

        Parameters = {'AuthToken': config.sessionkeysite,
                      'AuthUser': config.auth_user,
                      'SiteCode': "",
                      'FirstName': '',
                      'FirstNameCriteria': '8',
                      'LastName': '',
                      'LastNameCriteria': '8',
                      'GroupName': '',
                      'GroupSearchOption': '2',
                      'CalledBy': '',
                      'CalledByCriteria': '8',
                      'CalledTo': '',
                      'CalledToCriteria': '8',
                      'EncryptedCallsCriteria': '2',
                      'AssociatedAgentCriteria': '2',
                      'CallDateSearchCriteria': '8',
                      'StartDate': '',
                      'EndDate': '',
                      'ParamNumberOfDays': '',
                      'CallDuration': "",
                      'CallDurationCriteria': '3',
                      'CallDirectionCriteria': '0',
                      'ArchivedCallsCriteria': '2',
                      'ScreenCaptureCallsCriteria': "2",
                      'DeviceHangUpCriteria': "2",
                      'GlobalCallID': "",
                      'GlobalCallIDSearchCriteria': "8",
                      'CorrelatorID': "",
                      'CorrelatorIDSearchCriteria': "4",
                      'Device': "",
                      'DeviceSearchCriteria': "5",
                      'FlagSearchCriteria': "all",
                      'Notes': "",
                      'NotesSearchCriteria': "8",
                      'CallStatus': '5',
                      'CallTypeSearchCriteria': "0",
                      'RecordingInterface': "6",
                      'SortExpression': "0",
                      'SortDirection': "0",
                      'ScoredCallOption': "2",
                      'PrimaryPBXIPCriteria': "4",
                      'PrimaryPBXIP': "",
                      'SecondaryPBXIPCriteria': "4",
                      'SecondaryPBXIP': "",
                      'ServerRoleCriteria': "8",
                      'ServerRole': "0",
                      'IncludeExternalArchivedCall': "True",
                      'TotalCallShow': "100",
                      'ServerIDCriteria': "0",
                      'ServerID': '0',
                      'PageNumber': "1",
                      'CallsPerPage': "50",
                      'CustomField1_Value': "",
                      'CustomField1_Criteria': "8",
                      'CustomField2_Value': "",
                      'CustomField2_Criteria': "8",
                      'CustomField3_Value': "",
                      'CustomField3_Criteria': "8",
                      'CustomField4_Value': "",
                      'CustomField4_Criteria': "8",
                      'CustomField5_Value': "",
                      'CustomField5_Criteria': "8",
                      'CustomField6_Value': "",
                      'CustomField6_Criteria': "8",
                      'CustomField7_Value': "",
                      'CustomField7_Criteria': "8",
                      'CustomField8_Value': "",
                      'CustomField8_Criteria': "8",
                      'CustomField9_Value': "",
                      'CustomField9_Criteria': "8",
                      'CustomField10_Value': "",
                      'CustomField10_Criteria': "8",
                      'SIPTrunkDDI': "",
                      'RuleID': '',
                      'RegionValue': '0',
                      'SpeechAnalyticsCriteria': '0',
                      'BoardID': '',
                      'TrunkGroupID': '',
                      'Channel': '',
                      'ProACD': '',
                      'ProACDSearchCriteria': '5',
                      'CallingPartyName': '',
                      'CallingPartyNameSearchCriteria': '8',
                      'GroupID': '',
                      'ParamNumberOfMinutes': ''

                      }

        URL = '' + common.Domain + '' + self.UrlForGetRecorderCalls + ''
        response = requests.get(URL, headers=Parameters)
        time.sleep(1)
        resp = response.json()
        showcode = str(resp['ResponseCode'])

        if TestCasesStatus == True:
            try:
                if resp['ResponseCode'] == 400:
                    if resp['list'] == '[]':
                        print(common.SuccessMessage)
                        status = 'Passed - But List is Empty'
                    else:
                        print(common.SuccessMessage)
                        status = 'Passed'
                else:
                    status = 'Failed'
                    assert False

            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, status, starttime, resp)

        else:
            TestCasesStatus = False


