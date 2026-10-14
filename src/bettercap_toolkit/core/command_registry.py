"""Central registry for documented, fixed command templates."""
READ_ONLY_COMMANDS = {
    "help": "help",
    "network_show": "net.show",
    "network_probe_show": "net.probe on; net.show",
}
ACTIVE_LAB_COMMANDS = {
    # Templates are filled only after strict validation and explicit confirmation.
    "arp_spoof": "set arp.spoof.targets {target}; arp.spoof on",
    "dns_spoof": "set dns.spoof.domains {domain}; set dns.spoof.address {address}; dns.spoof on",
}
