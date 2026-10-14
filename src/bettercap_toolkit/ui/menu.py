import os
from pathlib import Path
from ..core.runner import BettercapRunner
from ..core.exceptions import ToolkitError
from ..modules.system_check import get_system_status
from ..modules.network_info import get_network_info
from ..modules.network_discovery import show_hosts
from ..modules.arp_lab import run_arp_lab
from ..modules.dns_lab import run_dns_lab
from ..modules.diagnostics import diagnostics
from ..modules.packet_analysis import packet_analysis_guidance
from ..modules.proxy_lab import proxy_guidance
from ..services.report_service import write_report
from ..services.cleanup_service import cleanup_notice
from .banner import BANNER

def _pause():
    input("\nPress Enter to return to menu...")

def run_menu(root: Path) -> int:
    runner = BettercapRunner()
    while True:
        print(BANNER)
        print(" [1] Installation / version check")
        print(" [2] Show local network interfaces")
        print(" [3] Bettercap help")
        print(" [4] Network discovery (net.probe + net.show)")
        print(" [5] ARP spoofing lab (active; opt-in)")
        print(" [6] DNS spoofing lab (active; opt-in)")
        print(" [7] Packet-analysis guidance")
        print(" [8] Proxy lab guidance")
        print(" [9] Diagnostics")
        print(" [10] Save cleanup checklist")
        print(" [11] Generate report")
        print(" [0] Exit")
        try:
            choice = input("\nSelect option: ").strip()
        except EOFError:
            print("\nInput closed; exiting.")
            return 0
        try:
            if choice == "0":
                return 0
            elif choice == "1":
                print(get_system_status(runner))
                try:
                    print("Bettercap version:", runner.version())
                except ToolkitError as exc:
                    print("Version check:", exc)
            elif choice == "2":
                print(get_network_info())
            elif choice == "3":
                print(runner.execute("help"))
            elif choice == "4":
                interface = input("Interface (e.g. eth0): ").strip()
                print(show_hosts(interface, runner))
            elif choice == "5":
                print("Only use in an isolated lab you own or are authorized to test.")
                print("Set BETTERCAP_LAB_MODE=1 before launching the toolkit to enable this module.")
                target = input("Private lab target IPv4: ").strip()
                interface = input("Lab interface: ").strip()
                confirmation = input('Type "I OWN THIS LAB" to continue: ')
                print(run_arp_lab(target, interface, confirmation, runner))
            elif choice == "6":
                print("Only use in an isolated lab with a domain you control.")
                print("Set BETTERCAP_LAB_MODE=1 before launching the toolkit to enable this module.")
                domain = input("Fully qualified lab domain: ").strip()
                redirect_ip = input("Private lab redirect IPv4: ").strip()
                interface = input("Lab interface: ").strip()
                confirmation = input('Type "I OWN THIS LAB" to continue: ')
                print(run_dns_lab(domain, redirect_ip, interface, confirmation, runner))
            elif choice == "7":
                print(packet_analysis_guidance())
            elif choice == "8":
                print(proxy_guidance())
            elif choice == "9":
                print("\n".join(diagnostics(runner)))
            elif choice == "10":
                print(cleanup_notice())
            elif choice == "11":
                body = input("Report summary (do not include secrets): ").strip()
                path = write_report(root / "reports", "Lab Report", body or "No summary supplied.")
                print(f"Report saved: {path}")
            else:
                print("Unknown option.")
        except (ToolkitError, ValueError, OSError) as exc:
            print(f"[ERROR] {exc}")
        except KeyboardInterrupt:
            print("\nCancelled by user.")
        _pause()
