import pytest
from driver import Driver 
from log_conf import Logger

logging = Logger().get_logger()
logging.info("информ ошибка")
logging.error("ошибка")

@pytest.fixture(scope="session")
def browser():
    """Фикстура для работы с WebDriver"""
    driver = Driver.start()  
    yield driver 
    Driver.finish()  
