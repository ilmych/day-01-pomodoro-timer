#!/usr/bin/env python3
"""
Pomodoro Timer CLI
Day 1 of 30 Days of Vibe Coding

A simple command-line Pomodoro timer with:
- 25-minute work sessions
- 5-minute short breaks
- 15-minute long breaks (every 4 pomodoros)
- Visual progress bar
- Sound notification (macOS)
"""

import sys
import time
import os
from datetime import datetime

# Timer durations (in minutes)
WORK_DURATION = 25
SHORT_BREAK = 5
LONG_BREAK = 15
POMODOROS_BEFORE_LONG_BREAK = 4

# Display settings
BAR_WIDTH = 40
CLEAR_LINE = "\033[K"
CURSOR_UP = "\033[A"


def play_sound():
    """Play a notification sound (macOS)."""
    # Try macOS system sounds
    sounds = [
        "/System/Library/Sounds/Glass.aiff",
        "/System/Library/Sounds/Ping.aiff",
        "/System/Library/Sounds/Pop.aiff",
    ]
    for sound in sounds:
        if os.path.exists(sound):
            os.system(f'afplay "{sound}" &')
            return
    # Fallback: terminal bell
    print("\a", end="", flush=True)


def format_time(seconds):
    """Format seconds as MM:SS."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}:{secs:02d}"


def progress_bar(current, total, width=BAR_WIDTH):
    """Create a progress bar string."""
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    percent = current / total * 100
    return f"[{bar}] {percent:.0f}%"


def countdown(minutes, label, session_num=None):
    """Run a countdown timer with progress display."""
    total_seconds = minutes * 60

    # Header
    if session_num:
        header = f"🍅 Pomodoro #{session_num}: {label}"
    else:
        header = f"☕ {label}"

    print(f"\n{header}")
    print("-" * 50)

    start_time = time.time()

    try:
        while True:
            elapsed = time.time() - start_time
            remaining = total_seconds - elapsed

            if remaining <= 0:
                break

            # Display progress
            progress = elapsed / total_seconds
            bar = progress_bar(elapsed, total_seconds)
            time_left = format_time(remaining)

            print(f"\r{CLEAR_LINE}  {bar}  {time_left} remaining", end="", flush=True)

            time.sleep(0.5)

        # Timer complete
        print(f"\r{CLEAR_LINE}  {progress_bar(1, 1)}  Done!     ")
        play_sound()
        return True

    except KeyboardInterrupt:
        print(f"\r{CLEAR_LINE}  Timer paused at {format_time(remaining)}")
        return False


def run_pomodoro_session():
    """Run a complete Pomodoro session."""
    pomodoro_count = 0

    print("\n" + "=" * 50)
    print("   🍅 POMODORO TIMER")
    print("=" * 50)
    print(f"\n  Work: {WORK_DURATION} min | Short break: {SHORT_BREAK} min | Long break: {LONG_BREAK} min")
    print("  Press Ctrl+C to pause/exit")

    try:
        while True:
            pomodoro_count += 1

            # Work session
            if not countdown(WORK_DURATION, "FOCUS TIME", pomodoro_count):
                raise KeyboardInterrupt

            print(f"\n  ✅ Pomodoro #{pomodoro_count} complete!")

            # Determine break type
            if pomodoro_count % POMODOROS_BEFORE_LONG_BREAK == 0:
                break_type = "LONG BREAK"
                break_duration = LONG_BREAK
                print(f"  🎉 You've completed {pomodoro_count} pomodoros! Time for a long break.")
            else:
                break_type = "SHORT BREAK"
                break_duration = SHORT_BREAK
                next_long = POMODOROS_BEFORE_LONG_BREAK - (pomodoro_count % POMODOROS_BEFORE_LONG_BREAK)
                print(f"  ({next_long} more until long break)")

            # Break
            input("\n  Press Enter to start break...")
            if not countdown(break_duration, break_type):
                raise KeyboardInterrupt

            print("\n  Break over!")
            input("  Press Enter to start next pomodoro...")

    except KeyboardInterrupt:
        print("\n")
        print("=" * 50)
        print(f"  Session ended. Completed {pomodoro_count - 1} pomodoros.")
        print("=" * 50)


def main():
    """Entry point."""
    # Quick demo mode for testing
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        global WORK_DURATION, SHORT_BREAK, LONG_BREAK
        WORK_DURATION = 0.1  # 6 seconds
        SHORT_BREAK = 0.05   # 3 seconds
        LONG_BREAK = 0.1     # 6 seconds
        print("🧪 Demo mode: Using short timers for testing")

    run_pomodoro_session()


if __name__ == "__main__":
    main()
