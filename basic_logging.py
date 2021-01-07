import logging

logging.basicConfig(
    filename="./logs/basic_logging.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
    level="DEBUG",
)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.warning("this is a warning")