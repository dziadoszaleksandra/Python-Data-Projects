from zajecia07.utils.logging import get_logger

logger = get_logger(__name__)


def run():
    logger.info("Start modułu example")
    logger.debug("Szczegóły debugowe example")


if __name__ == "__main__":
    run()
