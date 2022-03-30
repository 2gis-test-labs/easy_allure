from asyncio import exceptions
import os
import shutil
import subprocess
from typing import Tuple
from urllib import request


def run_cmd(cmd: str, timeout: int = 300) -> Tuple[str, str]:
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True,
                            shell=True)
    stdout, stderr = proc.communicate(timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError('Failed to run <{}>, got {}'.format(cmd, stderr))
    return stdout, stderr


def download_file(file_url: str, dest_dir: str, dest_file_name: str,
                  mode: int = 0o755) -> None:
    is_dir_exists = os.path.exists(dest_dir)
    if not is_dir_exists:
        os.makedirs(dest_dir)
    full_path = os.path.join(dest_dir, dest_file_name)
    try:
        request.urlretrieve(file_url, full_path)
        os.chmod(full_path, mode)
    except Exception as err:
        if not is_dir_exists:
            shutil.rmtree(dest_dir)
        raise err

