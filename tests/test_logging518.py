from logging import Logger

from logging518 import __version__
from logging518 import Logging518, logger, log, get_logger


def test_version():
    assert __version__ == "0.2.0"


def test_successful_parsing():
    l = Logging518(file_path="tests/pyproject_test.toml")

    test_dict = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {
                "format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "level": "ERROR",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.FileHandler",
                "formatter": "standard",
                "level": "DEBUG",
                "filename": "picklr.log",
                "mode": "w",
            },
        },
        "root": {"handlers": ["console", "file"], "level": "NOTSET"},
    }

    assert isinstance(l.logger, Logger)
    assert l.config == test_dict


def test_default_fallback():
    l = Logging518()  # default to main pyproject.toml file

    assert l.config == l.default_logging_config
    assert isinstance(l.logger, Logger)


def test_logger_name():
    l1 = logger
    l2 = log
    l3 = get_logger("foo")

    assert l1.name == "root"
    assert l2.name == "root"
    assert l3.name == "foo"
