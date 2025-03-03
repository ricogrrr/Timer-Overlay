# Timer Overlay

A simple transparent timer overlay that stays on top of other windows. The timer is controlled using hotkeys and displays in the top-right corner of your screen.

## Features
- Transparent green overlay
- Always stays on top of other windows
- Hotkey controls
- Hours:Minutes:Seconds display format

## Requirements
- Python 3.x
- keyboard package

## Installation

1. Clone or download this repository
2. Install the required package:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python timer_overlay.py
```

### Hotkeys
- **F5**: Start the timer
- **F6**: Stop the timer
- **F7**: Reset the timer to 0.00

## Note
The keyboard package might require administrator privileges on some systems to capture global hotkeys. 
