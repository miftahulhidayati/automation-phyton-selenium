from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
  driver = webdriver.Chrome()
  yield driver
  driver.quit()

def test_googling(driver):
  driver.get('http://www.google.com')
  driver.find_element(By.NAME,'q').send_keys('Miftahul Hidayati' + Keys.ENTER)
  assert 'Miftahul Hidayati' in driver.find_element(By.CSS_SELECTOR,'h3').text
  assert 'Miftahul Hidayati' in driver.title

def test_googling_radit(driver):
  driver.get('http://www.google.com')
  driver.find_element(By.NAME,'q').send_keys('Raditya Dika' + Keys.ENTER)
  assert 'Raditya Dika' in driver.find_element(By.CSS_SELECTOR,'h3').text
  assert 'Raditya Dika' in driver.title