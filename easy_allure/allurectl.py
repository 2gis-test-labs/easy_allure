import platform
import subprocess
import sys

import pkg_resources

from .helpers import download_file


ALLURECTL_VERSION = '1.21.2'

allure_executables = {
    'Darwin': {
        'x86_64': 'allurectl_darwin_amd64'
    },
    'Linux': {
        'arm': 'allurectl_linux_arm64',
        'i386': 'allurectl_linux_386',
        'x86_64': 'allurectl_linux_amd64'
    },
    'Windows': {
        'x86_64': 'allurectl_windows_amd64.exe',
        'arm': 'allurectl_windows_arm64.exe',
    }
}


def get_allure_executable() -> str:
    try:
        executable = allure_executables[platform.system()][platform.machine()]
    except Exception:
        raise OSError('Failed to find executable for your platform')
    return executable


def download_allurectl() -> None:
    executable_name = get_allure_executable()
    file_url = 'https://github.com/allure-framework/allurectl/'\
               'releases/download/{}/{}'\
               .format(ALLURECTL_VERSION, executable_name)
    dest_dir = pkg_resources.resource_filename('easy_allure', '/bin/')
    download_file(file_url, dest_dir, executable_name)


def run_allurectl() -> None:
    executable = get_allure_executable()
    command = [pkg_resources.resource_filename('easy_allure',
                                               '/bin/{}'.format(executable))]
    command.extend(sys.argv[1:])
    subprocess.call(command)
