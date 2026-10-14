from ..core.command_registry import READ_ONLY_COMMANDS
from ..core.runner import BettercapRunner

def show_network(runner=None, interface=None):
    return (runner or BettercapRunner()).execute(READ_ONLY_COMMANDS["network_show"], interface)

def probe_network(runner=None, interface=None):
    return (runner or BettercapRunner()).execute(READ_ONLY_COMMANDS["network_probe_show"], interface)
