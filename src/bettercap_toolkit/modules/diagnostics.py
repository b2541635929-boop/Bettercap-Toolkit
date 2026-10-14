import shutil
from ..core.runner import BettercapRunner

def diagnostics(runner=None) -> list[str]:
    runner = runner or BettercapRunner()
    results = []
    results.append(f"Bettercap executable: {shutil.which(runner.executable) or 'not found'}")
    results.append(f"ip utility: {shutil.which('ip') or 'not found'}")
    results.append("Active lab modules: disabled unless BETTERCAP_LAB_MODE=1")
    return results
