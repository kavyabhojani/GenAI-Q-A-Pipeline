"""
Simple logger utility for GenAI Q&A Pipeline.
Provides consistent INFO/ERROR messages with timestamps.
"""
import datetime

def _ts() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_info(message: str) -> None:
    print(f"[INFO]  {_ts()} - {message}")

def log_error(message: str) -> None:
    print(f"[ERROR] {_ts()} - {message}")
