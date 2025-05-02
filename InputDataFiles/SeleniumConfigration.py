import json
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from InputDataFiles import InputData


class SeleniumConfig():
    global I
    I = InputData.InputData

    def Generate_autoken(self):
        from test_Provisioning import GetAuthToken as Auth
        A = Auth.GetAuthToken
        authkey_server = A.testcase_01_GetServerAuthkey(self)
        authkey_site = A.testcase_02_GetSiteAuthkey(self)
        authkey_site_User = A.testcase_03_GetSiteAuthkeyUserToken(self)
    
        User_Key, Integrator_Key = SeleniumConfig.get_APITokenUserandIntegrator(self)
 
        AuthTokenDic = {
            "Domain": I.MainPrimaryServerIP,
            "User_Key": User_Key,
            "Integrator_Key": Integrator_Key,
            "authkey_server": authkey_server,
            "authkey_site": authkey_site,
            "authkey_site_User": authkey_site_User,
            "Date": str(datetime.now().date()),
            "Time": str(time.strftime("%H:%M:%S", time.localtime()))
        }

        Jsonfilelocaton = os.path.abspath(__file__).replace(
            r"InputDataFiles\SeleniumConfigration.py", "Settings"
        ) + r"\AuthToken.json"

        print(Jsonfilelocaton)
        with open(Jsonfilelocaton, 'w') as fp:
            json.dump(AuthTokenDic, fp)
            
        return authkey_server, authkey_site, authkey_site_User
    
    def get_APITokenUserandIntegrator(self):
        Jsonfilelocaton = os.path.abspath(__file__).replace("InputDataFiles\SeleniumConfigration.py",
                                                            "Settings") + "\AuthToken.json"
        f = open(Jsonfilelocaton, )

        # returns JSON object as

        data = json.load(f)
        
        if I.MainPrimaryServerIP == data["Domain"] and str(datetime.now().date()) == data['Date']:
            User_token = data["User_Key"]
            Integrator_Token = data["Integrator_Key"]
        else:
            print("Getting Token from Web")
            browser = webdriver.Chrome(
                executable_path=r"C:\Users\muneeb.ahmed\Downloads\OmniPcx_2.5.0.5-RestAPI_Automation\RESTAPI\InputDataFiles\chromedriver.exe")
            browser.maximize_window()
            browser.get('http://' + I.MainPrimaryServerIP + '/OmniPCXRECORD/TenantAdmin.aspx')

            # Web Login
            email = browser.find_element(By.NAME, 'ctrl_TenantAdmin1$txtUserName')  # Enter email ID
            email.send_keys(I.authuser)

            password = browser.find_element(By.NAME, 'ctrl_TenantAdmin1$txtPassword')  # Enter password
            password.send_keys(I.authpassword)

            sign_in = browser.find_element(By.ID, 'ctrl_TenantAdmin1_imgBtnLogin')  # Press submit button
            sign_in.click()

            # Click on API token
            browser.find_element_by_id('ctl00_ctrl_LeftMenuCloud1_hlnkAPIToken').click()

            # Get User Token
            Utoken_name = "User_Automation"
            Itoken_name = "Integrator_Automation"

            # initializing variables
            UserTokenFound = False
            IntegratorTokenFound = False

            rows = len(browser.find_elements(By.XPATH, "//tr[@role='row']"))
            x = 1
            while x < rows:
                col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
                if col.text.__contains__(Utoken_name):
                    browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                    print("Element Found to copy")
                    UserTokenFound = True
                    break
                x += 1

            if UserTokenFound == False:
                print("User not found")
                # Enter name
                browser.find_element_by_id('tbName').send_keys(Utoken_name)
                time.sleep(3)
                # User token
                select_token = Select(browser.find_element_by_css_selector(".combobox"))
                # select by visible text
                select_token.select_by_visible_text('User')
                # Generate Token
                browser.find_element_by_css_selector(".button.buttonStandardWidth.updatebutton").click()

                rows = len(browser.find_elements(By.XPATH, "//tr[@role='row']"))
                x = 1
                while x < rows:
                    col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
                    if col.text.__contains__(Utoken_name):  # Utoken
                        browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                        print("Element Found to copy")
                        break
                    x += 1

            User_token = browser.find_element_by_id('txtViewToken').get_attribute('value')
            browser.find_element_by_id('btnCloseViewToken').click()

            # Getting Integrator Token
            x = 1
            while x < rows:
                col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
                if col.text.__contains__("Integrator_Automa..."):  # Itoken_name
                    browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                    print("Element Found to copy")
                    IntegratorTokenFound = True
                    break
                x += 1

            if IntegratorTokenFound == False:
                print("Integrator not found")
                # Enter name
                browser.find_element_by_id('tbName').send_keys(Itoken_name)

                # User token
                select_token = Select(browser.find_element_by_css_selector(".combobox"))
                # select by visible text
                select_token.select_by_visible_text('Integrator')

                # Generate Token
                browser.find_element_by_css_selector(".button.buttonStandardWidth.updatebutton").click()

                rows = len(browser.find_elements(By.XPATH, "//tr[@role='row']"))
                x = 1
                while x < rows:
                    col = browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[1]")
                    if col.text.__contains__(Itoken_name):  # before Utoken
                        browser.find_element_by_xpath("//*[@id='gvAPIToken']/tbody/tr[" + str(x) + "]/td[5]/div/img").click()
                        print("Element Found to copy")
                        break
                    x += 1

            Integrator_Token = browser.find_element_by_id('txtViewToken').get_attribute('value')
            browser.find_element_by_id('btnCloseViewToken').click()

        AuthTokenDic = {
            "Domain": I.MainPrimaryServerIP,
            "User_Key": User_token,
            "Integrator_Key": Integrator_Token,
            "authkey_server": "",
            "authkey_site": "",
            "authkey_site_User": "",
            "Date": '',
            "Time": ""
        }

        Jsonfilelocaton = os.path.abspath(__file__).replace(
            r"InputDataFiles\SeleniumConfigration.py", "Settings"
        ) + r"\AuthToken.json"

        print(Jsonfilelocaton)
        with open(Jsonfilelocaton, 'w') as fp:
            json.dump(AuthTokenDic, fp)

        return User_token, Integrator_Token
    
    def get_autoken(self):
        # Opening JSON file
        Jsonfilelocaton = os.path.abspath(__file__).replace(
            r"InputDataFiles\SeleniumConfigration.py", "Settings"
        ) + r"\AuthToken.json"

        with open(Jsonfilelocaton, 'r') as f:
            data = json.load(f)
        
        if str(datetime.now().date()) == data['Date']:
            print("Date ok")
            
            time_interval = datetime.strptime(str(time.strftime("%H:%M:%S", time.localtime())), "%H:%M:%S") - datetime.strptime(data["Time"], "%H:%M:%S")
            time_interval = time_interval.total_seconds()
            print(time_interval)
            
            if int(time_interval) < 1500:
                print("time ok")
                authkey_server = data['authkey_server']
                authkey_site = data['authkey_site']
                authkey_site_User = data['authkey_site_User']
            else:
                print("time nok")
                authkey_server, authkey_site, authkey_site_User = SeleniumConfig.Generate_autoken(self)
        else:
            print("date nok")
            authkey_server, authkey_site, authkey_site_User = SeleniumConfig.Generate_autoken(self)
        
        return authkey_server, authkey_site, authkey_site_User


if __name__ == '__main__':
    obj = SeleniumConfig()
    obj.get_APITokenUserandIntegrator()
