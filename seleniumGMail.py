from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime

browser = webdriver.Firefox()
#browser = webdriver.Edge()

url = "https://mail.google.com/mail/#inbox"
print("Opening url: ", url)
browser.get(url)
time.sleep(1)

print("Fill user name...")
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('epd2017.python@gmail.com') #ernirulez

btnNext = browser.find_element_by_id('identifierNext')
btnNext.click()
print("\tWait for password screen load...")
time.sleep(1)

print("Fill user password...")
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('ernirulez')
btnNext = browser.find_element_by_id('passwordNext')
btnNext.click()
print("\tWait for inbox screen load...")
time.sleep(2)


try:
    print("Click compose button...")
    composeElem = browser.find_element_by_css_selector("div.T-I.J-J5-Ji.T-I-KE.L3")
    composeElem.click()
    print("\tWait for compose form load...")
    time.sleep(2)

    print("Fill recipient...")
    elem = browser.find_element_by_name('to')
    elem.send_keys("epd2017.python@gmail.com")
    time.sleep(4)

    print("Fill subject...")
    elem = browser.find_element_by_name('subjectbox')
    elem.send_keys("Subject auto filled at %s" % datetime.datetime.now())
    time.sleep(4)

    print("Fill message body...")
    elem = browser.find_element_by_css_selector('div.Am.Al.editable.LW-avf')
    elem.send_keys("Message body is auto filled, too")
    time.sleep(4)

    print("Click send button...")
    elem.send_keys(Keys.CONTROL, Keys.ENTER)
    #elem = browser.find_element_by_css_selector('div.T-I.J-J5-Ji.aoO.T-I-atl.L3.T-I-JO')
    #elem.click()
    time.sleep(1)
    browser.refresh()
    time.sleep(4)
finally:
    print("Click sign out options...")
    signoutElem = browser.find_element_by_css_selector("a.gb_b.gb_gb.gb_R")
    signoutElem.click()
    print("\tWait for sign out button load...")
    time.sleep(2)

    print("Click sign out button...")
    signoutElem = browser.find_element_by_id('gb_71')
    signoutElem.click()


browser.quit()