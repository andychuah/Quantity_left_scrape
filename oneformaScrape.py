
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def switchToAlertThenWaitAlertAndAccept(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.alert_is_present())
    browser.switch_to.alert.accept()

def switchToAlertThenWaitAlertAndDismiss(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.alert_is_present())
    browser.switch_to.alert.dismiss()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://jobs.oneforma.com/')
    account='xxx'
    password='xxx'
    button = driver.find_element_by_link_text("Log In")
    button.click()
    time.sleep(3)
    email_fill = driver.find_element_by_id("form-email")
    email_fill.send_keys(account)
    pw_fill = driver.find_element_by_id("form-password")
    pw_fill.send_keys(password)
    time.sleep(3)
    button_path = 'html/body/div[3]/div/div[2]/div/form/div[2]/div[2]/button/i'
    
    login_button = driver.find_element_by_css_selector("button.btn.btn-primary.float-right")
    login_button.click()
    
    time.sleep(5)
    
    alert_button = driver.find_element_by_xpath("//*[@id='onesignal-slidedown-cancel-button']")
    alert_button.click()
   
    time.sleep(2)
    
    desk_button = driver.find_element_by_link_text("Desk")
    desk_button.click()
   
    time.sleep(2)
    # Go the next tab
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    
    time.sleep(4)
    
    task1_path = '/html/body/div[3]/div[7]/div[2]/div[1]/div/div[2]/div[1]/span/span'
    task1 = driver.find_element_by_xpath(task1_path)
    task1_quantity = task1.text
    print("Task 1 left",task1_quantity,'.')
    
    task2_path = '/html/body/div[3]/div[7]/div[2]/div[2]/div/div[2]/div[1]/span/span'
    task2 = driver.find_element_by_xpath(task2_path)
    task2_quantity = task2.text
    print("Task 2 left",task2_quantity,'.')
    
    

    
   
    
   
    
   
    
   
    
   
   