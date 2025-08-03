import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome() DriverManager().install()) 
    driver.maximize_window()
    yield driver
    driver.quit()