from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class AddTask:
    def __init__(self, driver):
        self.driver = driver
        
        
    def addtask(self, task_text):
        driver = self.driver
        print("adding tasks")
        
        #adding 1st task
        input_box = driver.find_element(By.CLASS_NAME, "new-todo")
        # input_box.send_keys("add a task")
        input_box.send_keys(task_text)
        input_box.send_keys(Keys.RETURN)
        time.sleep(1)
        
        # try:
        #     tasks =  driver.find_elements(By.CLASS_NAME, "main")
        #     for task in tasks:
        #         print("Task found : ",task.text)
        # except Exception as e:
        #     print("NO tasks present yet, to proceed, add a task! ")
 
        # time.sleep(3)