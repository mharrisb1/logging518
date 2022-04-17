import logging
import logging.config

from typing import Union
from pathlib import Path


def fileConfig(fname: Union[str, Path]) -> None:
    """Imitates Python's native logging `fileConfig` interface, but allows
    the developer to pass in a TOML file instead of a ConfigParser-form file.

    Example
    -------

    >>> logging518.config.fileConfig("pyproject.toml")

    Parameters
    ----------
    fname : Union[str, Path]
        File path

    Raises
    ------
    KeyError
        If tool table not found in TOML file
    KeyError
        If logging not found in tool table
    """

    # tomli/tomlib compatibility layer
    try:
        import tomlib  # type: ignore
    except ModuleNotFoundError:
        import tomli as tomlib  # type: ignore

    with open(fname, "rb") as stream:
        toml_dict = tomlib.load(stream)

    tool_table = toml_dict.get("tool", {})

    if not tool_table:
        raise KeyError(
            "Tool table not found in TOML file. See https://peps.python.org/pep-0518/#tool-table"
        )

    tool_table_logging = tool_table.get("logging", {})

    if not tool_table_logging:
        raise KeyError("Logging section not found in tool table. See documentation")

    logging.config.dictConfig(tool_table_logging)
