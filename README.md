# Bettercap Toolkit

A Python + Bash guided CLI for checking a Bettercap installation, viewing local network details, running read-only discovery commands, collecting logs, and generating reports. It includes guarded ARP/DNS lab workflows for networks you own or have explicit permission to test.

> **Safety:** Run only on an isolated lab or a network you are explicitly authorized to assess. ARP spoofing and DNS spoofing can disrupt connectivity. Active modules are disabled by default, accept only private IPv4 targets, require an explicit confirmation, and do not capture credentials. Do not use this against public, campus, workplace, hotel, or other third-party networks without written authorization.

## Requirements

- Linux (Kali Linux recommended); Windows users can run this inside their Linux VM.
- Python 3.10+
- Bettercap installed separately and available as `bettercap`
- Root privileges may be required for packet-level operations.
- A host-only/internal VirtualBox lab is recommended for active tests.

## Install

```bash
git clone <YOUR_REPOSITORY_URL>
cd Bettercap-Toolkit
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
chmod +x scripts/*.sh
./scripts/check_environment.sh
python main.py
```

If Bettercap is not installed, install it using the official package instructions for your Linux distribution:
https://www.bettercap.org/

## Menu

- Installation/version check
- Network interface and local IP overview
- Read-only Bettercap discovery (`net.probe`, `net.show`)
- ARP lab workflow (explicit private target + confirmation)
- DNS lab workflow (private redirect IP + domain + confirmation)
- Diagnostics, logs, and report generation

## Notes on command handling

The toolkit invokes Bettercap with `-eval` and a validated command string. It never concatenates untrusted shell text into a shell command. Bettercap command names and options can differ between versions; check the installed version and `help` output if a module is unavailable.

## Active lab modules

Active spoofing workflows are deliberately opt-in. Use only a dedicated isolated lab with test devices you control. The DNS lab workflow requires a private redirect IP and a domain you control in that lab. You must stop the session and restore any temporary network configuration when done.

## Project layout

```text
config/                     Configuration defaults
scripts/                    Linux setup/environment scripts
src/bettercap_toolkit/core/ Process/session handling and validation
src/bettercap_toolkit/modules/ Network and lab modules
src/bettercap_toolkit/services/ Logs, config, reports, cleanup
src/bettercap_toolkit/ui/   Terminal UI
docs/                       Installation, architecture, command guide
logs/                       Runtime logs (not committed)
reports/                    Generated reports (not committed)
```

## License

MIT. Bettercap is a separate project with its own license and terms.
