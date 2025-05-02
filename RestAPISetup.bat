@echo off
setlocal EnableDelayedExpansion

REM Change to the correct working directory
cd /d "C:\Users\muneeb.ahmed\Downloads\OmniPcx_2.5.0.5-RestAPI_Automation\RESTAPI"

REM Check if the test_Provisioning directory exists
if not exist "test_Provisioning" (
    echo Error: test_Provisioning directory not found!
    pause
    exit /B 1
)

if "%$ecbId%" == "" (
    :Proc1
    echo Enter '1' to Execute whole Project
    echo Enter '2' to Execute any single module
    echo Enter anything else to abort.
    echo.
    set "UserChoice=abort"
    set /P "UserChoice=Type input: "

    if "!UserChoice!"=="1" (
        pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html ".\test_Provisioning"
    )
    if "!UserChoice!"=="2" (
        :Proc2
        echo Single Modules List
        echo Enter '3' to Execute System Settings
        echo Enter '4' to Execute PBX Configuration
        echo Enter '5' to Execute Packetizer Configuration
        echo Enter '6' to Execute Device Configuration
        echo Enter '7' to Execute Team Configuration
        echo Enter '8' to Execute Site Agent Configuration
        echo Enter '9' to Execute Recording Transfer Settings
        echo Enter '10' to Execute Storage Settings
        echo Enter '11' to Execute PRS Settings
        echo Enter '12' to Execute Recorder Settings
        echo Enter '13' to Execute Authentication Settings
        echo Enter '14' to Execute SNMP Settings
        echo Enter '15' to Execute SMTP Settings
        echo Enter '16' to Execute Server Permissions
        echo Enter '17' to Execute Server User Configuration
        echo Enter '18' to Execute Server Incidents
        echo Enter '19' to Execute Branch
        echo Enter '20' to Execute Send Branch Email
        echo Enter '21' to Execute Server Status
        echo Enter '22' to Execute SIP Trunk
        echo Enter '23' to Execute Change Password
        echo Enter '24' to Execute Event Configuration
        echo Enter '25' to Execute Modules Configuration
        echo Enter '26' to Execute Traces Configuration
        echo Enter '27' to Execute System Level Filter
        echo Enter '28' to Execute System Level Rule
        echo Enter '29' to Execute Default Recording Actions
        echo Enter '30' to Execute Site Settings
        echo Enter '31' to Execute Site Permissions
        echo Enter '32' to Execute User Level Filter
        echo Enter '33' to Execute Call Flags Configuration
        echo Enter '34' to Execute Custom Fields
        echo Enter '35' to Execute Archive Job
        echo Enter '36' to Execute Board
        echo Enter '37' to Execute Equipment
        echo Enter '38' to Execute Trunk Group
        echo Enter '39' to Execute Calls
        echo Enter '40' to Execute Search Recorded Calls
        echo Enter '41' to Execute Calls Count
        echo Enter '42' to Execute Notes
        echo Enter '43' to Execute Call Flags
        echo Enter '44' to Execute CDR Fields
        echo Enter '45' to Execute Recorded File URL
        echo Enter '46' to Execute Recorded File Playback URL
        echo Enter '47' to Execute SearchByGlobalIDs
        echo Enter '48' to Execute SearchByCallIDs
        echo Enter '49' to Execute Email Template
        echo Enter '50' to Execute Speech Analytics
        echo Enter '51' to Archive Schedule
        echo Enter '52' to Search Related Calls
        echo Enter '53' to Incident Settings
        echo Enter '54' Network Adapter Settings
        echo Enter '55' PBX User Management
        echo Enter '56' Dashboard Configuration
        echo Enter '57' Notification Settings
        echo Enter '98' to Execute Change Password
        echo Enter '99' to Send Rest API Test Cases Executed Sheet to Users
        echo Enter anything else to abort
        echo Enter 'r' to return main menu
        echo.
        set "UserChoice=abort"
        set /P "UserChoice=Type input: "

        if "!UserChoice!"=="3" (
            pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html ".\test_Provisioning\test_01_SystemSettings.py"
            goto :Proc2
        )
        if "!UserChoice!"=="4" (
            pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html ".\test_Provisioning\test_02_PBXConfiguration.py"
            goto :Proc2
        )
        if "!UserChoice!"=="5" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_03_PacketizerConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="6" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_04_DeviceConfigurations.py
					goto :Proc2
				)
				if "!UserChoice!"=="7" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_05_TeamConfigurations.py
					goto :Proc2
				)
				if "!UserChoice!"=="8" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_06_SiteAgentConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="9" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_07_RecordingTransferSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="10" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_08_StorageSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="11" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_09_PRSSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="12" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_10_RecorderSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="13" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_11_AuthenticationSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="14" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_12_SNMPSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="15" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_13_SMTPSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="16" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_14_ServerPermission.py
					goto :Proc2
				)
				if "!UserChoice!"=="17" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_15_ServerUserConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="18" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_18_ServerIncidents.py
					goto :Proc2
				)
				if "!UserChoice!"=="19" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_19_Branch.py
					goto :Proc2
				)
				if "!UserChoice!"=="20" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_20_SendBranchEmail.py
					goto :Proc2
				)
				if "!UserChoice!"=="21" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_21_ServerStatus.py
					goto :Proc2
				)
				if "!UserChoice!"=="22" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_22_SIPTrunk.py
					goto :Proc2
				)
				if "!UserChoice!"=="23" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_23_ChangePassword.py
					goto :Proc2
				)
				if "!UserChoice!"=="24" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_24_EventsConfigurations.py
					goto :Proc2
				)
				if "!UserChoice!"=="25" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_25_ModulesConfigurations.py
					goto :Proc2
				)
				if "!UserChoice!"=="26" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_26_TracesConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="27" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_27_SystemLevelFilters.py
					goto :Proc2
				)
				if "!UserChoice!"=="28" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_28_SystemLevelRuleConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="29" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_29_DefaultRecordingAction.py
					goto :Proc2
				)
				if "!UserChoice!"=="30" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_30_SiteSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="31" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_31_SitePermissionConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="32" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_32_UserLevelFilter.py
					goto :Proc2
				)
				if "!UserChoice!"=="33" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_33_CallFlagsConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="34" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_34_CustomFields.py
					goto :Proc2
				)
				if "!UserChoice!"=="35" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_35_ArchiveJob.py
					goto :Proc2
				)
				if "!UserChoice!"=="36" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_36_Board.py
					goto :Proc2
				)
				if "!UserChoice!"=="37" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_37_Equipment.py
					goto :Proc2
				)
				if "!UserChoice!"=="38" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_38_TrunkGroup.py
					goto :Proc2
				)
				if "!UserChoice!"=="39" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_39_AddCalls.py
					goto :Proc2
				)
				if "!UserChoice!"=="40" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_40_SearchRecordedCalls.py
					goto :Proc2
				)
				if "!UserChoice!"=="41" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_41_CallsCount.py
					goto :Proc2
				)
				if "!UserChoice!"=="42" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_42_Notes.py
					goto :Proc2
				)
				if "!UserChoice!"=="43" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_43_CallFlagsToARecordedCall.py
					goto :Proc2
				)
				if "!UserChoice!"=="44" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_44_CDRFields.py
					goto :Proc2
				)
				if "!UserChoice!"=="45" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_45_RecordedFileURL.py
					goto :Proc2
				)
				if "!UserChoice!"=="46" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_46_RecordedFilePlaybackURL.py
					goto :Proc2
				)
				if "!UserChoice!"=="47" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_47_SearchRecordedCallsByGlobalCallID.py
					goto :Proc2"
				)
				if "!UserChoice!"=="48" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_48_SearchRecordedCallsByCallIDs.py
					goto :Proc2
				)
				if "!UserChoice!"=="49" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_49_EmailTemplate.py
					goto :Proc2
				)
				if "!UserChoice!"=="50" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_50_SpeechAnalytics.py
					goto :Proc2
				)
				if "!UserChoice!"=="51" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_51_ArchiveSchedule.py
					goto :Proc2
				)
				if "!UserChoice!"=="52" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_52_SearchRelatedCalls.py
					goto :Proc2
				)
				if "!UserChoice!"=="53" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_53_IncidentSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="54" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_54_NetworkAdapterSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="55" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_55_PBXUserManagementConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="56" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_56_DashboardConfiguration.py
					goto :Proc2
				)
				if "!UserChoice!"=="57" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_57_NotificationSettings.py
					goto :Proc2
				)

				if "!UserChoice!"=="99" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\test_Provisioning\test_99_TestCasesSheetEmail.py
					goto :Proc2
				)
				if "!UserChoice!"=="r" (
					goto :Proc1
				)
    )
)

pause