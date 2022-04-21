# 🪵 logging518

[![PyPI version](https://badge.fury.io/py/logging518.svg)](https://badge.fury.io/py/logging518) ![PyPI - Downloads](https://img.shields.io/pypi/dm/logging518) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/logging518.svg)](https://pypi.org/project/logging518/) [![Test Matrix](https://github.com/mharrisb1/logging518/actions/workflows/test_matrix.yml/badge.svg)](https://github.com/mharrisb1/logging518/actions/workflows/test_matrix.yml)

Use your pyproject.toml (or any other TOML file) to configure Python's native logging module

## Usage

You can use `logging518.config.fileConfig` the same way you would use `logging.config.fileConfig` but instead of passing a ConfigParser-form file, you can pass in a TOML-form file.

```python
import logging
import logging518.config  # instead of logging.config

logging518.config.fileConfig("pyproject.toml")
logger = logging.get_logger("project")

logger.info("Hello, log!")
```

## Configure

`logging518.config.fileConfig` simply deserializes the TOML file you pass in (using `tomli`/`tomllib`) and passes the contents to `logging.config.dictConfig`.

`logging518.config.fileConfig` uses the [tool table](https://peps.python.org/pep-0518/#tool-table) in your TOML file to look up the configuration. All logging config should be defined under `tool.logging` in the tool table.

```toml
[tool.logging]
version = 1
disable_existing_loggers = true

[tool.logging.loggers.project]
level = "WARNING"

[tool.logging.loggers.project.foo_module]
level = "DEBUG"
```

This config would be the same as:

```python
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "loggers": {
        "project": {
            "level": "WARNING"
        },
        "project.foo_module": {
            "level": "DEBUG"
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
```

More examples can be found in the 👩‍🍳 [Cookbook](https://mharrisb1.github.io/logging518/)
