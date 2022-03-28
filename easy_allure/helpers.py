import subprocess
import os
from typing import Tuple
from urllib import request


def run_cmd(cmd: str, timeout: int = 60) -> Tuple[str, str]:
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            shell=True)
    stdout, stderr = proc.communicate(timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError('Failed to run <{}>, got {}'.format(cmd, stderr))
    return stdout, stderr


def download_file(file_url, dest_file_name, mode=0o755) -> None:
    request.urlretrieve(file_url, dest_file_name)
    os.chmod(dest_file_name, mode)
