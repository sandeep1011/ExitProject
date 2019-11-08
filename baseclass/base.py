from appium import webdriver

# desired capabilities to launch application


def setup():
    desired = {
        "deviceName": "Pixel 3 API 28",
        "platformName": "Android",
        "appPackage": "com.touchboarder.android.api.demos",
        "appActivity": "com.example.android.apis.ApiDemos",
        "path": "application/API.apk"


    }

    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired)


















































