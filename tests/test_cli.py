import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"


def run_cli(*args: str) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(SRC_PATH)
    cmd = [sys.executable, "-m", "offline_vm_toolkit", *args]
    return subprocess.run(cmd, capture_output=True, text=True, env=env, check=False)


def test_hello():
    result = run_cli("hello", "--name", "Tester")
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, Tester!"


def test_version():
    result = run_cli("version")
    assert result.returncode == 0
    assert result.stdout.strip() == "0.1.0"
