import logging
from logging.handlers import RotatingFileHandler

def setup_logging(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    root = logging.getLogger()
    if root.handlers:
        return
    root.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    file_handler = RotatingFileHandler(path, maxBytes=1_000_000, backupCount=3)
    file_handler.setFormatter(fmt)
    root.addHandler(console)
    root.addHandler(file_handler)
