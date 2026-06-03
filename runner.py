import subprocess
import argparse
import sys
import os
from pathlib import Path

from colorama import Fore

def main():
    BASE_DIR = Path(__file__).resolve().parent
    DJANGO_DIR = BASE_DIR / "FinanceTrackerAPI"
    VENV_PYTHON = BASE_DIR / ".venv" / "bin" / "python3"

    if not VENV_PYTHON.exists():
        VENV_PYTHON = Path(sys.executable)

    parser = argparse.ArgumentParser(description="Script for easier run django server")

    parser.add_argument(
        "-m",
        "--migrate",
        action="store_true",
        help="Run server with migration",
    )

    parser.add_argument(
        "-mm",
        "--makemigration",
        action="store_true",
        help="Run server with making migrations",
    )

    args = parser.parse_args()
    run_kwargs = {"cwd": str(DJANGO_DIR), "check": True}

    if args.makemigration:
        print(Fore.GREEN + "[LOG]" + Fore.RESET + ": Starting makemigrations")
        subprocess.run([str(VENV_PYTHON), "manage.py", "makemigrations"], **run_kwargs)
        subprocess.run([str(VENV_PYTHON), "manage.py", "migrate"], **run_kwargs)


    elif args.migrate:
        print(Fore.GREEN + "[LOG]" + Fore.RESET + ": Starting migrate")
        subprocess.run([str(VENV_PYTHON), "manage.py", "migrate"], **run_kwargs)


    print(Fore.GREEN + "[LOG]" + Fore.RESET + ": Starting django server")
    try:
        subprocess.run([str(VENV_PYTHON), "manage.py", "runserver"], **run_kwargs)
    except KeyboardInterrupt:
        print("\n" + Fore.YELLOW + "[WARNING]" + Fore.RESET + ": Server stopped by user")


if __name__ == "__main__":
    main()
