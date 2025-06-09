from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CompleteTask:
    def __init__(self, driver):
        self.driver = driver
        
    def completetask(self, task_text):
        driver = self.driver
        print("Trying to mark tasks as completed...")

        try:
            # WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "ul.todo-list li")) >= 4)
            tasks = driver.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
            found = False
            WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "ul.todo-list li")) <= 4)
            
            #print all the pending tasks
            
            for task in tasks:
                label = task.find_element(By.CSS_SELECTOR, "label")
                print("Task label found:", label.text)  # 💡 debug print
                
            for task in tasks:
                label = task.find_element(By.CSS_SELECTOR, "label")

                if task_text in label.text:
                    # Click the checkbox directly (no hover)
                    complete_button = task.find_element(By.CSS_SELECTOR, "input.toggle")
                    driver.execute_script("arguments[0].click();", complete_button)  # 🚀 Use JS click!
                    print(f"Completed the task : {task_text} !! Cheers 🥳")
                    found = True
                    break
            if not found:
                print("No such task found, please try again!")
        except Exception as e:
            print("No tasks present yet, to proceed, add a task!")
            print(f"Exception: {e}")
            
        time.sleep(1)
            
