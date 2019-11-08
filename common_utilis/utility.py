from baseclass import base
from locators import json_data_reader


# verify_button function will verify the element
def verify_button():
    try:
        base.driver.find_element_by_xpath(json_data_reader.get_json_data('ButtonThree'))
        output_of_hide_button = "Element is present"
        return output_of_hide_button

    except Exception:
        output_of_hide_button = "Element is absent"
        return output_of_hide_button
