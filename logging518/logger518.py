from dataclasses import dataclass
from typing import Union
from pathlib import Path
import logging
import logging.config
import toml

"""
If config file not found or logging518 not found in tool table
    then the below values will be passed in to dictConfig() for
    logging configuration

Currently setup with the minimal configuration required
"""
default_logging_config = {"version": 1}


@dataclass(frozen=True)
class Logger518:
    file_path: Path
    logger: logging.Logger
    config: dict


def __logger518__(file_path: Union[Path, str] = "pyproject.toml") -> Logger518:
    """Constructor function for Logger518 object

    Parameters
    ----------
    file_path : Union[Path, str], optional
        Path to PEP 518 config file, by default "pyproject.toml"

    Returns
    -------
    Logger518
        Dataclass object with `logger` and `config` attributes
    """
    l518_file_path = Path(file_path)

    with open(l518_file_path, "r") as f:
        tool_table = toml.load(f).get("tool", {})
        l518_config = tool_table.get("logging518", default_logging_config)
        logging.config.dictConfig(l518_config)

    l518_logger = logging.getLogger(__name__)

    return Logger518(
        file_path=l518_file_path.absolute(),
        logger=l518_logger,
        config=l518_config,
    )


# ------------------ export fully constructed objects below ------------------

_L = __logger518__()

logger = log = _L.logger
debug_config = _L.config
debug_file_path = _L.file_path
