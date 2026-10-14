import shutil
import subprocess

def get_network_info():
    if not shutil.which("ip"):
        return "The Linux 'ip' utility was not found."
    result = subprocess.run(["ip", "-brief", "address"], capture_output=True,
                            text=True, timeout=10, check=False)
    output = (result.stdout or result.stderr).strip()
    if result.returncode:
        return output or "Unable to read network interfaces."
    return output or "No interfaces reported."
