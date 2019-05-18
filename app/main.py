#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from argparse import RawTextHelpFormatter, \
    Namespace, ArgumentParser
import sys
import os
from cli import Client


def main():
    platform = sys.platform
    kwargs = {"platform": platform}
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
    print(kwargs["path"])
    if arguments.output:
        if os.path.isdir(arguments.output):
            kwargs["output"] = arguments.output
        else:
            raise NotADirectoryError("Target output path is not directory")
    else:
        kwargs["output"] = ""

    if arguments.graphics:
        pass
        # Starts graphics session.
    else:
        client = Client(kwargs["platform"], kwargs["path"], kwargs["output"],
                        kwargs["restore"])
        print(client.rest)
        if client.rest:
            client.restore()
        else:
            client.get_tree()
            client.backup()


args_parser = ArgumentParser(description="Backup client application",
                             formatter_class=RawTextHelpFormatter)
args_parser.add_argument('-g' '--graphics', dest='graphics', action='store_true',
                         help='Enables GUI')
args_parser.add_argument('--no-graphics', dest='graphics', action='store_false',
                         help='Disables GUI')
args_parser.set_defaults(graphics=False)
args_parser.add_argument('-p', '--path', action='store',
                         help='Path to directory for backup')
args_parser.add_argument('-o', '--output', action='store',
                         help='Path where the backup will be stored')
args_parser.add_argument('-r', '--restore', action='store_true',
                         help='Restores backup from target path to output',
                         default=False)
arguments: Namespace = args_parser.parse_args()
print(type(arguments))
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as error:
        print(error)
