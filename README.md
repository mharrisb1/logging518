# logging518

[![PyPI version](https://badge.fury.io/py/logging518.svg)](https://badge.fury.io/py/logging518) ![PyPI - Downloads](https://img.shields.io/pypi/dm/logging518)

Configure Python's native `logging` library using `pyproject.toml`

# About
`logging518` is simply a wrapper around the [`logging` module in the standard library](https://docs.python.org/3/library/logging.html). It allows a developer to configure the module within the `pyproject.toml` config file instead of using an additional `.ini` or `.conf` config file as specified when using the `fileConfig()` method.

Why use `pyproject.toml` instead of `logging.conf`?

[PEP 518](https://www.python.org/dev/peps/pep-0518/) introduced a new config file, `pyproject.toml`, for specifying build dependecies. [An interesting side effect](https://snarky.ca/what-the-heck-is-pyproject-toml/) of this new config file standard is that many tools started allowing developers to configure them using the `pyproject.toml` file that likely already existed in their project.

Using a single, universal config file helps declutter all of those additional config files for each tool (many those `.conf`, `.ini`, `.yml`, etc. files at the root level) bringing some minimalism back in our lives.


# Usage
Under the hood, `logging518` parses the `pyproject.toml` file using the [`toml` library](https://github.com/uiri/toml) and then passes that output to the `dictConfig()` method.

Following the spec in PEP 518 pertaining to the [tool table](https://www.python.org/dev/peps/pep-0518/#tool-table), `logging518` will recognize all config values associated with the `tool.logging518` key.

Any config option specified in the [`logging` configuration dictionary schema](https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema) is allowed.

## Installation

```python
pip install logging518
```

## Example Config

Below is an example `pyproject.toml` file associated with a project using [Poetry](https://python-poetry.org).

```toml
# pyproject.toml

[tool.poetry]
name = "picklr"
version = "0.1.0"
description = "Turns anything into a pickle"
authors = ["Rick Sanchez <rdawgg9000@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

# ------------- logging518 configured below -------------

[tool.logging518]
version = 1
disable_existing_loggers = true

[tool.logging518.formatters.standard]
format = "%(asctime)s %(levelname)-8s %(name)-15s %(message)s"

[tool.logging518.handlers.console]
class = "logging.StreamHandler"
formatter = "standard"
level = "ERROR"
stream = "ext://sys.stdout"

[tool.logging518.handlers.file]
class = "logging.FileHandler"
formatter = "standard"
level = "DEBUG"
filename = "picklr.log"
mode = "w"

[tool.logging518.root]
handlers = ["console", "file"]
level = "NOTSET"
```

The configuration above:

1. Created a formatter called "standard"
2. Created 2 handlers (one for logging to the console and the other for writing to a `.log` file) that both use the formatter created above
3. Configured the root logger to use both handlers created


When parsed by `logging518` the above configuration will turn into the below KV object:

```json
{
    "version": 1,
    "disable_existing_loggers": true,
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
    "root": {
        "handlers": ["console", "file"], 
        "level": "NOTSET"
    },
}
```

**NOTE**: Please see [this StackOverflow post](https://stackoverflow.com/a/7507842) for an dictionary example with `dictConfig()`.


## Using the logger

To access the root logger:

```python
from logging518 import logger

logger.info("This will be an info message")
```

The `logger` object accessed from `logging518` is normal a [regular `Logger` object](https://docs.python.org/3/library/logging.html#logging.Logger) from the `logging` module meaning all of the methods you would normally use are available to you. Note that this is actually the root logger.

Prefer to use `log` instead `logger` when you create a `Logger` object? The below works too (and is just a copy of the `logger` object demoed above):

```python
from logging518 import log

log.info("This will be an info message")
```

To access a logger other than the root, you can use the `get_logger` method:

```python
from logging518 import get_logger

logger = get_logger("foo")
assert logger.name == "foo"
```

## Debugging your configuration

If you would like to peak under the hood and see the dictionary object passed in to `dictConfig()` you can import `debug_config`:

```python
from pprint import pprint
from logging518 import debug_config

pprint(debug_config)
```