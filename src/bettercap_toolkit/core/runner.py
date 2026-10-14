import logging
import shutil
import subprocess
from .exceptions import BettercapError
from .validator import interface_name

log = logging.getLogger(__name__)

class BettercapRunner:
    def __init__(self, executable="bettercap", timeout=30, popen_factory=subprocess.run):
        self.executable = executable
        self.timeout = timeout
        self._run = popen_factory

    def installed(self) -> bool:
        return shutil.which(self.executable) is not None

    def version(self) -> str:
        try:
            result = self._run([self.executable, "-version"], capture_output=True,
                               text=True, timeout=self.timeout, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise BettercapError(f"Could not check Bettercap version: {exc}") from exc
        output = (result.stdout or result.stderr or "").strip()
        if result.returncode != 0:
            raise BettercapError(output or "Bettercap version check failed.")
        return output or "Version output was empty."

    def execute(self, command: str, interface: str | None = None) -> str:
        # Command strings are only assembled by validated internal module functions.
        if not command or any(ch in command for ch in ("\n", "\r", "\x00")):
            raise BettercapError("Empty or malformed Bettercap command.")
        args = [self.executable]
        if interface:
            args.extend(["-iface", interface_name(interface)])
        args.extend(["-eval", command])
        log.info("Executing Bettercap operation (command details omitted from log)")
        try:
            result = self._run(args, capture_output=True, text=True,
                               timeout=self.timeout, check=False)
        except subprocess.TimeoutExpired as exc:
            raise BettercapError("Bettercap timed out. Check interface and permissions.") from exc
        except OSError as exc:
            raise BettercapError(f"Unable to start Bettercap: {exc}") from exc
        output = "\n".join(x for x in [result.stdout, result.stderr] if x).strip()
        if result.returncode != 0:
            raise BettercapError(output or f"Bettercap exited with status {result.returncode}.")
        return output or "(No output returned.)"
