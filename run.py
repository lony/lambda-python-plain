#!/usr/bin/env python
#
# Script to deploy lambda function

import subprocess
import argparse

lambda_name = 'plain-python'
zip_name = 'bundle.zip'
region = 'eu-west-1'
account = ''
role = 'log_eu-west-1'


def run_cmd(cmd, output_return=False):
    """
    Runs command on system and returns result output.
    :param cmd: The command to execute
    :param output_return: Should the console output be returned
    :return: Output of the console OR status
    """
    if output_return:
        return subprocess.check_output(cmd)
    else:
        return subprocess.call(cmd)


def zip_bundle():
    run_cmd(['zip', '-9', zip_name, 'handler.py'])
    run_cmd(['zip', '-r9', zip_name, 'psycopg2/'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-z', '--zip', action='store_true', help='Zip Lambda')
    parser.add_argument('-c', '--create', action='store_true', help='Create Lambda')
    parser.add_argument('-u', '--update', action='store_true', help='Update Lambda')

    args = parser.parse_args()

    if args.zip:
        zip_bundle()
    elif args.create:
        zip_bundle()
        run_cmd(['aws', 'lambda', 'create-function',
                 '--region', region,
                 '--function-name', lambda_name,
                 '--zip-file', 'fileb://' + zip_name,
                 '--role', 'arn:aws:iam::' + account + ':role/' + role,
                 '--handler', 'handler.lambda_handler',
                 '--runtime', 'python2.7',
                 '--timeout', '15',
                 '--memory-size', '512'])
    elif args.update:
        zip_bundle()
        run_cmd(['aws', 'lambda', 'update-function-code',
                 '--function-name', lambda_name,
                 '--zip-file', 'fileb://' + zip_name])
    else:
        print parser.print_help()
