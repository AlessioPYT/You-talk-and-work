from log_conf import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from speech_conf import SpeechRecognizer

logging = Logger().get_logger()
logging.info("информ ошибка")
logging.error("ошибка")

xpath_1 = os.getenv("xpath1")
xpath_2 = os.getenv("xpath2")
xpath_3 = os.getenv("xpath3")
text_for_start = os.getenv("start")


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.speech_recognizer = SpeechRecognizer()

    def check_info(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            current_text = element.get_attribute("value")  
            
            if not current_text.strip():  
                return True
            return False  
        except Exception as e:
            logging.error(f"Ошибка при проверке информации: {e}")
            return False

    def insert_info(self, xpath, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(text)
            logging.info("Информация успешно введена")
        except Exception as e:
            logging.error(f"Ошибка при вводе информации: {e}")

    def speech_insert(self, speech_recognizer):
        try:
            logging.info("Ожидание голосовой команды...")
            command = self.speech_recognizer.listen_command()  

            if text_for_start in command:
                logging.info("Команда распознана, начинаем ввод текста")

                xpath = xpath_3  
                self.insert_info(xpath, "Начинаем ввод текста...")  

                text = speech_recognizer.listen_text() 
                if text:
                    self.insert_info(xpath, text)  
                else:
                    logging.info("Текст не был распознан")
        except Exception as e:
            logging.error(f"Ошибка при голосовом вводе: {e}")
