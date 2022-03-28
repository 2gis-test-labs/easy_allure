import platform
from urllib import request

import pkg_resources


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
        return 'allurectl_linux_amd64'
        executable = allure_executables[platform.system()][platform.machine()]
        # executable = pkg_resources.resource_filename('easy_allure', executable)
    except Exception as err:
        raise OSError('Failed to find executable for your platform')
    return executable

def download_allurectl():
    executable_name = get_allure_executable()
    download_link = 'https://github.com/allure-framework/allurectl/releases/download/{}/{}'\
                    .format(ALLURECTL_VERSION, executable_name)
    print('downloading allurectl from {}'.format(download_link))
    download_path = './easy_allure/lib/allurectl'
    request.urlretrieve(download_link, download_path)
