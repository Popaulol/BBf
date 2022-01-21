import subprocess
import sys


def mypy_test(
    dir: str, config_file: str = "mypy.ini"
) -> bool | subprocess.CompletedProcess:
    res = subprocess.run(
        ["mypy", "--config-file", config_file, dir], capture_output=False
    )
    return res.returncode == 0


def main() -> None:
    print("Running Mypy...")
    res = mypy_test("./src")


main()
