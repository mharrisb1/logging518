__version__ = "0.2.2"

from .main import Logging518

debug_config = Logging518().config
logger = log = Logging518().logger
get_logger = Logging518.get_logger
