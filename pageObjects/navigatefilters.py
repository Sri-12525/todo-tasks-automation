from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Filters:
    def __init__(self, driver):
        self.driver = driver
        
    def navigateFilters(self, filter_text):
        driver = self.driver
        
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "main")))
            tasks = driver.find_elements(By.CLASS_NAME, "main")
            
            WebDriverWait(driver, 10 ).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='filters']")))
            filters = driver.find_elements(By.XPATH, "//ul[@class='filters']")
            for filter in filters:
                if "Active" in filter_text:
                    filter_button = filter.find_element(By.XPATH ,"./li/a[@href='#/active']")
                    filter_button.click()
                    time.sleep(2)
                elif "All" in filter_text:
                    filter_button = filter.find_element(By.XPATH ,"./li/a[@href='#/']")
                    filter_button.click()
                    time.sleep(2)
                elif "Completed" in filter_text:
                    filter_button = filter.find_element(By.XPATH ,"./li/a[@href='#/completed']")
                    filter_button.click()
                    time.sleep(2)
                    
            if "Clear" in filter_text:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR , "button.clear-completed")))
                clear_completed_button = driver.find_element(By.CSS_SELECTOR , "button.clear-completed")
                clear_completed_button.click()
                    
        except Exception as e:
            print("No tasks present yet, please try again ! ")
            print(f"Exception : {e}")
        
        time.sleep(1)