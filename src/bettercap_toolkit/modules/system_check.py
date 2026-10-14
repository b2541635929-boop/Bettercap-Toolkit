import shutil
import platform
from ..core.runner import BettercapRunner

def get_system_status(runner=None) -> dict:
    runner = runner or BettercapRunner()
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "bettercap_path": shutil.which(runner.executable) or "Not found",
    }
