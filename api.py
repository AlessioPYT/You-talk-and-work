from fastapi import FastAPI
from speech_conf import SpeechRecognizer
from driver import Driver
from pages import Page

app = FastAPI()
speech_recognizer = SpeechRecognizer()

@app.get("/listen")
async def listen():
    """Распознает голосовую команду и возвращает текст"""
    command = speech_recognizer.listen_command()
    return {"command": command}

@app.post("/open_page/")
async def open_page(url: str):
    """Открывает страницу в браузере через Selenium"""
    browser = Driver.start()
    browser.get(url)
    return {"status": "success", "opened": url}

@app.post("/insert_text/")
async def insert_text(xpath: str, text: str):
    """Вставляет текст в поле по XPath"""
    browser = Driver.find_browser()
    page = Page(browser)
    page.insert_info(xpath, text)
    return {"status": "success", "xpath": xpath, "text": text}
