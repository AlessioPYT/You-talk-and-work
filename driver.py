import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from log_conf import Logger
import os
from dotenv import load_dotenv

load_dotenv()

logging = Logger().get_logger()
logging.info("информ ошибка")
logging.error("ошибка")

host = os.getenv("HOST")
port = os.getenv("PORT")
site_url = os.getenv("pass_to_site")

class Driver:
    driver = None

    @classmethod
    def start(cls):
        logging.info("коннект к уже открытому браузеру")
        options = Options()
        options.debugger_address = f"{host}:{port}"  # Подключение к браузеру на порту
        cls.driver = webdriver.Chrome(options=options)
        return cls.driver

    @classmethod
    def find_browser(cls):
        if not cls.driver:
            raise Exception("Браузер не загружен, загрузи в начале")
        logging.info("Выполнение действий в текущем открытом браузере")
        cls.driver.get(site_url)  # Открытие новой страницы (если нужно)
        return cls.driver

    @classmethod
    def finish(cls):
        if cls.driver:
            logging.info("Работа")
            cls.driver.quit()
