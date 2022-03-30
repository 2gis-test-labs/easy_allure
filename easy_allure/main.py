import argparse
import sys

from .testops import get_available_actions
from .allurectl import ALLURECTL_VERSION, check_allurectl


allurectl_version = ALLURECTL_VERSION.replace('.', '')
__version__ = '1.0.0.{}'.format(allurectl_version)


@check_allurectl
def main():
    print('Running easy_allure v{}'.format(__version__))

    parser = argparse.ArgumentParser(prog='easy_allure')
    parser.add_argument('action')
    parser.add_argument('reports_path')
    parser.add_argument('-l', '--launch-name', dest='launch_name',
                        default='default_launch_name')
    parsed_args = parser.parse_args()

    actions = get_available_actions()
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
