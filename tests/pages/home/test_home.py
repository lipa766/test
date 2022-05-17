""" Testing home page """
import pytest
from pages.home.functions import HomePageFunctions


class TestAddAnimals:
    """ Class for testing adding animals """
    @staticmethod
    def test_add_without_animal_and_animal_name(browser):
        """ Test adding without inputs """
        home_page = HomePageFunctions(browser)

        home_page.click_get_animals_button()
        animals_length_before = home_page.get_animal_list_length()

        home_page.click_add_animal_button()

        home_page.click_get_animals_button()
        animals_length_after = home_page.get_animal_list_length()

        assert animals_length_before == animals_length_after

    @staticmethod
    def test_add_name_without_animal(browser):
        """ Test adding only name """
        home_page = HomePageFunctions(browser)

        home_page.click_get_animals_button()
        animals_length_before = home_page.get_animal_list_length()

        home_page.fill_in_animal_name("Patryk")
        home_page.click_add_animal_button()

        home_page.click_get_animals_button()
        animals_length_after = home_page.get_animal_list_length()

        assert animals_length_before == animals_length_after

    @staticmethod
    def test_add_animal_without_name(browser):
        """ Test adding only animal """
        home_page = HomePageFunctions(browser)

        home_page.click_get_animals_button()
        animals_length_before = home_page.get_animal_list_length()

        home_page.fill_in_animal("Cat")
        home_page.click_add_animal_button()

        home_page.click_get_animals_button()
        animals_length_after = home_page.get_animal_list_length()

        assert animals_length_before == animals_length_after

    @staticmethod
    @pytest.mark.parametrize('animal_name,animal_type', [('Patryk', 'Dog'), ('zaq', 'wsx'), ('asd', 'test')])
    def test_add_animal_and_name(browser, animal_name, animal_type):
        """ Test adding both name and animal """
        home_page = HomePageFunctions(browser)

        home_page.click_get_animals_button()
        current_animal_list_length = home_page.get_animal_list_length()

        home_page.fill_in_animal_name(animal_name)
        home_page.fill_in_animal(animal_type)
        home_page.click_add_animal_button()

        home_page.click_get_animals_button()
        assert home_page.get_animal_list_length() == current_animal_list_length + 1

        assert home_page.get_animal_name() == animal_name
        assert home_page.get_animal_type() == animal_type
