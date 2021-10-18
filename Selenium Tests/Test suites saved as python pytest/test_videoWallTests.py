# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestVideoWallTests():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_videoWallchangevideo(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) .filename").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(2) > button .filename").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) .filename").click()
    self.driver.find_element(By.CSS_SELECTOR, "a > .icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(2) > button .filename").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) .filename").click()
  
  def test_videoWallplayvideo1(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) .filename").click()
  
  def test_videoWallplayvideo2(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(2) > button .filename").click()
  
