from ..core.command_registry import ACTIVE_LAB_COMMANDS
from ..core.permissions import ensure_lab_mode
from ..core.validator import private_ipv4, interface_name, require_confirmation
from ..core.runner import BettercapRunner

def run_arp_lab(target: str, interface: str, confirmation: str, runner=None) -> str:
    ensure_lab_mode()
    target = private_ipv4(target)
    interface = interface_name(interface)
    require_confirmation(confirmation)
    runner = runner or BettercapRunner(timeout=45)
    command = ACTIVE_LAB_COMMANDS["arp_spoof"].format(target=target)
    return runner.execute(command, interface=interface)
