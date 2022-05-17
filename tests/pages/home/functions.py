""" Functions for finding elements on frontend """
from base_page import BasePage
from pages.home.locators import HomePageLocators


class HomePageFunctions(BasePage):
    """ Functions for home page"""

    def fill_in_animal_name(self, name):
        """ Filling animal name input """
        element = self._driver.find_element(*HomePageLocators.name_insert)
        element.send_keys(name)

    def fill_in_animal(self, animal):
        """ Filling animal input """
        element = self._driver.find_element(*HomePageLocators.animal_insert)
        element.send_keys(animal)

    def click_add_animal_button(self):
        """ Clicking button for adding animal """
        element = self._driver.find_element(*HomePageLocators.add_button)
        element.click()

    def click_get_animals_button(self):
        """ Clicking button for getting animals"""
        element = self._driver.find_element(*HomePageLocators.get_button)
        element.click()

    def get_animal_list_length(self):
        """ Return number of animals """
        elements = self._driver.find_elements(*HomePageLocators.animal_list)
        return len(elements)

    def get_animal_name(self):
        """ Return last animal name """
        elements = self._driver.find_elements(*HomePageLocators.animal_name)
        return elements[-1].text

    def get_animal_type(self):
        """ Return last animal """
        elements = self._driver.find_elements(*HomePageLocators.animal_type)
        return elements[-1].text
