from logging import Logger

from logging518 import __version__
from logging518.logger518 import default_logging_config, Logger518, __logger518__


def test_version():
    assert __version__ == "0.1.1"


def test_successful_parsing():
    l = __logger518__(file_path="tests/fixtures/example_success.toml")

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


def test_reversion_to_default_config():
    l = __logger518__(file_path="tests/fixtures/example_fail.toml")

    assert l.config == default_logging_config
    assert isinstance(l.logger, Logger)
