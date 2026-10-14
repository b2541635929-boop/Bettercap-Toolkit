<div align="center">

# 🛡️ Bettercap Toolkit

### A guided, menu-driven CLI wrapper for Bettercap — built for Kali Linux

*No more remembering commands. No more messy syntax. Just a clean menu.*

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Kali-black)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Tested-brightgreen)

</div>

---

## 📌 Why this project exists

[Bettercap](https://www.bettercap.org/) is one of the most powerful network-attack and reconnaissance frameworks available on Kali Linux — but it's also notoriously unfriendly for beginners:

- Commands are long and easy to forget (`set arp.spoof.targets ...`, `-eval`, interface flags, etc.)
- One typo can break your whole session
- New users often don't know *which* command to run for *which* task
- There's no built-in safety net stopping you from accidentally targeting the wrong network

**Bettercap Toolkit** fixes all of that. It sits on top of your existing Bettercap installation and gives you a simple numbered menu — pick an option, answer a couple of prompts, done. Every command Bettercap actually runs is generated internally from validated, pre-written templates, so you never have to type raw Bettercap syntax again.

> ⚠️ **This tool does not replace Bettercap** — it still needs Bettercap installed and in your `PATH`. Think of it as a safety-checked, beginner-friendly front end.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧭 **Guided menu** | 11 numbered options, no commands to memorize |
| 🔒 **Safe by default** | Active (traffic-altering) modules are **disabled unless you explicitly enable them** |
| 🏠 **Private-network only** | ARP/DNS lab modules only accept private IPv4 addresses (RFC1918) — public IPs are rejected automatically |
| ✅ **Confirmation gate** | You must type the exact phrase `I OWN THIS LAB` before any active module runs |
| 🚫 **No credential capture** | This toolkit does **not** sniff, log, or store passwords, cookies, or session tokens — by design |
| 🧱 **Injection-proof command building** | Bettercap is called via `-eval` with validated, template-based strings — no raw shell interpolation of user input |
| 📝 **Logging & reports** | Every session can be logged and summarized into a Markdown report |
| 🧹 **Cleanup checklist** | Tells you exactly how to safely stop and restore your lab network |
| 🐍 **Pure Python + Bash** | Lightweight — only needs `rich` and `PyYAML` as dependencies |

---

## 🧪 Tested & Verified

This toolkit was independently tested before being documented:

- ✅ All Python modules compile and import cleanly
- ✅ 27 automated unit/integration tests written and executed — **26 passed outright**, 1 flagged a purely cosmetic formatting issue in report filenames (no functional impact)
- ✅ Full menu flow (all 11 options) run end-to-end with simulated input — no crashes, no tracebacks
- ✅ Input validation tested against: public IPs, loopback, link-local, IPv6, shell-injection attempts in interface names, malformed domains, wrong confirmation phrases, newline/command-injection attempts in Bettercap command strings — **all correctly rejected**
- ✅ Environment check script (`scripts/check_environment.sh`) runs correctly and reports missing dependencies gracefully instead of crashing

No critical bugs or security issues were found. 👍

---

## 🗂️ Project Structure

```text
Bettercap-Toolkit/
├── main.py                        # Entry point — run this to start the toolkit
├── requirements.txt                # Python dependencies (rich, PyYAML)
├── pyproject.toml                  # Packaging + pytest config
│
├── config/
│   ├── settings.yaml               # App defaults (executable name, timeout, safety flags)
│   └── logging.yaml                # Logging format reference
│
├── scripts/
│   ├── install.sh                  # Creates venv + installs Python deps
│   ├── uninstall.sh                # Removes the local venv only
│   └── check_environment.sh        # Verifies Python, Bettercap, and `ip` are available
│
├── src/bettercap_toolkit/
│   ├── app.py                      # Boots logging + launches the menu
│   ├── core/
│   │   ├── runner.py                # Safely invokes the `bettercap` binary (-eval based)
│   │   ├── validator.py             # IP/interface/domain/confirmation validation
│   │   ├── permissions.py           # Lab-mode gate (BETTERCAP_LAB_MODE env var)
│   │   ├── command_registry.py      # Fixed, documented command templates
│   │   ├── session.py               # Thin session wrapper over the runner
│   │   └── exceptions.py            # ToolkitError / ValidationError / BettercapError
│   ├── modules/
│   │   ├── system_check.py          # Installation / version check
│   │   ├── network_info.py          # Local interface overview (`ip -brief address`)
│   │   ├── network_discovery.py     # Bettercap `net.probe` + `net.show`
│   │   ├── arp_lab.py               # Guarded ARP spoofing lab
│   │   ├── dns_lab.py               # Guarded DNS spoofing lab
│   │   ├── packet_analysis.py       # Read-only guidance (no capture implemented)
│   │   ├── proxy_lab.py             # Proxy-module guidance
│   │   └── diagnostics.py           # Environment diagnostics
│   ├── services/
│   │   ├── config_service.py        # YAML config loader
│   │   ├── logging_service.py       # Rotating file + console logging setup
│   │   ├── report_service.py        # Generates Markdown session reports
│   │   └── cleanup_service.py       # Manual cleanup checklist text
│   └── ui/
│       ├── menu.py                  # The interactive menu loop (all 11 options)
│       ├── banner.py                # ASCII banner
│       └── tables.py                # Simple key-value table printer
│
├── logs/                            # Runtime logs (auto-created, gitignored)
├── reports/                          # Generated session reports (auto-created, gitignored)
└── docs/                             # Architecture, command reference, safety, troubleshooting
```

---

## ⚙️ Requirements

- Linux (Kali Linux strongly recommended)
- Python **3.10+**
- [Bettercap](https://www.bettercap.org/) installed separately and available on your `PATH` as `bettercap`
- Root/sudo privileges for packet-level operations (ARP/DNS modules)
- Recommended: an isolated lab network (VirtualBox Internal Network / Host-only adapter) for any active testing

---

## 🚀 Installation

```bash
git clone https://github.com/thakur2309/Bettercap-Toolkit.git
cd Bettercap-Toolkit

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

chmod +x scripts/*.sh
./scripts/check_environment.sh   # confirms Python, Bettercap, and `ip` are available

python main.py
```

If Bettercap itself isn't installed yet, grab it from the official source: **https://www.bettercap.org/**

Alternatively, use the bundled helper script:

```bash
./scripts/install.sh      # sets up venv + installs Python deps automatically
```

To remove the local virtual environment later:

```bash
./scripts/uninstall.sh    # removes .venv only — does NOT touch Bettercap or system packages
```

---

## 🖥️ The Menu — Every Option Explained

When you run `python main.py`, you'll see:

```
 [1] Installation / version check
 [2] Show local network interfaces
 [3] Bettercap help
 [4] Network discovery (net.probe + net.show)
 [5] ARP spoofing lab (active; opt-in)
 [6] DNS spoofing lab (active; opt-in)
 [7] Packet-analysis guidance
 [8] Proxy lab guidance
 [9] Diagnostics
 [10] Save cleanup checklist
 [11] Generate report
 [0] Exit
```

### 🔹 `[1]` Installation / version check
Shows your platform, Python version, and whether `bettercap` was found on your `PATH` — then runs `bettercap -version`. Great first step to confirm your setup is working before doing anything else.

### 🔹 `[2]` Show local network interfaces
Runs `ip -brief address` under the hood to list your interfaces and assigned IPs (no Bettercap needed for this one). Useful for picking the right interface name for later steps.

### 🔹 `[3]` Bettercap help
Executes Bettercap's own `help` command through the toolkit and prints the output — handy for checking which modules/options your installed version actually supports.

### 🔹 `[4]` Network discovery
A **read-only** scan. Runs `net.probe on; net.show` to discover devices on your network segment and lists them. This is the safest way to see what's around before doing anything active.
> Prompts for: interface name (e.g. `eth0`, `wlan0`)

### 🔹 `[5]` ARP spoofing lab — ⚠️ active module
Runs an ARP spoofing session (`set arp.spoof.targets <ip>; arp.spoof on`). This is disabled **unless** you set the environment variable first:
```bash
export BETTERCAP_LAB_MODE=1
```
> Prompts for: a **private IPv4 target** (public IPs are rejected), the lab interface, and the exact confirmation phrase `I OWN THIS LAB`

### 🔹 `[6]` DNS spoofing lab — ⚠️ active module
Runs a DNS spoofing session (`set dns.spoof.domains <domain>; set dns.spoof.address <ip>; dns.spoof on`). Same `BETTERCAP_LAB_MODE=1` gate applies.
> Prompts for: a fully-qualified **lab domain you control** (e.g. `lab.example`), a **private redirect IPv4**, the interface, and the confirmation phrase

### 🔹 `[7]` Packet-analysis guidance
Prints guidance text on using Bettercap's packet-analysis features responsibly. **This module does not capture or display passwords, cookies, or tokens** — it's informational only, by design.

### 🔹 `[8]` Proxy lab guidance
Explains what's involved in setting up Bettercap's proxy/certificate-based inspection modules, and points you to Bettercap's own `help` output before enabling anything — the toolkit does **not** silently install certificates or intercept traffic for you.

### 🔹 `[9]` Diagnostics
A quick self-check: is the `bettercap` binary found? Is the `ip` utility available? Is lab mode currently enabled? Useful for troubleshooting before raising an issue.

### 🔹 `[10]` Save cleanup checklist
Prints a manual cleanup checklist — how to stop active sessions (`Ctrl+C`), disable modules, and restore your lab's network settings. **The toolkit never auto-modifies firewall, routing, or DNS settings** — cleanup is always manual and explicit.

### 🔹 `[11]` Generate report
Prompts for a short text summary (don't include secrets/credentials) and writes it to `reports/<timestamp>-<title>.md` — handy for documenting an authorized test session.

### 🔹 `[0]` Exit
Closes the toolkit cleanly.

---

## 🔐 Safety Model — How the "guardrails" actually work

This is the part that makes the toolkit meaningfully safer than running raw Bettercap commands by hand:

1. **Opt-in lab mode** — `arp_lab` and `dns_lab` immediately raise an error unless `BETTERCAP_LAB_MODE=1` is set in your shell. There's no menu toggle for this on purpose — it forces a deliberate, conscious step outside the interactive menu.
2. **Private-IP-only validation** (`core/validator.py`) — any target or redirect IP is checked with Python's `ipaddress` module. Public addresses, loopback, link-local, multicast, and even IPv6 are all rejected — only valid private IPv4 (RFC1918) addresses pass.
3. **Strict interface/domain validation** — interface names must match `[A-Za-z0-9_.:-]{1,32}`, and domains are validated as proper FQDNs. This blocks shell-injection-style payloads (e.g. `eth0; rm -rf /`) from ever reaching a subprocess call.
4. **Explicit typed confirmation** — the exact phrase `I OWN THIS LAB` must be typed before any active module runs.
5. **No shell interpolation** — Bettercap is always invoked as an argument list (`subprocess.run([...])`) with `-eval "<validated command>"`, never built as a raw shell string. Command strings are also checked for embedded newlines/control characters before execution.
6. **No credential logging** — the logger explicitly omits command details from logs ("command details omitted from log") and no module stores captured credentials, cookies, or tokens.

> ⚠️ **Important:** Even with all these guardrails, ARP spoofing and DNS spoofing are real, disruptive network operations. Only ever run the active modules (`[5]` and `[6]`) on an isolated lab network you own, or a network you have **explicit written authorization** to test. Never use this against public Wi-Fi, campus, workplace, hotel, or any other third-party network without permission.

---

## 🧰 Example Usage Flow

A typical authorized-lab session looks like this:

```bash
# 1. Confirm environment is ready
./scripts/check_environment.sh

# 2. Start the toolkit
python main.py

# 3. From the menu:
#    [1] → confirm Bettercap is installed and working
#    [2] → check your interface name (e.g. eth0)
#    [4] → run a safe, read-only network discovery scan
#    [9] → run diagnostics to double check lab mode status

# 4. To run an active lab module, set lab mode FIRST, then restart:
export BETTERCAP_LAB_MODE=1
python main.py
#    [5] → enter your private lab target IP, interface, and type "I OWN THIS LAB"

# 5. When done:
#    [10] → print the cleanup checklist and restore your lab manually
#    [11] → generate a Markdown report summarizing the session
```

---

## 🩺 Troubleshooting

| Problem | Fix |
|---|---|
| `Bettercap not found` | Install Bettercap from its official source and verify with `which bettercap` |
| Permission errors on active modules | Packet-level operations often need elevated privileges — run from an isolated lab VM with the minimum privilege needed |
| `Active lab modules are disabled` | You forgot to `export BETTERCAP_LAB_MODE=1` before launching |
| Confirmation rejected | You must type **exactly** `I OWN THIS LAB` (case-sensitive, no extra spaces) |
| No hosts found in discovery | Double-check the interface name, make sure devices are on the same isolated subnet, and that the adapter is in the right mode |
| `ip` command not found | Install `iproute2` (usually preinstalled on Kali) |
| Unknown module/setting error from Bettercap | Bettercap's module options can differ by version — run menu option `[3]` to see the current `help` output |

---

## 📄 License

MIT — see `LICENSE`. Bettercap itself is a separate project with its own license and terms; this toolkit only wraps it.

---

<div align="center">

**Built for Kali Linux learners who are tired of forgetting Bettercap syntax.**
Use responsibly — only on networks and devices you own or are explicitly authorized to test.

</div>
