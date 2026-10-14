import ipaddress
import re
from .exceptions import ValidationError

def private_ipv4(value: str) -> str:
    try:
        ip = ipaddress.ip_address(value.strip())
    except ValueError as exc:
        raise ValidationError("Enter a valid IPv4 address.") from exc
    if not isinstance(ip, ipaddress.IPv4Address) or not ip.is_private:
        raise ValidationError("Only private IPv4 addresses are accepted for lab targets.")
    if ip.is_loopback or ip.is_link_local or ip.is_multicast or ip.is_unspecified:
        raise ValidationError("This IP address is not accepted as a lab target.")
    return str(ip)

def interface_name(value: str) -> str:
    value = value.strip()
    if not re.fullmatch(r"[A-Za-z0-9_.:-]{1,32}", value):
        raise ValidationError("Invalid interface name.")
    return value

def domain_name(value: str) -> str:
    value = value.strip().rstrip(".").lower()
    if len(value) > 253 or not value or "/" in value or " " in value:
        raise ValidationError("Enter a valid lab domain name.")
    labels = value.split(".")
    if any(not re.fullmatch(r"(?!-)[a-z0-9-]{1,63}(?<!-)", label) for label in labels):
        raise ValidationError("Enter a valid lab domain name.")
    if "." not in value:
        raise ValidationError("Use a fully qualified lab domain (for example, lab.example).")
    return value

def require_confirmation(answer: str) -> None:
    if answer.strip() != "I OWN THIS LAB":
        raise ValidationError("Confirmation did not match. Operation cancelled.")
