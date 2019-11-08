from baseclass import base
from locators import json_data_reader
from common_utilis import utility


# hide_button_animation function will hide the buttons
def hide_button_animation():
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('Animation')).click()
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('HideShowAnimation')).click()
    base.driver.implicitly_wait(30)
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('ButtonOne')).click()
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('ButtonTwo')).click()
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('ButtonThree')).click()
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('ButtonFour')).click()
    base.driver.implicitly_wait(30)
    return utility.verify_button()









