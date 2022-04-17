# 🪵 logging518

[![PyPI version](https://badge.fury.io/py/logging518.svg)](https://badge.fury.io/py/logging518) ![PyPI - Downloads](https://img.shields.io/pypi/dm/logging518)

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

`logging518.config.fileConfig` simply deserializes the TOML file you pass in (using `tomli`/`tomlib`) and passes the contents to `logging.config.dictConfig`.

`logging518.config.fileConfig` uses the [tool table](https://peps.python.org/pep-0518/#tool-table) to look up the configuration. All logging config should be defined under `tool.logging`.

```toml
[tool.logging]
version = 1
disable_existing_loggers = true

[tool.logging.loggers.project]
level = "WARNING"

[tool.logging.loggers.project.troubling.module]
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
        "project.troubling.module": {
            "level": "DEBUG"
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
```

### Expectations

`logging518.config.fileConfig` assumes the following:

1. The file passed in is valid TOML (else will result in `tomlib.TOMLDecodeError`)
2. The file contains a tool table (else will result in `KeyError`)
3. `logging` is found in the tool table (else will result in `KeyError`)

### Configuring the root logger

I haven't done much testing but using the empty key (`""`) to configure the logger doesn't play well with TOML. Instead, it is recommended to configure the root logger like this:

```toml
[tool.logging]
version = 1
disable_existing_loggers = true

[tool.logging.root] # root logger
level = "NOTSET"

[tool.logging.loggers.not_root] # not root logger
level = "WARNING"
```
