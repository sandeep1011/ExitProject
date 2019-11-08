from baseclass import base
from locators import json_data_reader


# show_title_app function will return the title of app
def show_title_app():
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('App')).click()
    base.driver.find_element_by_id(json_data_reader.get_json_data('ActionBar')).click()
    base.driver.find_element_by_xpath(json_data_reader.get_json_data('DisplayOptions')).click()
    base.driver.find_element_by_id(json_data_reader.get_json_data('ShowTitle')).click()
    base.driver.find_element_by_id(json_data_reader.get_json_data('ShowTitle')).click()
    title_app = base.driver.find_element_by_id(json_data_reader.get_json_data('GetTitle'))
    return title_app.text






