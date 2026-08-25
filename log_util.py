# log_util.py
# Minimal logger for Vossberg Mobility KM-Waechter.
# Modernized 2024: context manager, cleared dead debug branch, idiomatic list clear.

import time

LOG_LINES: list[str] = []  # module-level buffer; flushed to disk by flush_log()


def log(message: str) -> None:
    """Append a timestamped line to the in-memory log buffer and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def flush_log(path: str) -> None:
    """Write all buffered log lines to the given file and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    LOG_LINES.clear()
