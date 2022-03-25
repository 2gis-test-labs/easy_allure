import argparse
import os
import sys

from .helpers import run_cmd
from .allurectl import get_allure_executable
from .exceptions import ScriptException


def create_launch(launch_name: str) -> str:
    cmd = '{} launch create --launch-name {} ' \
          '--no-header --format ID | tail -n1'.format(get_allure_executable(), launch_name)
    try:
        launch_id, _ = run_cmd(cmd)
        launch_id = launch_id.strip()
    except RuntimeError as err:
        errMessage = 'Failed to create launch: {}'.format(err)
        raise ScriptException(errMessage)
    return launch_id


def upload_launch(reports_path: str, launch_id: str) -> None:
    cmd = '{} upload {} --launch-id {}' \
          .format(get_allure_executable(), reports_path, launch_id)
    try:
        run_cmd(cmd)
    except RuntimeError as err:
        errMessage = 'Failed to upload launch: {}'.format(err)
        raise ScriptException(errMessage)


def close_launch(launch_id: str) -> None:
    cmd = '{} launch close {}'.format(get_allure_executable(), launch_id)
    try:
        run_cmd(cmd)
    except RuntimeError as err:
        errMessage = 'Failed to close launch: {}'.format(err)
        raise ScriptException(errMessage)


def send_to_testops(parsed_args: argparse.Namespace) -> int:
    launch_id = create_launch(parsed_args.launch_name)
    upload_launch(parsed_args.reports_path, launch_id)
    close_launch(launch_id)

    allure_endpoint = os.environ.get('ALLURE_ENDPOINT')
    print('Test run was successfully pushed to {}/launch/{}'
          .format(allure_endpoint, launch_id))
    return 0


def main():
    parser = argparse.ArgumentParser(prog='easy_allure')
    parser.add_argument('action', nargs='?')
    parser.add_argument('-l', '--launch-name', dest='launch_name',
                        default='default_launch_name')
    parser.add_argument('-r', '--reports-path', dest='reports_path',
                        default='./allure_reports')
    parsed_args = parser.parse_args()

    actions = {
        'send': send_to_testops
    }

    if parsed_args.action not in actions.keys():
        print('<{}> action is not supported, plase select from {}'
              .format(parsed_args.action, actions.keys()))
        sys.exit(2)

    try:
        sys.exit(actions[parsed_args.action](parsed_args))
    except Exception as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    main()
