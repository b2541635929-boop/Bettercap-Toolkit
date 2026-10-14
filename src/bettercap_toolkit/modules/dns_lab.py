from ..core.command_registry import ACTIVE_LAB_COMMANDS
from ..core.permissions import ensure_lab_mode
from ..core.validator import private_ipv4, interface_name, domain_name, require_confirmation
from ..core.runner import BettercapRunner

def run_dns_lab(domain: str, redirect_ip: str, interface: str, confirmation: str, runner=None) -> str:
    ensure_lab_mode()
    domain = domain_name(domain)
    redirect_ip = private_ipv4(redirect_ip)
    interface = interface_name(interface)
    require_confirmation(confirmation)
    runner = runner or BettercapRunner(timeout=45)
    command = ACTIVE_LAB_COMMANDS["dns_spoof"].format(domain=domain, address=redirect_ip)
    return runner.execute(command, interface=interface)
