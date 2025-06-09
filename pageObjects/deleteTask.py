from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DeleteTask:
    def __init__(self, driver):
        self.driver = driver
        
    def deletetask(self, task_text):
        driver = self.driver
        print("Trying to delete a task -- 'Add a task'")
        action = ActionChains(driver)
        try:
            tasks =  driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
            found = False
            for task in tasks:
                if task_text in task.text:
                    action.move_to_element(task).perform() #hover over the task
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ".//button[@aria-label='Delete']")))
                    delete_button = task.find_element(By.XPATH, ".//button[@aria-label='Delete']")
                    delete_button.click()
                    print("Deleted the task : ", task_text)
                    found = True
                    break
            if not found:
                print("No such task found, please try again!")          
        except Exception as e:
            print("No tasks present yet, to proceed, add a task!")
            print(f"Exception : {e}")
            
        time.sleep(1)