"""Active lab commands are dispatched only through guarded lab modules."""
from ..modules.arp_lab import run_arp_lab
from ..modules.dns_lab import run_dns_lab

__all__ = ["run_arp_lab", "run_dns_lab"]
