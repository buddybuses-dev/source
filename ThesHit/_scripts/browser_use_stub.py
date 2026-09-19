#!/usr/bin/env python3
"""
ThesHit browser-use STUB — dry-run by default.

Does NOT open a browser or scrape unless THESHIT_BROWSER_LIVE=1.
Maps to tickets T-009 / T-010 (browser-gated ThesHit scrape;
remaining modules historically blocked on logged-in browser e.g. the-faction.mn.co).

Usage:
  python browser_use_stub.py --url https://example.com --module 09_anything-about-game
  THESHIT_BROWSER_LIVE=1 python browser_use_stub.py ...  # live path (not implemented here)
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone


DEFAULT_MODULE = "09_anything-about-game"
PLANNED_STEPS = [
    "Resolve target URL / module folder under ThesHit/",
    "Load browser-use from rooms/production/repos/agent-frameworks/browser-use (venv later)",
    "Plan navigation + extract selectors for browser-gated page",
    "Write scrape notes into module folder / 08_clief-notes as appropriate",
    "Update _NEXT-SCRAPE.md / _STATUS.md after run (live only)",
]


def env_live() -> bool:
    return os.environ.get("THESHIT_BROWSER_LIVE", "0").strip() in ("1", "true", "TRUE", "yes", "YES")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="ThesHit browser-use stub (dry-run unless THESHIT_BROWSER_LIVE=1)",
    )
    p.add_argument(
        "--url",
        default="https://example.com",
        help="Target URL to plan against (default: example.com)",
    )
    p.add_argument(
        "--module",
        default=DEFAULT_MODULE,
        help=f"ThesHit module folder name (default: {DEFAULT_MODULE})",
    )
    p.add_argument(
        "--list-steps",
        action="store_true",
        help="Only print planned steps and exit",
    )
    return p


def print_plan(url: str, module: str, live: bool) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    mode = "LIVE (refused by stub — implement later)" if live else "DRY-RUN"
    print(f"[theshit-browser-use-stub] {now}")
    print(f"  mode:    {mode}")
    print(f"  url:     {url}")
    print(f"  module:  {module}")
    print(f"  live_env: THESHIT_BROWSER_LIVE={os.environ.get('THESHIT_BROWSER_LIVE', '0')}")
    print("  planned steps:")
    for i, step in enumerate(PLANNED_STEPS, 1):
        print(f"    {i}. {step}")
    if live:
        print()
        print("REFUSING live browser launch in stub.")
        print("Set up browser-use venv per _scripts/BROWSER-USE.md, then implement live path.")
        print("Exiting 0 without opening a browser.")
    else:
        print()
        print("Dry-run complete. No browser opened. No network scrape.")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    live = env_live()
    if args.list_steps:
        for i, step in enumerate(PLANNED_STEPS, 1):
            print(f"{i}. {step}")
        return 0
    print_plan(args.url, args.module, live)
    return 0


if __name__ == "__main__":
    sys.exit(main())
