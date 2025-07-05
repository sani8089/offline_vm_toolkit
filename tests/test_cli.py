import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from offline_vm_toolkit.cli import main
from offline_vm_toolkit import __version__


def test_greet(capsys):
    main(['greet', 'Tester'])
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Hello, Tester!'


def test_version(capsys):
    main(['version'])
    captured = capsys.readouterr()
    assert captured.out.strip() == __version__
