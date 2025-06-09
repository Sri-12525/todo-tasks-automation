import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pageObjects.addTask import AddTask
from pageObjects.deleteTask import DeleteTask
from pageObjects.completeTask import CompleteTask
from pageObjects.taskCount import TaskCount
from pageObjects.navigatefilters import Filters

@pytest.mark.usefixtures("setup")
class TestE2E:
    
    def test_addtask(self):
        driver = self.driver
        #add task
        add_task = AddTask(driver)
        add_task.addtask("Add a task")
        add_task.addtask("Delete a task")
        add_task.addtask("Complete a task")
        add_task.addtask("Find task count")
        
    
    def test_deletask(self):
        driver = self.driver
        #delete task
        delete_task = DeleteTask(driver)
        delete_task.deletetask("Add a task")
        

    def test_completetask(self):
        driver = self.driver
        #complete task
        complete_task = CompleteTask(driver)
        complete_task.completetask("Delete a task")

    def test_activetaskscount(self):
        driver = self.driver
        #task count
        task_count = TaskCount(driver)
        print(task_count.activetaskscount())
            
    def test_filters(self):
        driver = self.driver
        driver.implicitly_wait(5)
        #check filter navigation
        filter = Filters(driver)
        filter.navigateFilters("Active")
        print("You are on active tasks filter.")
        filter.navigateFilters("Completed")
        print("You are on completed tasks filter.")
        filter.navigateFilters("All")
        print("You are on all tasks filter.")
        print("Clearing completed tasks -- ")
        filter.navigateFilters("Clear")
        print("Cleared completed tasks ! ")
        
        
        
        
        
        
        
        