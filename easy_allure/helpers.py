import subprocess
from typing import Tuple


def run_cmd(cmd: str, timeout: int = 60) -> Tuple[str, str]:
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            shell=True)
    stdout, stderr = proc.communicate(timeout=timeout)
    print(stdout)
    print(stderr)
    if proc.returncode != 0:
        raise RuntimeError('Failed to run <{}>, got {}'.format(cmd, stderr))
    return stdout, stderr
