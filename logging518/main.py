from typing import Union
from pathlib import Path
import logging
import logging.config
import toml


class Logging518:
    """Configure Python's logging module from your pyproject.toml file.

    Usage
    -----
    Configure the logger using the pyproject.toml tool table. Logging518 will
        use that configuration whe you create a logger.

    >>> from logging518 import logger
    >>> logger.info("Example info message)
    """

    def __init__(self, file_path: Union[Path, str] = "pyproject.toml") -> None:

        self._file_path = Path(file_path)  # TODO - prop
        self.default_logging_config = {"version": 1}

        with open(self._file_path, "r") as f:
            self._config = (
                toml.load(f)
                .get("tool", {})  # get PEP 518 tool table
                .get("logging518", self.default_logging_config)
            )
            logging.config.dictConfig(self._config)

    @property
    def file_path(self) -> Path:
        return self._file_path

    @property
    def config(self) -> dict:
        return self._config

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger()

    @classmethod
    def get_logger(
        cls, name: str, file_path: Union[Path, str] = "pyproject.toml"
    ) -> logging.Logger:
        cls(file_path)
        return logging.getLogger(name=name)
