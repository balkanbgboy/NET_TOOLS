# NET_TOOLS

A Python CLI with five tools useful for network engineers:

```
Enter:
 '1' Print IP addresses in IP range
 '2' Provide Network and Wildcard mask
 '3' Check Ip address/mask and provide network information
 '4' Create Subnets from Supernet
 '5' Subnet(Route) Summarization
 'q' to quit (Ctrl + C to exit at any time):
```

Options that produce a list of IPs or subnets can either print to the screen or save the result to a `.csv` file at a path you provide.

## Requirements

- Python 3.8 or newer (tested on 3.11+)
- Internet access on first run (to install dependencies)

## Run

```
python3 app.py
```

On the first run, `app.py` automatically:
1. Creates a virtual environment in `.venv/`
2. Installs the dependencies listed in `requirements.txt` (`IPy`, `netaddr`, `pandas`)
3. Re-executes itself inside the venv and shows the main menu

Subsequent runs reuse the existing `.venv` and start in well under a second.

## CSV output paths

When the program asks for a path to save CSV files (options `1`, `4`), paste any folder path. The folder is created if it does not already exist.

- **Windows** (PowerShell / cmd): `C:\Users\you\Desktop\NET-Tools`
- **Linux / macOS**: `/home/you/net-tools`
- **WSL**: either a native WSL path (`/home/you/...`) or a Windows path (`C:\Users\you\...`) — both work; Windows paths are auto-translated to `/mnt/c/...`.

## Subnet summarization

Option `5` reads subnet entries from `Subnets.txt` (one CIDR per line) located in the project root, then prints a summarized list of the merged ranges. Edit `Subnets.txt` before running the option.

## CONTRIBUTORS
1. balkanbgboy
