# System Help 

A Python CLI tool that provides interactive documentation for functions and libraries using the built-in `help()` command. Outputs color-coded, structured text for an improved terminal experience.

## Features

- Prompts the user for a function or library name
- Displays full documentation via `help()`
- Color-coded and structured terminal output
- Loops until the user types `FIM` to exit

## Requirements

- Python 3.x

## Setup

1. Clone the repository:
```bash
git clone https://github.com/gomesmc/System_Help_Python.git
cd System_Help_Python
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

## Usage

```bash
python helpPython.py
```

Enter any Python function or library name to view its documentation. Type `FIM` to exit.
FIM is the exit keyword defined in the source code.
