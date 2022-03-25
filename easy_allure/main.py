import argparse
import os
import sys

import pkg_resources
from .helpers import run_cmd


def send_to_testops(launch_name: str, reports_path: str) -> int:
    allurectl = pkg_resources.resource_filename('easy_allure', 'lib/allurectl')
    cmd = '{} launch create --launch-name {} ' \
          '--no-header --format ID | tail -n1'.format(allurectl, launch_name)
    try:
        launch_id, _ = run_cmd(cmd)
        launch_id = launch_id.strip()
    except RuntimeError as err:
        print('Failed to create launch: {}'.format(err))
        return 1

    cmd = '{} upload {} --launch-id {}' \
          .format(allurectl, reports_path, launch_id)
    try:
        run_cmd(cmd)
    except RuntimeError as err:
        print('Failed to upload launch: {}'.format(err))
        return 1

    cmd = '{} launch close {}'.format(allurectl, launch_id)
    try:
        run_cmd(cmd)
    except RuntimeError as err:
        print('Failed to close launch: {}'.format(err))
        return 1

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
        sys.exit(1)

    sys.exit(actions[parsed_args.action](
        launch_name=parsed_args.launch_name,
        reports_path=parsed_args.reports_path
    ))


if __name__ == '__main__':
    main()
