from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TaskCount:
    def __init__(self, driver):
        self.driver = driver
        
    def activetaskscount(self):
        driver = self.driver
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "main")))
            tasks =  driver.find_elements(By.CLASS_NAME, "main")
            
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.todo-count")))
            no_of_activeTasks = driver.find_element(By.CSS_SELECTOR, "span.todo-count").text
            return no_of_activeTasks
            
            
        except Exception as e:
            print("No tasks present yet, to proceed, add a task!")
            print(f"Exception : {e}")
        
        time.sleep(1)
            