import logging

class Logger:
    _instance = None  # Атрибут класса для хранения единственного экземпляра

    def __new__(cls, name="Logger"):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(name)
            cls._instance.logger.setLevel(logging.DEBUG)

            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            if not cls._instance.logger.hasHandlers():  
                cls._instance.logger.addHandler(handler)

        return cls._instance

    def get_logger(self):
        return self.logger

