'''
Created on 10-Sep-2021

@author: nouman.ijaz
'''



from Settings import CommonFunctions as CF
from pickle import FALSE, TRUE
from test_Provisioning import test_02_PBXConfiguration as PC
from test_Provisioning import test_57_NotificationSettings as NS


global DataList

DataList = {}
#common = Cf.CommonFunctions()


class DataStorage:
    
    

    def add_data(self, method_name, header, resp, url, results_modified=FALSE):
        value = [header,  resp, url, results_modified]
        key = method_name
        DataList[key] = value
        
        print(DataList)
        

    def get_ReceiverNumber(self, results_modified):
        '''
        @ results_modified = TRUE if on calling this function results in modification of the return values (Put and 
        Delete methods) 
        '''
        common = CF.CommonFunctions()
        NS_call = NS.test_2_AddNotificationSettings
        
        
        if DataList.__contains__('testcase_2_AddNotificationSettings'):
            modification_status = DataList.get('testcase_2_AddNotificationSettings')[3]

            if modification_status == TRUE:
                
                ReceiverNumber = NS_call.testcase_2_AddNotificationSettings(common.PrereqTestCasesStatusUpdate)
            else:

                ReceiverNumber = DataList.get('testcase_2_AddNotificationSettings')[0]['ReceiverNumber']
                print("Successfully Got ReceiverNumber : " + ReceiverNumber + " from Dictionary")
                if results_modified == TRUE:
                    DataList.get('testcase_2_AddNotificationSettings')[3] = TRUE

        else:
            print("Couldn't find course_id  in Dictionary,Generating course_id")
            
            ReceiverNumber = NS_call.testcase_2_AddNotificationSettings(common.PrereqTestCasesStatusUpdate)
            if results_modified == TRUE:
                DataList.get('testcase_01_AddCourse')[3] = TRUE

        print(ReceiverNumber)
        return ReceiverNumber
    
    
    
    def get_OXENameAndIP(self, results_modified):
        '''
        @ results_modified = TRUE if on calling this function results in modification of the return values (Put and 
        Delete methods) 
        '''
        common = CF.CommonFunctions()
        PC_call = PC.test_1_AddPBXConfiguration
        
        
        if DataList.__contains__('testcase_01_AddPBXConfiguration'):
            modification_status = DataList.get('testcase_01_AddPBXConfiguration')[3]

            if modification_status == TRUE:
                
                OXEName,ValidIP = PC_call.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
            else:
                OXEName = DataList.get('testcase_01_AddPBXConfiguration')[0]['PBXName']
                ValidIP = DataList.get('testcase_01_AddPBXConfiguration')[0]['PrimaryIP']
                print("Successfully Got OXENameAndIP : " + OXEName+ValidIP+ " from Dictionary")
                if results_modified == TRUE:
                    DataList.get('testcase_01_AddPBXConfiguration')[3] = TRUE

        else:
            print("Couldn't find OXEName,ValidIP  in Dictionary,Generating OXEName,ValidIP")
            
            OXEName,ValidIP = PC_call.testcase_01_AddPBXConfiguration(common.PrereqTestCasesStatusUpdate)
            if results_modified == TRUE:
                DataList.get('testcase_01_AddPBXConfiguration')[3] = TRUE

        
        return OXEName,ValidIP