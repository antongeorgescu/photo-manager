import logging
from typing import Any

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
)

logger = logging.getLogger(__name__)  # Create a logger for this module

def log_info(message):
    """Log an informational message."""
    logger.info(message)

def log_warning(message):
    """Log a warning message."""
    logger.warning(message)

def log_error(message):
    """Log an error message."""
    logger.error(message)

def log_debug(message):
    """Log a debug message."""
    logger.debug(message)

tool_usage_log = []

def log_tool_usage(tool_name: str, input_data: Any):
    """Logs the tool used and its input."""
    tool_usage_log.append({"tool": tool_name, "input": input_data})