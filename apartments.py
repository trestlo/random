import sys, os, time, json, uuid, urllib2, urllib, smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)


driver.get("http://www.equityapartments.com/arlington/courthouse/courthouse-plaza-apartments")

plazaBeds = driver.find_elements_by_class_name("starting-from")

plazaBedsPrice = plazaBeds[1].text

driver.get("http://www.equityapartments.com/arlington/courthouse/2201-wilson-apartments")

wilsonBeds = driver.find_elements_by_class_name("starting-from")

wilsonBedsPrice = wilsonBeds[1].text

body = "Courthouse Plaza = " + plazaBedsPrice + '\n' + "2201 Wilson = " + wilsonBedsPrice

driver.quit()

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

sendemail(from_addr    = 'aurpineiro@gmail.com', 
          to_addr_list = ['leo.pineiro@outlook.com'],
          cc_addr_list = [], 
          subject      = 'Apartment Prices', 
          message      = body, 
          login        = 'aurpineiro', 
          password     = '')
