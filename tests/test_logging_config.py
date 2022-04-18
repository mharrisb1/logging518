import logging
import logging518.config

import pytest

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def test_successful_config():
    logging518.config.fileConfig("tests/mock/success.toml")
    logger = logging.getLogger("project.child")

    print("\n")  # helps make pytest output more readable

    logger.debug("This should appear in consoleChild")
    logger.info("This should appear in consoleChild")
    logger.warning("This should appear in consoleChild and consoleParent")
    logger.error("This should appear in consoleChild and consoleParent")


def test_failure_config():
    with pytest.raises(tomllib.TOMLDecodeError):
        logging518.config.fileConfig("tests/mock/failure.toml")


def test_config_without_tool_table():
    with pytest.raises(KeyError):
        logging518.config.fileConfig("tests/mock/missing_tool_table.toml")


def test_config_without_logging_in_tool_table():
    with pytest.raises(KeyError):
        logging518.config.fileConfig("tests/mock/missing_logging_in_tool_table.toml")
