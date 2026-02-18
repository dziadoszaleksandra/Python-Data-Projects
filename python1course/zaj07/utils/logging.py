import logging
from datetime import datetime
from pathlib import Path


def get_logger(
    name: str,
    level: int = logging.DEBUG,
    log_dir: Path = Path("logs"),
) -> logging.Logger:
    """Fabryka loggerów aplikacji"""

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # konsola - INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # plik - DEBUG
    log_dir.mkdir(exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d")
    file_handler = logging.FileHandler(
        log_dir / f"app_{date_str}.log", encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
