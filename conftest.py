import allure
import allure_commons
import pytest
# import config

from appium.options.android import UiAutomator2Options
from selene import browser, support
from appium import webdriver
# from qa_guru_python_8_22.utils import allure_attach


@pytest.fixture(scope='function')
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        'deviceName': 'Pixel_3a_API_34_extension_level_7_x86_64',
        'appWaitActivity': 'org.wikipedia.*',
        "app": "C:\Users\Y3ll0w\Desktop\app-alpha-universal-release.apk",
    })

    # browser.config.driver_remote_url = remote_browser_url
    # browser.config.driver_options = options

    # with allure.step('setup app session'):
    #     browser.config.driver = webdriver.Remote(
    #         config.remote_browser_url,
    #         options=options
    #     )

    browser.config.timeout = 10.0

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext)

    yield

    # allure_attach.screenshot()

    # allure_attach.page_source_xml()

    # session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    # allure_attach.bstack_video(session_id)
