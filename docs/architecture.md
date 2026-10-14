# Architecture

- `ui/`: terminal UI only.
- `modules/`: one feature per module.
- `core/runner.py`: process invocation; no shell interpolation.
- `core/validator.py`: input checks for interface names, private IPv4 addresses, domains, and confirmation.
- `core/command_registry.py`: central command templates.
- `services/`: config, logs, reports, and cleanup guidance.

Active modules are disabled unless `BETTERCAP_LAB_MODE=1` is set. Unit tests should mock the runner rather than sending packets.
