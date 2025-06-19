import logging

def setup_logger():
    general_handler = logging.FileHandler("bot.log", encoding="utf-8")
    general_handler.setLevel(logging.INFO)

    error_handler = logging.FileHandler("errors.log", encoding="utf-8")
    error_handler.setLevel(logging.ERROR)

    console_handler = logging.StreamHandler()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[general_handler, error_handler, console_handler]
    )
