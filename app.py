import os
import sys
import subprocess
import venv
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV_DIR = ROOT / ".venv"
REQUIREMENTS = ROOT / "requirements.txt"


def _venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def _deps_available() -> bool:
    try:
        import IPy  # noqa: F401
        import netaddr  # noqa: F401
        import pandas  # noqa: F401
        return True
    except ImportError:
        return False


def _ensure_venv() -> None:
    if VENV_DIR.exists():
        return
    print(f"Creating virtual environment at {VENV_DIR} ...")
    venv.create(VENV_DIR, with_pip=True)
    py = str(_venv_python())
    print("Installing dependencies into the virtual environment ...")
    subprocess.check_call([py, "-m", "pip", "install", "--quiet", "-r", str(REQUIREMENTS)])


def main() -> None:
    if _deps_available():
        from Menu.user_menu import user_menu
        user_menu()
        return

    _ensure_venv()
    sys.exit(subprocess.call([str(_venv_python()), str(Path(__file__).resolve())]))


if __name__ == "__main__":
    main()
