import pkg_resources
import platform


allure_executables = {
    'Darwin': {
        'x86_64': 'lib/allurectl_darwin_amd64'
    },
    'Linux': {
        'arm': 'lib/allurectl_linux_arm64',
        'i386': 'lib/allurectl_linux_386',
        'x86_64': 'lib/allurectl_linux_amd64'
    },
    'Windows': {
        'x86_64': 'lib/allurectl_windows_amd64.exe',
        'arm': 'lib/allurectl_windows_arm64.exe',
    }
}

def get_allure_executable() -> str:
    executable = allure_executables[platform.system()][platform.machine()]
    return pkg_resources.resource_filename('easy_allure', executable)
