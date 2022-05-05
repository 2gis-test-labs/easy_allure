import os
from typing import List

import pkg_resources

from .helpers import download_file
from .logger import get_logger

ALLURECTL_VERSION = '1.21.2'
LOGGER = get_logger(__name__)

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


def get_allure_executable(platform: str) -> str:
    platform = platform or 'auto'

    system = platform.system() if platform == 'auto' \
        else platform.split('.')[0]
    machine = platform.machine() if platform == 'auto' \
        else platform.split('.')[1]
    try:
        executable = allure_executables[system][machine]
    except Exception:
        raise OSError('Failed to find executable for your platform')
    return executable


def download_allurectl(dest_dir: str, platform: str = None) -> None:
    executable_name = get_allure_executable(platform)
    file_url = 'https://github.com/allure-framework/allurectl/'\
               'releases/download/{}/{}'\
               .format(ALLURECTL_VERSION, executable_name)
    LOGGER.info('Downloading allurectl from {}'.format(file_url))
    download_file(file_url, dest_dir, executable_name)


def install_allurectl(platform: str = None) -> str:
    bin_dir = pkg_resources.resource_filename('easy_allure', '/bin/')
    path = os.path.join(bin_dir, get_allure_executable(platform))
    if not os.path.exists(path):
        download_allurectl(bin_dir, platform)
    return path


def get_platforms() -> List:
    platforms = []
    for operation_sys, executables in allure_executables.items():
        for platform in executables.keys():
            platforms.append('{}.{}'.format(operation_sys, platform))
    return platforms
