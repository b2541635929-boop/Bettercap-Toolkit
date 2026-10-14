class ToolkitError(Exception):
    """Base exception for expected toolkit errors."""

class ValidationError(ToolkitError):
    """Input did not pass safety validation."""

class BettercapError(ToolkitError):
    """Bettercap invocation failed."""
