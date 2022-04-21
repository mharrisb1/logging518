---
layout: default
title: "🪵 Logging518"
---

# 👩‍🍳 Cookbook

This cookbook will use examples from the [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#using-logging-in-multiple-modules) to show how you would accomplish the same configuration with a TOML file.

## Using Logging in Multiple Modules

[Source](https://docs.python.org/3/howto/logging-cookbook.html#using-logging-in-multiple-modules)

**Note**: Added mode functionality by setting `propagate` to `False` to make sure the log only appears once.

```toml
# pyproject.toml
[tool.logging]
version = 1

[tool.logging.formatters.formatter]
class = "logging.Formatter"
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

[tool.logging.handlers.fh]
level = "DEBUG"
class = "logging.FileHandler"
file = "spam.log"
formatter = "formatter"

[tool.logging.handlers.ch]
level = "ERROR"
class = "logging.StreamHandler"
formatter = "formatter"

[tool.logging.spam_application]
level = "DEBUG"
handlers = ["fh", "ch"]

[tool.logging.spam_application.auxiliary]
propagate = false

[tool.logging.spam_application.auxiliary.Auxiliary]
propagate = false
```
