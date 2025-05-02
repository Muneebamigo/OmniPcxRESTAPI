'''
Created on Sep 4, 2018

update on Feb 17, 2024
this last upadate successfully on 2.5.0.15 release
@author: Muneeb.ahmed

'''

import smtplib
from unittest import TestCase
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from Settings import CommonFunctions as CF
from email import encoders
from InputDataFiles import InputData as ID
from Key import config

class Test_1_TestCasesSheetEmail(TestCase):
    
    def testcase_01_TestCasesSheetEmail(self):
        # Calling Common Functions
        common = CF.CommonFunctions()
        # Calling Common Functions
        IDF = ID.InputData()
        
        MailFrom = IDF.SenderEmailAddress
        # MailTo = IDF.mailto
        # MailCC = IDF.mailcc
        MailTo = [IDF.UserOne]
        MailCC = [IDF.UserTwo]
        msg = MIMEMultipart()
        
        msg['From'] = MailFrom
        msg['To'] = ','.join(MailTo)
        msg['Cc'] = ','.join(MailCC)
        msg['Subject'] = IDF.Subject
        
        emailbody = IDF.EmailBody
        
        msg.attach(MIMEText(emailbody, 'plain'))
        
        # filename = 'R2.5.0.16-OmniPCX RECORD REST API Automated Tests Sheet.xlsx'
        filename = config.file_name
        attachment = open(common.OutPutFilePath, "rb")

        
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        msg.attach(part)
        
        server = smtplib.SMTP(IDF.SMTPServerName, 587)
        server.starttls()
        server.login(MailFrom, IDF.SMTPPassword)
        text = msg.as_string()
        server.sendmail(MailFrom, MailTo, text)
        server.quit()