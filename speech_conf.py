import speech_recognition as sr
from log_conf import Logger

logging = Logger().get_logger()
logging.info("информ ошибка")
logging.error("ошибка")

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_command(self):
        with self.microphone as source:
            logging.info("Слушаю команду...")
            self.recognizer.adjust_for_ambient_noise(source)  # Улучшает качество распознавания
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio, language="ru-RU")
            logging.info(f"Команда: {command}")
            return command.lower()  # Преобразуем в нижний регистр для удобства
        except sr.UnknownValueError:
            print("Не удалось распознать команду")
            return ""
        except sr.RequestError:
            print("Ошибка подключения к сервису распознавания речи")
            return ""

    def listen_text(self):
        full_text = ""
        while True:
            with self.microphone as source:
                print("Говорите текст (пауза завершит ввод)...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio, language="ru-RU")
                print(f"Распознанный текст: {text}")
                full_text += " " + text
            except sr.UnknownValueError:
                print("Не удалось распознать текст, завершение ввода...")
                break  # Выход из цикла, если ничего не распознано
            except sr.RequestError:
                print("Ошибка подключения к сервису распознавания речи")
                break

        return full_text.strip()

