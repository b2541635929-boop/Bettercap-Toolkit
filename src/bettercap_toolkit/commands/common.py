from ..core.command_registry import READ_ONLY_COMMANDS
from ..core.runner import BettercapRunner

def run_help(runner=None):
    return (runner or BettercapRunner()).execute(READ_ONLY_COMMANDS["help"])
