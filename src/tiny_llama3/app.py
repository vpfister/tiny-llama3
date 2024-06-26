import logging

logger = logging.getLogger("tiny_llama3")


class App:
    def __init__(self, settings) -> None:
        self.settings = settings

    def start(self) -> None:
        logger.info("tiny_llama3 Starting")

    def stop(self) -> None:
        logger.info("tiny_llama3 Stopping")
