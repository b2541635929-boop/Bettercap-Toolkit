"""Thin session facade. Active operations remain opt-in in module handlers."""
from .runner import BettercapRunner

class BettercapSession:
    def __init__(self, runner=None):
        self.runner = runner or BettercapRunner()

    def run_readonly(self, command: str, interface: str | None = None) -> str:
        return self.runner.execute(command, interface)
