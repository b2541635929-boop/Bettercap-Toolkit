from ..core.runner import BettercapRunner

def show_hosts(interface: str, runner=None) -> str:
    runner = runner or BettercapRunner()
    return runner.execute("net.probe on; net.show", interface=interface)
