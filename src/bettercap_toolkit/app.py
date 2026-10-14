from pathlib import Path
from .ui.menu import run_menu
from .services.logging_service import setup_logging

ROOT = Path(__file__).resolve().parents[2]

def main() -> int:
    (ROOT / "logs").mkdir(exist_ok=True)
    (ROOT / "reports").mkdir(exist_ok=True)
    setup_logging(ROOT / "logs" / "toolkit.log")
    return run_menu(ROOT)
