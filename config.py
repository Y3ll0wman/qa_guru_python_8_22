import os

from appium.options.android import UiAutomator2Options
from qa_guru_python_8_22 import utils


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == 'local_emulator':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))

    if context == 'local_real_device':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        options.set_capability(
            'bstack:options', {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',
                'userName': os.getenv('USER_NAME'),
                'accessKey': os.getenv('ACCESS_KEY'),
            },
        )

    return options
