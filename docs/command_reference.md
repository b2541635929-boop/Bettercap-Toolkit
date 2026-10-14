# Command Reference

Commands used by this toolkit (verify against the installed Bettercap version):

- `help` — display Bettercap help.
- `net.show` — display discovered hosts.
- `net.probe on; net.show` — probe the local network, then display discovered hosts.
- ARP lab template: `set arp.spoof.targets <private-lab-ip>; arp.spoof on`
- DNS lab template: `set dns.spoof.domains <lab-domain>; set dns.spoof.address <private-lab-ip>; dns.spoof on`

The last two are active traffic-manipulation operations. They are guarded by explicit opt-in and private-address/domain validation. Only run them in an isolated lab you own or have permission to test. Module settings may vary by Bettercap version; use its built-in `help` output to confirm available options.
