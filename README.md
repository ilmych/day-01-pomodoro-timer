# Pomodoro Timer

> A Pomodoro timer with both CLI and browser versions.

Built as part of [30 Days of Vibe Coding](../README.md) - Day 1.

## What it does

The Pomodoro Technique helps you focus by breaking work into intervals (traditionally 25 minutes) separated by short breaks. This timer handles the timing for you with visual feedback and audio notifications.

Features:
- 25-minute work sessions
- 5-minute short breaks
- 15-minute long breaks (every 4 pomodoros)
- Visual progress indicator
- Sound notifications
- Session counter
- Total focus time tracking

## Two Versions

### Web Version (Recommended)

Just open `index.html` in your browser. No server needed.

- Circular progress ring
- Color-coded sessions (purple=work, green=short break, orange=long break)
- Browser notifications
- Keyboard shortcuts: Space (start/pause), R (reset), S (skip)
- Updates page title with timer

### CLI Version

```bash
python3 pomodoro.py

# Demo mode (short timers for testing)
python3 pomodoro.py --demo
```

## Demo

**Web UI:**
- Purple gradient background during focus
- Green gradient during short breaks
- Orange gradient during long breaks
- Smooth circular progress animation

**CLI:**
```
🍅 Pomodoro #1: FOCUS TIME
--------------------------------------------------
  [████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 30%  17:30 remaining
```

## How I built it

- **Time**: ~1 hour (CLI + Web)
- **Stack**: Python 3 (CLI), vanilla HTML/CSS/JS (Web)
- **AI assist**: Claude Code

## What I learned

1. **CSS gradients for mood** - Different background colors for work/break states make the timer feel more alive.

2. **SVG circle progress** - Using `stroke-dasharray` and `stroke-dashoffset` to animate a circular progress indicator. The trick is rotating the SVG -90deg so it starts from the top.

3. **Web Audio API** - Generating tones programmatically instead of loading audio files. Created a pleasant C-E-G chord chime.

4. **Browser notifications** - `Notification.requestPermission()` lets you alert users even when the tab is in the background.

## Run locally

```bash
# Web version - just open the file
open index.html

# CLI version
python3 pomodoro.py
```

No dependencies. Works offline.
