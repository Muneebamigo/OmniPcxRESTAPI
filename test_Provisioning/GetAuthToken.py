'''
Created on Sep 20, 2021

@author: Numan Ijaz
'''
import sys

import  requests,os
from unittest import TestCase

from Settings import dataFunction as DataFunction
from InputDataFiles import SeleniumConfigration as SC
from InputDataFiles import InputData
from Key import config

class GetAuthToken(TestCase):
    global UrlForGetAccessToken,ds
    UrlForGetAccessToken = '/Authentication/GetSessionAuthToken'
    ds = DataFunction.DataStorage()
    
    global  I
   
    I= InputData.InputData
  


    # Server AuthToken
    def testcase_01_GetServerAuthkey(self):

        S = SC.SeleniumConfig()
        
        
        
        
        #browser = S.InitializeBrowser(webdriver)
        #browser = S.SignInServer(browser)
        #S.ClickAPIToken(browser)
        # integratortoken = S.get_APITokenUserandIntegrator()[1]
        #browser.quit()

        # i have do some changes to check the key genratation they access the web & get from web now they have to get from config.py
        Parameters = {
            "AuthToken": config.integrated_auth_token,
            "AuthUser": config.auth_user,
            "AuthPassword": config.auth_password,
            "AuthenticationType": "0"}

        URL = '' +I.Domain+ '' + UrlForGetAccessToken + ''

        response = requests.get(URL, headers=Parameters)
        #print(response.content)
        resp = response.json()
        authkey_server = str(resp['AuthToken'])
        print('authkey_server: ' + authkey_server)

     #   return authkey_server

    # Site AuthToken
    def testcase_02_GetSiteAuthkey(self):

        S = SC.SeleniumConfig()
        
       # browser = S.InitializeBrowser(webdriver)
        #browser = S.SignInServer(browser)
        #S.ClickAPIToken(browser)
        # integratortoken = S.get_APITokenUserandIntegrator()[1]
        #browser.quit()
        #integratortoken = self.S.CreateNewTokenIntegrator(browser)
        Parameters = {
            "AuthToken": config.integrated_auth_token,
            "AuthUser": config.auth_user,
            "SiteCode": config.site_code, #I.SiteCode
            "AuthPassword": config.auth_password,
            "AuthenticationType": "0"}

        URL = '' +I.Domain+ '' + UrlForGetAccessToken + ''

        response = requests.get(URL, headers=Parameters)
        #print(response.content)
        resp = response.json()
        authkey_site = str(resp['AuthToken'])
        print('authkey_Site ' + authkey_site)

       # return authkey_site

    def testcase_03_GetSiteAuthkeyUserToken(self):

        S = SC.SeleniumConfig()
        #browser = S.InitializeBrowser(webdriver)
        #browser = S.SignInServer(browser)
        #S.ClickAPIToken(browser)
        
        
        # usertoken = S.get_APITokenUserandIntegrator()[0]
        #browser.quit()

        Parameters = {
            "AuthToken": config.integrated_auth_token,
            "AuthUser": config.auth_user,
            "SiteCode": config.site_code,  # I.SiteCode
            "AuthPassword": config.auth_password,
            "AuthenticationType": "0"}

        URL = '' +I.Domain+ '' + UrlForGetAccessToken + ''

        response = requests.get(URL, headers=Parameters)
       # print(response.content)
        resp = response.json()
        authkey_site_User = str(resp['AuthToken'])
        print('authkey_Site_UserToken ' + authkey_site_User)

     #   return authkey_site_User
        
 
   



