from driver import Driver
from pages import Page
from speech_conf import SpeechRecognizer
from log_conf import Logger

logging = Logger().get_logger()
logging.info("информ ошибка")
logging.error("ошибка")


def main():
    browser = Driver.start()  
    page = Page(browser)
    speech_recognizer = SpeechRecognizer()

    logging.info("Запуск программы")
    page.speech_insert(speech_recognizer)  

    Driver.finish()  
    logging.info("Программа завершена")

if __name__ == "__main__":
    main()
