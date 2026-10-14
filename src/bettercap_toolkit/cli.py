"""CLI helpers."""
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Bettercap Toolkit")
    parser.add_argument("--version", action="version", version="Bettercap Toolkit 1.0.0")
    return parser
