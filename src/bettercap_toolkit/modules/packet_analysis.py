"""Read-only packet-analysis guidance; no credential capture is implemented."""
GUIDANCE = (
    "Use packet-analysis tools only on traffic you own or are authorized to inspect. "
    "This module does not collect passwords, cookies, or session tokens. "
    "For a simple Bettercap host overview, use the Network Discovery menu option."
)
def packet_analysis_guidance() -> str:
    return GUIDANCE
