from baseclass import base
from bussinesslogic import animation_hide_button
from bussinesslogic import animation_show_button
from bussinesslogic import app_show_title
# all the test are present in this file


# test_animation_hide_button will verify button is hidden
def test_animation_hide_button():
    base.setup()
    assert animation_hide_button.hide_button_animation() == "Element is absent"


# test_animation_show_button will verify element is  present
def test_animation_show_button():
    base.setup()
    assert animation_show_button.show_button_animation() == "Element is present"


# test_show_title_app will verify the title of app
def test_show_title_app():
    base.setup()
    assert app_show_title.show_title_app() == "App/Action Bar/Display Options"


'''
To run  in terminal
pytest -v -s --html=ExitProjectReport.html --self-contained-html test_api_demos.py

'''












