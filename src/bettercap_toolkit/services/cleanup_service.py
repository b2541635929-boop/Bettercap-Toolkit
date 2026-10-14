"""Conservative cleanup helper: does not alter system networking automatically."""
def cleanup_notice() -> str:
    return (
        "Stop any Bettercap session with Ctrl+C, disable any active module from that session, "
        "and restore lab network settings manually. Toolkit cleanup never changes firewall, "
        "routing, or DNS settings automatically."
    )
