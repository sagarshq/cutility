import logging
from cutility.loggers import get_simple_logger


def test_get_simple_logger(caplog):
    logger = get_simple_logger()

    # Use caplog to capture log output
    with caplog.at_level(logging.INFO):
        logger.i("Info message")

    # Check pytest's log capture
    assert "Info message" in caplog.text
    log_record = caplog.records[0]
    assert log_record.levelname == "INFO"
