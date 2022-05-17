""" locators for frontend """
from selenium.webdriver.common.by import By


class HomePageLocators:
    """ Home page locators """
    name_insert = (By.ID, 'name')
    animal_insert = (By.ID, 'animal')
    add_button = (By.NAME, 'add_animal')
    get_button = (By.NAME, 'get_animals')
    animal_list = (By.CLASS_NAME, 'animal-list-item')
    animal_name = (By.CLASS_NAME, 'animal-name')
    animal_type = (By.CLASS_NAME, 'animal-type')
