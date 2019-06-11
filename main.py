#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
This is the main file in this application.
It works as controller for cli and gui.
"""
from argparse import RawTextHelpFormatter, \
    Namespace, ArgumentParser
import sys
import os
from app.cli import Client


def main():
    """
    The main method that is called in
    begining of program
    """
    platform = sys.platform
    kwargs = {"platform": platform, "compression": arguments.compression,
              "encryption": arguments.encryption}
    if arguments.restore:
        kwargs["restore"] = True
    else:
        kwargs["restore"] = False

    if arguments.path:

        kwargs["path"] = arguments.path

    else:
        if platform == "linux":
            kwargs["path"] = "/home/"
        elif "win" in platform:
            kwargs["path"] = "C:"

    if arguments.output:
        if os.path.isdir(arguments.output):
            kwargs["output"] = arguments.output
        else:
            raise NotADirectoryError("Target output path is not directory")

    if arguments.graphics:
        # Starts graphics session.
        os.system("python gui.py")
    else:

        client = Client(kwargs)
        if kwargs["restore"]:
            client.split_backup()
            client.restore()
        else:
            client.get_tree()
            client.backup()


ARGS_PARSER = ArgumentParser(description="Backup client application",
                             formatter_class=RawTextHelpFormatter)
ARGS_PARSER.add_argument('-g', '--graphics', dest='graphics',
                         action='store_true', help='Enables GUI')
ARGS_PARSER.add_argument('--no-graphics', dest='graphics',
                         action='store_false', help='Disables GUI')
ARGS_PARSER.add_argument('-p', '--path', action='store',
                         help='Path to directory for backup',
                         default="")
ARGS_PARSER.add_argument('-o', '--output', action='store',
                         help='Path where the backup will be stored',
                         default="")
ARGS_PARSER.add_argument('-r', '--restore', action='store_true',
                         help='Restores backup from target path to output',
                         default=False)
ARGS_PARSER.add_argument('-c', '--compression', action='store_true',
                         help="Compress files using gzip",
                         default=False)
ARGS_PARSER.add_argument('-e', '--encryption', action='store_true',
                         help="Encrypt files in backup",
                         default=False)
arguments: Namespace = ARGS_PARSER.parse_args()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as error:
        print(error)
