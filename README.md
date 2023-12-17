# qa_guru_python_8_22
Задание к двадцать второму уроку курса QA Guru

## локальный запуск на эмулированном устройсте
pytest -s -v --context=local_emulator .

## локальный запуск на реальном устройсте
pytest -s -v --context=local_real_device .

## удаленный запуск на BrowserStack
pytest -s -v --context=bstack .

## Просмотр отчета allure
allure serve .\allure-results\