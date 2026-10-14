# Troubleshooting

- `bettercap not found`: install Bettercap from your distribution's trusted package source and verify `which bettercap`.
- Permission error: packet-level operations may require elevated privileges; prefer isolated lab VMs and minimum required privileges.
- Unknown module/setting: run Bettercap's `help` and check the installed version. Do not assume every release exposes identical module settings.
- No hosts shown: verify the interface, lab adapter mode, client connectivity, and that devices are on the same isolated subnet.
- Timeout: verify Bettercap exits normally and no process is waiting on an interactive terminal.
- Active module blocked: check `BETTERCAP_LAB_MODE=1` and enter the confirmation phrase exactly.
