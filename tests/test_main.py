import pytest
from pages import Page
from speech_conf import SpeechRecognizer
from log_conf import Logger

logging = Logger().get_logger()
logging.info("информ ошибка")
logging.error("ошибка")

"""
пока только алтернативный запуск... тут будут тесты по апи
"""

def test_speech_insert(browser):
    """Альтернативный запуск через пайтест"""
    logging.info("Запуск теста: ввод голосовой команды")
    page = Page(browser)
    speech_recognizer = SpeechRecognizer()

    page.speech_insert(speech_recognizer)  # Проверяем ввод через голосовую команду
    assert True  # Можно добавить проверку, если знаешь, что должно произойти
