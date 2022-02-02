import shlex
import subprocess


def test_main():
    expected = 'Same thing over and over and expecting different results.'
    cmd = 'python gumazon "Same thing over and over and expecting different results."'
    actual = subprocess.run(shlex.split(cmd), check=True, capture_output=True).stdout.decode().strip().strip("[]'")     # .stdout.decode().strip()
    assert actual == expected

