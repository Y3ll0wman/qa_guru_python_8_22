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
        # Specify device and os_version for testing
        'platformName': 'android',
        'platformVersion': '13.0',
        'deviceName': 'Samsung Galaxy S23 Ultra',

        # Set URL of the application under test
        # "app": "bs://sample.app",
        'app': 'bs://04b49845ae18715f926fe263abfef9701aa7a4d6',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'Android tests',
            'buildName': 'browserstack-wikipedia-build',
            'sessionName': 'BStack wikipedia_test',

            # Set your access credentials
            'userName': 'konstantinvarvar_PVsOgD',
            'accessKey': 'VVA32jN9kwsJHmxS92Wx'
        }
    })

    # browser.config.driver_remote_url = remote_browser_url
    # browser.config.driver_options = options

    with allure.step('setup app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options
        )

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
