from datetime import datetime, timezone
from pathlib import Path

def write_report(report_dir: str | Path, title: str, body: str) -> Path:
    report_dir = Path(report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_title = "".join(c.lower() if c.isalnum() else "-" for c in title).strip("-") or "report"
    path = report_dir / f"{stamp}-{safe_title}.md"
    path.write_text(f"# {title}\n\nGenerated: {stamp}\n\n{body.strip()}\n", encoding="utf-8")
    return path
