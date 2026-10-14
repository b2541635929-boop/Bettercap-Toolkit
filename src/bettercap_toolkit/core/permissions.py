import os
from .exceptions import ValidationError

def ensure_lab_mode() -> None:
    if os.environ.get("BETTERCAP_LAB_MODE") != "1":
        raise ValidationError(
            "Active lab modules are disabled. Set BETTERCAP_LAB_MODE=1 only inside an isolated, authorized lab."
        )
